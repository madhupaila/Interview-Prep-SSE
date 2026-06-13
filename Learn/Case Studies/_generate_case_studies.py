#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate case study markdown from HLD/LLD question files + overrides."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
LEARN = ROOT.parent
HLD_ROOT = LEARN / "System Design - High Level Design"
LLD_ROOT = LEARN / "System Design - Low Level Design"

sys.path.insert(0, str(ROOT))
from _paired_topics_registry import (  # noqa: E402
    GOLD_STANDARD_SKIP,
    PAIRED_TOPICS,
    pair_by_hld,
    pair_by_lld,
    pair_doc_name,
)
from _case_study_overrides import get_override  # noqa: E402

HLD_TRACKS = {
    "genai": ("hld/genai", "02-genai-llm-hld/questions", "HLD-G", "Gen AI / LLM HLD"),
    "classic": ("hld/classic", "03-classic-hld/questions", "HLD-C", "Classic HLD"),
}

LLD_TRACKS = {
    "classic-ood": ("lld/classic-ood", "02-classic-ood/questions", "LLD-O", "Classic OOD"),
    "design-patterns": ("lld/design-patterns", "03-design-patterns/questions", "LLD-P", "Design Patterns"),
    "concurrency": ("lld/concurrency", "04-concurrency-lld/questions", "LLD-X", "Concurrency LLD"),
    "genai": ("lld/genai", "05-genai-llm-lld/questions", "LLD-A", "Gen AI LLD"),
}


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.exists() else ""


def _extract_meta(text: str) -> dict[str, str]:
    meta: dict[str, str] = {}
    for key in ("Track", "Companies", "Difficulty"):
        m = re.search(rf"\*\*{key}:\*\*\s*(.+)", text)
        if m:
            meta[key.lower()] = m.group(1).strip()
    m = re.search(r"^#\s+(.+)$", text, re.M)
    meta["title"] = m.group(1).strip() if m else "Untitled"
    return meta


def _extract_section(text: str, *names: str) -> str:
    for name in names:
        pat = rf"(?:^|\n)(?:##?\s+\d*\.?\s*)?{re.escape(name)}[^\n]*\n(.*?)(?=\n##?\s|\Z)"
        m = re.search(pat, text, re.S | re.I)
        if m:
            return m.group(1).strip()
    return ""


def _extract_all_sections(text: str) -> dict[str, str]:
    sections: dict[str, str] = {}
    for m in re.finditer(r"^##\s+(?:\d+\.\s+)?(.+?)\s*$", text, re.M):
        start = m.end()
        nxt = re.search(r"^##\s+", text[start:], re.M)
        end = start + nxt.start() if nxt else len(text)
        sections[m.group(1).strip()] = text[start:end].strip()
    return sections


def _rel(from_dir: Path, to: Path) -> str:
    return Path(os_relpath(from_dir, to)).as_posix()


def os_relpath(from_dir: Path, to: Path) -> str:
    try:
        return str(to.relative_to(from_dir.parent)).replace("\\", "/")
    except ValueError:
        import os
        return os.path.relpath(to, from_dir.parent).replace("\\", "/")


def _cs_id(prefix: str, num: int) -> str:
    return f"CS-{prefix}{num:02d}"


def _stakeholders(override: dict, title: str) -> str:
    rows = override.get("stakeholders") or [
        ("End user", "Complete core flows quickly", "Slow, unreliable UX", "Task completion rate > 95%"),
        ("Product owner", "Ship MVP on schedule", "Scope creep", "On-time V1 delivery"),
        ("SRE / platform", "Meet SLO with observability", "Opaque failures", "Error budget > 0 monthly"),
        ("Security / compliance", "Data protection, audit trail", "Regulatory breach", "Zero critical findings"),
    ]
    lines = ["| Persona | Goals | Pain points | Success metric |", "|---------|-------|-------------|----------------|"]
    for r in rows:
        lines.append(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} |")
    return "\n".join(lines)


def _moscow_fr(override: dict, functional: str, problem: str) -> str:
    must = override.get("fr_must") or []
    should = override.get("fr_should") or []
    could = override.get("fr_could") or []
    wont = override.get("fr_wont") or ["Multi-region active-active", "Advanced ML personalization"]
    if not must and functional:
        for line in functional.split("\n"):
            line = line.strip("- ").strip()
            if line:
                must.append((line, "Verified in integration tests"))
    if not must:
        must = [(f"Core {problem[:60]}…", "E2E test passes")]
    lines = ["| Priority | Requirement | Acceptance criteria |", "|----------|-------------|---------------------|"]
    for pri, items in [("Must", must), ("Should", should), ("Could", could), ("Won't (MVP)", wont)]:
        for item in items:
            if isinstance(item, tuple):
                lines.append(f"| {pri} | {item[0]} | {item[1]} |")
            else:
                lines.append(f"| {pri} | {item} | Documented in PRD |")
    return "\n".join(lines)


def _nfr_table(override: dict, nfr_text: str, is_genai: bool) -> str:
    defaults = override.get("nfr_table") or []
    if not defaults:
        defaults = [
            ("Latency", "p99 < 500ms sync API; p99 < 8s LLM" if is_genai else "p99 < 200ms", "APM / distributed tracing"),
            ("Availability", "99.9%", "Uptime SLO dashboard"),
            ("Throughput", "10K peak QPS (scale phase)", "Load test report"),
            ("Security", "AuthN/Z, encryption at rest/transit", "Annual pen test"),
            ("Maintainability", "Modular services, ADRs documented", "Change failure rate < 15%"),
        ]
        if is_genai:
            defaults.append(("LLM faithfulness", "Citation accuracy > 95% on eval set", "Offline eval pipeline"))
    lines = ["| Attribute | Target | Measurement |", "|-----------|--------|-------------|"]
    for a, t, m in defaults:
        lines.append(f"| {a} | {t} | {m} |")
    if nfr_text:
        lines.append("")
        lines.append("**From requirements analysis:**")
        lines.append(nfr_text.strip())
    return "\n".join(lines)


def _constraints(override: dict) -> str:
    rows = override.get("constraints") or [
        ("Budget", "$50K/month infra at V1 scale", "Prefer managed services over self-host"),
        ("Team", "2 backend, 1 frontend, 1 ML engineer", "MVP scope strictly bounded"),
        ("Timeline", "MVP in 8 weeks", "Defer nice-to-have features"),
        ("Tech", "Cloud-native on AWS/GCP", "Use existing org SSO and VPC"),
        ("Build vs buy", "Buy vector DB / LLM API; build orchestration", "Focus engineering on differentiation"),
    ]
    lines = ["| Constraint | Detail | Impact on design |", "|------------|--------|------------------|"]
    for r in rows:
        lines.append(f"| {r[0]} | {r[1]} | {r[2]} |")
    return "\n".join(lines)


def _adrs(override: dict, tradeoffs: str, title: str) -> str:
    adrs = override.get("adrs") or []
    if not adrs:
        adrs = [
            {
                "id": "001",
                "title": "Primary architecture pattern",
                "context": f"Need to balance delivery speed, operability, and scale for {title}.",
                "decision": "Event-driven async for writes; cache-heavy sync read path.",
                "consequences": "Higher eventual consistency on analytics; simpler peak handling.",
                "alternatives": "Fully synchronous CRUD — rejected due to peak QPS.",
            },
            {
                "id": "002",
                "title": "Data store selection",
                "context": "Mixed OLTP, cache, and search/vector needs.",
                "decision": "PostgreSQL for source of truth; Redis for hot path; specialized index where needed.",
                "consequences": "Operational complexity of multiple stores; optimal per access pattern.",
                "alternatives": "Single document DB — rejected for strong consistency requirements.",
            },
            {
                "id": "003",
                "title": "Multi-tenancy model",
                "context": "B2B SaaS with strict isolation requirements.",
                "decision": "Logical tenant_id on all rows + encryption per tenant for sensitive payloads.",
                "consequences": "Cost-effective vs physical isolation; requires rigorous integration tests.",
                "alternatives": "Database-per-tenant — rejected at 10K tenant scale.",
            },
        ]
    parts = []
    for a in adrs:
        parts.append(f"""### ADR-{a['id']}: {a['title']}

**Status:** Accepted  
**Context:** {a['context']}  
**Decision:** {a['decision']}  
**Consequences:** {a['consequences']}  
**Alternatives considered:** {a['alternatives']}

""")
    if tradeoffs.strip():
        parts.append("### Tradeoffs Summary (from design analysis)\n\n")
        parts.append(tradeoffs.strip())
        parts.append("\n")
    return "\n".join(parts)


def _roadmap(override: dict, title: str) -> str:
    phases = override.get("roadmap") or [
        ("MVP", "2 weeks", "Single-region, core user flows, manual ops", "Multi-region, advanced analytics"),
        ("V1", "3 months", "Production SLO, auth, monitoring, connector integrations", "Custom ML models"),
        ("Scale", "12 months", "Auto-scaling, cost optimization, enterprise compliance", "Edge deployment"),
    ]
    lines = ["| Phase | Timeline | Scope | Out of scope |", "|-------|----------|-------|--------------|"]
    for p in phases:
        lines.append(f"| {p[0]} | {p[1]} | {p[2]} | {p[3]} |")
    lines.append(f"\n**MVP success criteria for {title}:** Core flows demo-ready; p99 within 2× target; on-call runbook draft.")
    return "\n".join(lines)


def _ops(override: dict, title: str, is_genai: bool) -> str:
    slis = override.get("slis") or [
        ("Availability", "successful_requests / total_requests", "99.9% monthly"),
        ("Latency", "p99 response time", "< 8s" if is_genai else "< 300ms"),
    ]
    sli_lines = ["| SLI | Definition | SLO |", "|-----|------------|-----|"]
    for s in slis:
        sli_lines.append(f"| {s[0]} | {s[1]} | {s[2]} |")
    incident = override.get("incident") or (
        "**Scenario:** p99 latency spike 3× baseline.\n\n"
        "1. Check error budget burn in Grafana\n"
        "2. Identify hot shard / tenant via trace tags\n"
        "3. Scale workers or enable degradation mode\n"
        "4. Post-incident: ADR if architecture change needed"
    )
    security = override.get("security_checklist") or [
        "Authentication via org SSO (OIDC)",
        "Authorization at API + data layer",
        "Encryption at rest (AES-256) and in transit (TLS 1.3)",
        "Audit log for admin and sensitive reads",
        "Secrets in vault; no keys in code",
    ]
    if is_genai:
        security.extend([
            "Prompt injection tests in CI",
            "Output guardrails on PII and policy violations",
        ])
    sec = "\n".join(f"- {s}" for s in security)
    return f"""### SLI / SLO

{chr(10).join(sli_lines)}

### Observability

- **Metrics:** Request rate, error rate, latency histograms, queue depth, cache hit ratio
- **Logs:** Structured JSON with `trace_id`, `tenant_id`, `user_id`
- **Traces:** OpenTelemetry across API → workers → DB/cache/LLM

### Deployment

- Blue/green or canary via CI/CD; feature flags for risky changes
- Database migrations backward-compatible; expand-contract pattern

### Incident Runbook

{incident}

### Security Checklist

{sec}
"""


def _supplemental_depth(title: str, kind: str, is_genai: bool, analog: str) -> str:
    """Extra learning sections for practical depth."""
    genai_block = ""
    if is_genai:
        genai_block = """
### OWASP LLM Top 10 Mapping

| Risk | Mitigation in this design |
|------|---------------------------|
| LLM01 Prompt injection | Input sanitization; separate system/user channels |
| LLM06 Sensitive disclosure | ACL on retrieval; redact PII in logs |
| LLM09 Overreliance | Citations, confidence scores, refuse when uncertain |
| LLM10 Model theft | API keys in vault; rate limits per tenant |

"""
    kind_note = "HLD distributed components" if kind == "hld" else "LLD object model and patterns"
    return f"""
---

## Part 11b — Practical Learning Lab

### Hands-on exercises

1. **Whiteboard (15 min):** Draw {kind_note} from memory after reading Parts 1–5.
2. **Tradeoff drill (10 min):** Pick one ADR and argue the rejected alternative for 2 minutes.
3. **Failure mode (10 min):** Pick one failure from Part 7/10; write a 5-step runbook.
4. **Pivot practice (5 min):** Practice the HLD↔LLD pivot script aloud.
5. **Timed mock (45 min):** Use the linked question file without looking at this case study.

### Production readiness checklist

- [ ] SLO defined and dashboarded
- [ ] Load test at 2× expected peak QPS
- [ ] Chaos test: kill one dependency; verify degradation
- [ ] Security review: auth, encryption, audit
- [ ] Runbook linked from on-call playbook
- [ ] Cost model reviewed with FinOps
- [ ] ADRs stored in repo `docs/adr/`

### Industry comparison

| Capability | {analog} (reference) | This design (MVP) | Scale phase |
|------------|----------------------|-------------------|-------------|
| Core flow | Production-grade | MVP scope in Part 9 | Part 9 Scale column |
| Reliability | Multi-region | Single-region 99.9% | Multi-region failover |
| Observability | Full APM + SRE | Metrics + traces + logs | SLO error budgets |
| Security | Enterprise compliance | Checklist in Part 10 | SOC2 / pen test |

{genai_block}
### Senior interviewer rubric

| Signal | Strong | Weak |
|--------|--------|------|
| Requirements | Measurable NFRs stated upfront | Vague "it should scale" |
| Constraints | Names budget, team, timeline | Ignores constraints |
| Tradeoffs | ADR with rejected alternative | Single option only |
| Depth | Failure modes unprompted | Happy path only |
| Communication | Structured 30-min narrative | Jumps to diagram |

"""


def _walkthrough(override: dict, script: str, title: str, kind: str) -> str:
    intro = override.get("walkthrough_intro") or (
        f"This is a 30-minute senior loop for **{title}**. "
        "Spend 5 minutes on context, 10 on HLD, 10 on LLD/boundaries, 5 on ops."
    )
    parts = [f"> {intro}\n"]
    if script:
        for para in re.split(r"\n\s*\n", script.strip()):
            para = para.strip().strip(">").strip()
            if para:
                parts.append(f"> {para}\n")
    extras = override.get("walkthrough_extra") or []
    for e in extras:
        parts.append(f"> {e}\n")
    if kind == "hld":
        parts.append("> If the interviewer pivots to object design, I sketch the service boundaries and DTOs — detailed classes are in the LLD case study.\n")
    elif kind == "lld":
        parts.append("> If the interviewer asks about millions of users, I pivot: same object model, but add Redis cache, message queue, and sharded DB — see HLD case study.\n")
    return "\n".join(parts)


def _lld_boundary(title: str, entities: str) -> str:
    return f"""## Part 8 — Low-Level Design (LLD Boundary)

At the HLD level, defer class-level design to the LLD round. Sketch the **object model** the interviewer may ask for:

### Core object clusters

{entities.strip() if entities else "- **Service facade** — orchestrates use cases\\n- **Domain entities** — hold business state\\n- **Strategy interfaces** — swappable algorithms"}

### Patterns to mention in LLD follow-up

| Pattern | Use |
|---------|-----|
| Strategy | Swappable algorithms (allocation, routing, pricing) |
| Repository | Persistence abstraction behind domain |
| Factory | Complex object creation |
| Observer | Event notifications |

### Pivot script

> "At object level I'd model the core domain entities with a service facade and Strategy for variation points. "
> "For distributed scale, I'd add the cache, queue, and shard layers from the HLD — happy to go deeper on either."
"""


def _hld_boundary(title: str, scale: str) -> str:
    return f"""## Part 7 — High-Level Design (Scale Projection / HLD Boundary)

The LLD object model is correct for **single-process / in-memory MVP**. When the interviewer pivots to scale:

### Scale triggers

| Signal | HLD addition |
|--------|--------------|
| Multiple instances | Stateless API behind load balancer |
| Shared state | Redis / distributed cache |
| Write contention | Message queue + async workers |
| Global users | Multi-region read replicas; CDN |

{scale.strip() if scale else ""}

### Distributed sketch

```
Client → CDN → LB → API (stateless) → Cache → DB
                              ↓
                         Message queue → Workers
```

### Pivot script

> "My object model stays — ParkingLotService, Strategy, entities. "
> "At scale I'd add a central occupancy registry in Redis, event bus for cross-garage sync, and shard by buildingId."
"""


def build_case_study(
    *,
    cs_prefix: str,
    num: int,
    slug: str,
    track_label: str,
    kind: str,
    question_path: Path,
    out_path: Path,
    pair: dict | None,
    override: dict,
) -> str:
    text = _read(question_path)
    meta = _extract_meta(text)
    title = meta.get("title", slug)
    companies = meta.get("companies", "Various")
    difficulty = meta.get("difficulty", "Medium")
    cs_id = _cs_id(cs_prefix, num)
    is_genai = "genai" in track_label.lower() or "gen ai" in meta.get("track", "").lower()

    problem = _extract_section(text, "Problem Statement", "1. Problem Statement")
    functional = _extract_section(text, "Functional Requirements", "Functional & Non-Functional Requirements", "3. Functional")
    nfr = _extract_section(text, "Non-Functional Requirements")
    if not nfr and "Non-Functional" in functional:
        parts = re.split(r"\*\*Non-Functional", functional, flags=re.I)
        functional = parts[0]
        nfr = parts[1] if len(parts) > 1 else ""
    capacity = _extract_section(text, "Capacity Estimation", "6. Capacity")
    hld_diag = _extract_section(text, "HLD Diagram", "5. HLD Diagram")
    components = _extract_section(text, "Component Choices", "7. Component")
    deep = _extract_section(text, "Deep Dive", "Deep Dive Topics", "8. Deep Dive")
    tradeoffs = _extract_section(text, "Tradeoffs", "10. Tradeoffs")
    failures = _extract_section(text, "Failure Modes", "11. Failure")
    script = _extract_section(text, "Interview Answer Script", "12. Interview Answer Script")
    entities = _extract_section(text, "Core Entities", "4. Core Entities")
    class_diag = _extract_section(text, "Class Diagram", "5. Class Diagram")
    patterns = _extract_section(text, "Design Patterns", "7. Design Patterns")
    sequences = _extract_section(text, "Sequence Diagrams", "8. Sequence")
    concurrency = _extract_section(text, "Concurrency", "11. Concurrency")
    api = _extract_section(text, "Public API", "6. Public API")
    clarify = _extract_section(text, "Clarifying Questions", "2. Clarifying Questions")
    related = _extract_section(text, "Related", "14. Related")

    analog = override.get("industry_analog", "Industry-leading products in this domain (see industry-standards-reference.md)")
    biz = override.get("business_context") or (
        f"**Industry analog:** {analog}\n\n"
        f"This case study examines **{title}** — a system type commonly built at {companies.split(',')[0].strip()} "
        f"and similar organizations. {problem.strip() if problem else ''}\n\n"
        f"**Why now:** Teams with 3–5 YOE full-stack backgrounds are expected to connect product requirements "
        f"to concrete architecture — especially with GenAI/LLM components where cost, safety, and correctness trade off sharply.\n\n"
        f"**Success definition:** Meet NFR targets, ship MVP within constraints, and articulate tradeoffs using ADRs."
    )

    q_rel = _rel(out_path.parent, question_path)
    pair_link = ""
    if pair:
        pair_path = ROOT / "paired" / pair_doc_name(pair)
        pair_link = f"**Paired case study:** [{pair_doc_name(pair)}]({_rel(out_path.parent, pair_path)})\n"

    java_link = ""
    if kind == "lld":
        impl = LLD_ROOT / "09-code-implementations" / "java"
        for sub in ("classic", "patterns", "concurrency", "genai"):
            if (impl / sub / slug.replace("-", "_").split("-")[0]).exists():
                break
        # try slug-based path
        for p in impl.rglob(slug.split("-")[0]):
            if p.is_dir():
                java_link = f"**Java implementation:** [{slug}]({_rel(out_path.parent, p)})\n"
                break

    doc = f"""# {title} — Case Study

**Case Study ID:** {cs_id}
**Track:** {track_label}
**Companies:** {companies}
**Difficulty:** {difficulty}
**Related question:** [{question_path.name}]({q_rel})
{pair_link}{java_link}
---

## Part 1 — Business Context

{biz}

---

## Part 2 — Stakeholders & Personas

{_stakeholders(override, title)}

---

## Part 3 — Requirements

### Functional Requirements (MoSCoW)

{_moscow_fr(override, functional, problem or title)}

### Non-Functional Requirements

{_nfr_table(override, nfr, is_genai)}

### Clarifying Questions (Discovery Phase)

{clarify.strip() if clarify else "| # | Question | Expected answer |\\n|---|----------|-----------------|\\n| 1 | Scope? | MVP vs full platform |"}

---

## Part 4 — Constraints

{_constraints(override)}

---

## Part 5 — Tradeoffs & Architecture Decision Records

{_adrs(override, tradeoffs, title)}

---

## Part 6 — Capacity & Cost Estimation

{capacity.strip() if capacity else override.get('capacity', '**Scale projection:** Start with single-region MVP; model QPS and storage at 10× current load before Scale phase.')}

### Cost ballpark (V1)

{override.get('cost', '- Compute: $5–15K/mo\\n- Managed DB/cache: $3–8K/mo\\n- LLM API (if applicable): usage-based; budget caps per tenant')}

---

"""

    if kind == "hld":
        doc += f"""## Part 7 — High-Level Design

### Problem recap

{problem.strip() if problem else title}

### Architecture

{hld_diag.strip() if hld_diag else 'See related question file for diagrams.'}

### Component choices

{components.strip() if components else '| Component | Choice | Alternative |\\n|-----------|--------|-------------|\\n| API | Stateless REST/gRPC | GraphQL |'}

### Deep dive topics

{deep.strip() if deep else 'Refer to linked question file for deep dives.'}

### Failure modes

{failures.strip() if failures else '| Failure | Mitigation |\\n|---------|------------|\\n| Dependency outage | Graceful degradation + circuit breaker |'}

---

{_lld_boundary(title, entities)}

"""
    else:
        doc += f"""{_hld_boundary(title, override.get('scale_projection', ''))}

---

## Part 8 — Low-Level Design

### Problem recap

{problem.strip() if problem else title}

### Core entities

{entities.strip() if entities else 'See class diagram below.'}

### Class diagram

{class_diag.strip() if class_diag else 'See related question file.'}

### Public API

{api.strip() if api else 'See related question file for key methods.'}

### Design patterns & SOLID

{patterns.strip() if patterns else '| Pattern | Application |\\n|---------|-------------|\\n| Strategy | Swappable behavior |'}

### Sequence diagrams

{sequences.strip() if sequences else 'Happy path + failure path in related question file.'}

### Concurrency & edge cases

{concurrency.strip() if concurrency else 'Identify shared mutable state; lock at finest safe granularity.'}

---

"""

    doc += f"""## Part 9 — Implementation Roadmap

{_roadmap(override, title)}

---

## Part 10 — Operations

{_ops(override, title, is_genai)}

---

## Part 11 — Interview Walkthrough (30 min)

{_walkthrough(override, script, title, kind)}

{_supplemental_depth(title, kind, is_genai, override.get('industry_analog', title))}

---

## Part 12 — Related Links

- **Question file:** [{question_path.name}]({q_rel})
"""
    if pair:
        doc += f"- **End-to-end pair:** [{pair_doc_name(pair)}]({_rel(out_path.parent, ROOT / 'paired' / pair_doc_name(pair))})\n"
    doc += f"""- **Template:** [case-study-template.md]({_rel(out_path.parent, ROOT / '00-framework/case-study-template.md')})
- **Industry standards:** [industry-standards-reference.md]({_rel(out_path.parent, ROOT / '00-framework/industry-standards-reference.md')})

{related.strip() if related else ''}
"""
    return doc


def discover_hld() -> list[dict]:
    items = []
    for track_key, (out_sub, q_sub, prefix, label) in HLD_TRACKS.items():
        qdir = HLD_ROOT / q_sub
        for f in sorted(qdir.glob("Q*.md")):
            m = re.match(r"Q(\d+)-(.+)\.md", f.name)
            if not m:
                continue
            num = int(m.group(1))
            slug = m.group(2)
            items.append({
                "kind": "hld", "track_key": track_key, "num": num, "slug": slug,
                "prefix": prefix, "label": label, "question": f, "out_sub": out_sub,
            })
    return items


def discover_lld() -> list[dict]:
    items = []
    for track_key, (out_sub, q_sub, prefix, label) in LLD_TRACKS.items():
        qdir = LLD_ROOT / q_sub
        for f in sorted(qdir.glob("Q*.md")):
            m = re.match(r"Q(\d+)-(.+)\.md", f.name)
            if not m:
                continue
            num = int(m.group(1))
            slug = m.group(2)
            items.append({
                "kind": "lld", "track_key": track_key, "num": num, "slug": slug,
                "prefix": prefix, "label": label, "question": f, "out_sub": out_sub,
            })
    return items


def out_file(item: dict) -> Path:
    cs = _cs_id(item["prefix"], item["num"])
    return ROOT / item["out_sub"] / f"{cs}-{item['slug']}.md"


def build_paired(pair: dict) -> str:
    hld_track = pair["hld"]["track"]
    lld_track = pair["lld"]["track"]
    hld_item = next(x for x in discover_hld() if x["track_key"] == hld_track and x["num"] == pair["hld"]["num"])
    lld_item = next(x for x in discover_lld() if x["track_key"] == lld_track and x["num"] == pair["lld"]["num"])
    hld_cs = build_case_study(
        cs_prefix=hld_item["prefix"], num=hld_item["num"], slug=hld_item["slug"],
        track_label=f"Paired (HLD + LLD): {pair['title']}", kind="hld",
        question_path=hld_item["question"], out_path=ROOT / "paired" / pair_doc_name(pair),
        pair=pair, override=get_override(hld_item["slug"], "hld", pair["title"]),
    )
    lld_cs = build_case_study(
        cs_prefix=lld_item["prefix"], num=lld_item["num"], slug=lld_item["slug"],
        track_label=f"Paired (HLD + LLD): {pair['title']}", kind="lld",
        question_path=lld_item["question"], out_path=ROOT / "paired" / pair_doc_name(pair),
        pair=pair, override=get_override(lld_item["slug"], "lld", pair["title"]),
    )
    # Merge: header + HLD parts 1-7 from hld + LLD part 8 from lld + shared 9-12
    hld_parts = hld_cs.split("## Part 8 — Low-Level Design (LLD Boundary)")[0]
    lld_part8 = lld_cs.split("## Part 8 — Low-Level Design")[1].split("## Part 9")[0]
    tail = lld_cs.split("## Part 9 — Implementation Roadmap")[1]
    header = f"""# {pair['title']} — End-to-End Case Study

**Case Study ID:** CS-PAIR-{pair['id']}
**Track:** Paired HLD + LLD
**HLD question:** [{hld_item['question'].name}](../{HLD_TRACKS[hld_track][0].replace('hld/', 'hld/')}/../../System Design - High Level Design/{HLD_TRACKS[hld_track][1]}/{hld_item['question'].name})
**LLD question:** [{lld_item['question'].name}](../System Design - Low Level Design/{LLD_TRACKS[lld_track][1]}/{lld_item['question'].name})

---

"""
    # Fix header links properly
    hld_rel = f"../{HLD_TRACKS[hld_track][0]}/{_cs_id(hld_item['prefix'], hld_item['num'])}-{hld_item['slug']}.md"
    lld_rel = f"../{LLD_TRACKS[lld_track][0]}/{_cs_id(lld_item['prefix'], lld_item['num'])}-{lld_item['slug']}.md"
    header = f"""# {pair['title']} — End-to-End Case Study

**Case Study ID:** CS-PAIR-{pair['id']}
**Track:** Paired HLD + LLD
**HLD case study:** [{_cs_id(hld_item['prefix'], hld_item['num'])}]({hld_rel})
**LLD case study:** [{_cs_id(lld_item['prefix'], lld_item['num'])}]({lld_rel})
**HLD question:** [{hld_item['question'].name}](../../System Design - High Level Design/{HLD_TRACKS[hld_track][1]}/{hld_item['question'].name})
**LLD question:** [{lld_item['question'].name}](../../System Design - Low Level Design/{LLD_TRACKS[lld_track][1]}/{lld_item['question'].name})

> Read this document for the **full stack narrative**. Use individual HLD/LLD case studies for depth on one round type.

---

"""
    # Use HLD from part 1 through 7
    body = hld_parts.split("# ", 1)[1] if "# " in hld_parts else hld_parts
    body = "# " + body  # restore
    body = re.sub(r"^# .+ — Case Study\n\n\*\*Case Study ID:\*\*.+?\n---\n\n", "", body, count=1, flags=re.S)
    merged = header + body + "## Part 8 — Low-Level Design (Full)\n\n" + lld_part8 + "## Part 9 — Implementation Roadmap" + tail
    return merged


def write_index(all_items: list[tuple[Path, dict]]) -> None:
    lines = [
        "# Case Studies Index",
        "",
        "Auto-generated master index. Regenerate with `python _generate_case_studies.py --index`.",
        "",
        "| ID | Title | Track | Difficulty | Pair | File |",
        "|----|-------|-------|------------|------|------|",
    ]
    for path, item in sorted(all_items, key=lambda x: str(x[0])):
        text = _read(item["question"])
        meta = _extract_meta(text)
        cs_name = path.name
        pair = ""
        if item["kind"] == "hld":
            p = pair_by_hld(item["track_key"], item["num"])
        else:
            p = pair_by_lld(item["track_key"], item["num"])
        if p:
            pair = f"[PAIR-{p['id']}](paired/{pair_doc_name(p)})"
        rel = path.relative_to(ROOT).as_posix()
        lines.append(
            f"| {_cs_id(item['prefix'], item['num'])} | {meta.get('title', item['slug'])} | "
            f"{item['label']} | {meta.get('difficulty', 'Medium')} | {pair} | [{cs_name}]({rel}) |"
        )
    for pair in PAIRED_TOPICS:
        rel = f"paired/{pair_doc_name(pair)}"
        lines.append(
            f"| CS-PAIR-{pair['id']} | {pair['title']} | Paired | — | — | [{pair_doc_name(pair)}]({rel}) |"
        )
    (ROOT / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", action="store_true", help="Regenerate index only")
    ap.add_argument("--force", action="store_true", help="Overwrite gold-standard files")
    ap.add_argument("--paired-only", action="store_true")
    args = ap.parse_args()

    all_written: list[tuple[Path, dict]] = []

    if not args.index:
        for sub in ["hld/genai", "hld/classic", "lld/classic-ood", "lld/design-patterns", "lld/concurrency", "lld/genai", "paired"]:
            (ROOT / sub).mkdir(parents=True, exist_ok=True)

        for item in discover_hld() + discover_lld():
            out = out_file(item)
            rel = out.relative_to(ROOT).as_posix()
            if rel in GOLD_STANDARD_SKIP and not args.force:
                all_written.append((out, item))
                continue
            pair = pair_by_hld(item["track_key"], item["num"]) if item["kind"] == "hld" else pair_by_lld(item["track_key"], item["num"])
            override = get_override(item["slug"], item["kind"], _extract_meta(_read(item["question"])).get("title", item["slug"]))
            md = build_case_study(
                cs_prefix=item["prefix"], num=item["num"], slug=item["slug"],
                track_label=item["label"], kind=item["kind"],
                question_path=item["question"], out_path=out,
                pair=pair, override=override,
            )
            out.write_text(md, encoding="utf-8")
            all_written.append((out, item))
            print(f"Wrote {out.relative_to(ROOT)}")

        if not args.paired_only:
            for pair in PAIRED_TOPICS:
                pname = f"paired/{pair_doc_name(pair)}"
                if pname in GOLD_STANDARD_SKIP and not args.force:
                    continue
                pout = ROOT / "paired" / pair_doc_name(pair)
                pout.write_text(build_paired(pair), encoding="utf-8")
                print(f"Wrote paired/{pair_doc_name(pair)}")

    # rebuild index from disk
    index_items: list[tuple[Path, dict]] = []
    for item in discover_hld() + discover_lld():
        index_items.append((out_file(item), item))
    write_index(index_items)
    print("Wrote index.md")


if __name__ == "__main__":
    main()

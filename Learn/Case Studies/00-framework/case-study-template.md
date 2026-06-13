# Case Study Template (12 Parts)

Use this template for every case study in the library. Target length: **800–1200 lines** for gold-standard topics; generated topics follow the same section order with proportional depth.

---

## Part 0 — Metadata

```markdown
# {Title}

**Case Study ID:** CS-{TRACK}-{ID}
**Track:** {HLD GenAI | HLD Classic | LLD OOD | LLD Patterns | LLD Concurrency | LLD GenAI | Paired}
**Companies:** {comma-separated}
**Difficulty:** {Easy | Medium | Hard}
**Related question:** [Q{nn} …](path)
**Paired case study:** [CS-PAIR-xx …](path) *(if applicable)*
**Java implementation:** [path](path) *(LLD only)*
```

---

## Part 1 — Business Context

- **Industry analog:** Name a real product (Bitly, Glean, Stripe, Uber, Notion AI, etc.)
- **Problem in product terms:** What business pain does this solve?
- **Why now:** Market or technical trigger (GenAI wave, scale event, compliance mandate)
- **Success definition:** 2–3 measurable outcomes (DAU, revenue, SLA, cost reduction)

---

## Part 2 — Stakeholders & Personas

| Persona | Goals | Pain points | Success metric |
|---------|-------|-------------|----------------|
| End user | … | … | … |
| Admin / operator | … | … | … |
| SRE / platform | … | … | … |
| Compliance / security | … | … | … |

---

## Part 3 — Requirements

### Functional Requirements (MoSCoW)

| Priority | Requirement | Acceptance criteria |
|----------|-------------|---------------------|
| Must | … | … |
| Should | … | … |
| Could | … | … |
| Won't (MVP) | … | … |

### Non-Functional Requirements

| Attribute | Target | Measurement |
|-----------|--------|-------------|
| Latency | p99 < X ms/s | APM |
| Availability | 99.X% | Error budget |
| Throughput | X QPS | Load test |
| Security | … | Audit |
| Cost | … | FinOps dashboard |
| Compliance | SOC2 / GDPR / HIPAA | Certification |

---

## Part 4 — Constraints

| Constraint | Detail | Impact on design |
|------------|--------|------------------|
| Budget | … | … |
| Team size | … | … |
| Timeline | MVP in N weeks | … |
| Tech lock-in | … | … |
| Regulatory | … | … |
| Build vs buy | … | … |

---

## Part 5 — Tradeoffs & ADRs

Use [ADR format](industry-standards-reference.md#architecture-decision-records):

### ADR-001: {Title}

- **Status:** Accepted
- **Context:** …
- **Decision:** …
- **Consequences:** Positive / negative
- **Alternatives rejected:** …

*(Repeat for 3–5 ADRs)*

### Tradeoffs Summary Table

| Decision | Option A | Option B | Pick | Rationale |
|----------|----------|----------|------|-----------|

---

## Part 6 — Capacity & Cost Estimation

- Back-of-envelope math (QPS, storage, bandwidth)
- Infra cost ballpark (monthly at scale)
- **LLD topics:** "Scale projection" — what happens at 10M users

---

## Part 7 — High-Level Design

- ASCII architecture diagram
- Mermaid flowchart
- Component choices table (Choice | Why | Alternative)
- Read path + write path (where applicable)
- Failure modes table

**HLD-only:** Full HLD here.

**LLD-only:** Brief "Scale projection / HLD boundary" sketch.

---

## Part 8 — Low-Level Design

- Core entities table
- Class diagram (ASCII + Mermaid)
- Key APIs (Java snippets for LLD)
- Design patterns + SOLID mapping
- Sequence diagrams (happy + failure paths)
- Concurrency notes

**HLD-only:** "LLD Boundary" — object model sketch, defer to LLD round.

**LLD-only:** Full LLD here.

**Paired:** Full both HLD (Part 7) and LLD (Part 8) in one document.

---

## Part 9 — Implementation Roadmap

| Phase | Timeline | Scope | Out of scope |
|-------|----------|-------|--------------|
| MVP | 2 weeks | … | … |
| V1 | 3 months | … | … |
| Scale | 12 months | … | … |

---

## Part 10 — Operations

- **SLI/SLO:** Define 2–3 SLIs with SLO targets
- **Observability:** Metrics, logs, traces
- **Deployment:** CI/CD, rollback strategy
- **Incident scenario:** One runbook walkthrough
- **Security checklist:** Auth, encryption, audit

---

## Part 11 — Interview Walkthrough (30 min)

Blockquoted spoken narrative tying:

1. Business context → requirements (5 min)
2. Constraints → ADRs → tradeoffs (5 min)
3. HLD walkthrough (10 min)
4. LLD / pivot to objects (5 min)
5. Ops, failure modes, extensions (5 min)

---

## Part 12 — Related Links

- Original HLD/LLD question file(s)
- Paired case study (if any)
- Core concept docs
- Java implementation (LLD)
- Industry standards applied

---

## Quality Checklist

- [ ] Real industry analog named
- [ ] FR/NFR measurable
- [ ] ≥3 explicit constraints
- [ ] ≥3 ADRs with rejected alternatives
- [ ] Read + write paths (HLD)
- [ ] Patterns + SOLID (LLD)
- [ ] 3-phase roadmap
- [ ] SLI/SLO + incident scenario
- [ ] Links to question files and pair doc

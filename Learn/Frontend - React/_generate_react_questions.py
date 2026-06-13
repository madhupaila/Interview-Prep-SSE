#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate React interview question markdown files."""

from __future__ import annotations

from pathlib import Path

from _react_question_data import CLASSIC_QUESTIONS, GENAI_QUESTIONS

ROOT = Path(__file__).resolve().parent


def _options_table(options: list[tuple[str, str]]) -> str:
    lines = ["| Option | Issue / note |", "|--------|--------------|"]
    for a, b in options:
        lines.append(f"| {a} | {b} |")
    return "\n".join(lines)


def _tradeoffs_table(tradeoffs: list[tuple[str, str, str, str]]) -> str:
    lines = ["| Decision | A | B | Pick |", "|----------|---|---|------|"]
    for row in tradeoffs:
        lines.append(f"| {row[0]} | {row[1]} | {row[2]} | {row[3]} |")
    return "\n".join(lines)


def _followups(items: list[str]) -> str:
    return "\n".join(f"{i+1}. {q}" for i, q in enumerate(items))


def render_question(
    *,
    track: str,
    prefix: str,
    num: int,
    slug: str,
    title: str,
    companies: str,
    difficulty: str,
    memory_hook: str,
    concept: str,
    options: list,
    pick: str,
    script_paras: list,
    code_hint: str,
    tradeoffs: list,
    followups: list,
    related: str,
) -> str:
    qid = f"{prefix}{num:02d}"
    if track == "classic":
        qpath = f"../../03-classic-react/questions/Q{num:02d}-{slug}.md"
        concept_link = f"../../01-core-concepts/{related}"
    else:
        qpath = f"questions/Q{num:02d}-{slug}.md"
        concept_link = f"../{related}" if not related.startswith("0") else f"../{related}"

    script = "\n\n".join(f"> {p}" for p in script_paras)

    return f"""# {title}

**Track:** {track.replace('_', ' ').title()} React
**Companies:** {companies}
**Difficulty:** {difficulty}
**Case Study ID:** R-{prefix}-{num:02d}

---

## Memory Hook

> **{memory_hook}**

---

## What Interviewers Test

{concept}

---

## Options / Approaches

{_options_table(options)}

---

## Senior Pick

**Use:** {pick}

---

## Clarifying Questions (If Build / System Question)

| # | Question | Why it matters |
|---|----------|----------------|
| 1 | Mobile vs desktop? | Layout, virtual keyboard |
| 2 | SSR required? | Next.js vs SPA |
| 3 | Real-time / streaming? | SSE vs polling |
| 4 | Accessibility level? | WCAG, live regions |
| 5 | Error / offline behavior? | Degraded UX |

---

## Interview Answer Script (Speak Aloud)

{script}

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// {code_hint}
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

{_tradeoffs_table(tradeoffs)}

---

## Follow-Up Questions

{_followups(followups)}

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | {concept.split('—')[0].strip() if '—' in concept else concept[:50]} |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | {pick} |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [{related}]({concept_link})
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)
"""


def main() -> None:
    classic_dir = ROOT / "03-classic-react" / "questions"
    genai_dir = ROOT / "02-genai-llm-react" / "questions"
    classic_dir.mkdir(parents=True, exist_ok=True)
    genai_dir.mkdir(parents=True, exist_ok=True)

    for row in CLASSIC_QUESTIONS:
        num, slug, title, companies, diff, hook, concept, opts, pick, script, code, to, fu, rel = row
        md = render_question(
            track="classic", prefix="C", num=num, slug=slug, title=title,
            companies=companies, difficulty=diff, memory_hook=hook, concept=concept,
            options=opts, pick=pick, script_paras=script, code_hint=code,
            tradeoffs=to, followups=fu, related=rel,
        )
        path = classic_dir / f"Q{num:02d}-{slug}.md"
        path.write_text(md, encoding="utf-8")
        print(f"Wrote {path.relative_to(ROOT)}")

    for row in GENAI_QUESTIONS:
        num, slug, title, companies, diff, hook, concept, opts, pick, script, code, to, fu, rel = row
        md = render_question(
            track="genai_llm", prefix="G", num=num, slug=slug, title=title,
            companies=companies, difficulty=diff, memory_hook=hook, concept=concept,
            options=opts, pick=pick, script_paras=script, code_hint=code,
            tradeoffs=to, followups=fu, related=rel,
        )
        path = genai_dir / f"Q{num:02d}-{slug}.md"
        path.write_text(md, encoding="utf-8")
        print(f"Wrote {path.relative_to(ROOT)}")

    print(f"Generated {len(CLASSIC_QUESTIONS)} classic + {len(GENAI_QUESTIONS)} genai questions")


if __name__ == "__main__":
    main()

# RAG UI with Citations and Source Panel

**Track:** Genai Llm React
**Companies:** Perplexity, Glean, Harvey
**Difficulty:** Hard
**Case Study ID:** R-G-04

---

## Memory Hook

> **Citation chips + drawer with snippet**

---

## What Interviewers Test

Trust UX for enterprise RAG

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Answer only | No trust |
| Inline citations + panel | Enterprise |
| Footnotes only | Academic |

---

## Senior Pick

**Use:** CitationChip + SourceDrawer

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

> Message metadata citations array.

> Click [1] opens drawer.

> Empty sources → no answer state.

> Highlight matching snippet.

> Loading retrieval indicator.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// AssistantMessage citations prop
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Empty retrieval | Hallucinate | Refuse UI | Refuse |

---

## Follow-Up Questions

1. PDF page highlight?
2. Citation hover preview?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Trust UX for enterprise RAG |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | CitationChip + SourceDrawer |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [rag-ui-patterns.md](../rag-ui-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

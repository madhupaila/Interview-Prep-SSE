# Side-by-Side Model Comparison UI

**Track:** Genai Llm React
**Companies:** OpenAI Playground, Anthropic Workbench
**Difficulty:** Hard
**Case Study ID:** R-G-14

---

## Memory Hook

> **Same prompt → two parallel streams**

---

## What Interviewers Test

Eval/compare UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Sequential compare | Slow |
| Parallel streams | Fast |
| Single panel | No compare |

---

## Senior Pick

**Use:** DualPane stream hooks

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

> Two AbortControllers.

> Sync scroll optional.

> Show latency per model.

> Cost estimate each.

> Export comparison.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// CompareView modelA modelB
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Stream | Sequential | Parallel | Parallel |

---

## Follow-Up Questions

1. Sync scroll?
2. Blind compare mode?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Eval/compare UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | DualPane stream hooks |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-genai-react.md](../memory-map-genai-react.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

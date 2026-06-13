# Token Budget & Context Window Warning

**Track:** Genai Llm React
**Companies:** OpenAI, Anthropic, Cursor
**Difficulty:** Hard
**Case Study ID:** R-G-08

---

## Memory Hook

> **Progress bar tokens used; warn truncate**

---

## What Interviewers Test

Context limit UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Silent truncate | Confusing |
| Visible token meter | Transparent |
| Hard block send | Strict |

---

## Senior Pick

**Use:** TokenMeter + warn at 80%

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

> Estimate tokens client-side approx.

> Show remaining context.

> Suggest start new thread.

> Summarize old messages action.

> API returns context_length_exceeded.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// TokenBudgetBar used max
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Over limit | Fail mysteriously | Warn + actions | Warn |

---

## Follow-Up Questions

1. Accurate token count API?
2. Auto-summarize thread?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Context limit UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | TokenMeter + warn at 80% |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-genai-react.md](../memory-map-genai-react.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

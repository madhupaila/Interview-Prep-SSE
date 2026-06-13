# Model Selector with Cost/Latency Hints

**Track:** Genai Llm React
**Companies:** OpenAI, Azure OpenAI, Groq
**Difficulty:** Medium
**Case Study ID:** R-G-07

---

## Memory Hook

> **Dropdown models + tooltip cost/latency**

---

## What Interviewers Test

Model routing UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Hidden model | No user control |
| Selector with hints | Transparent |
| Raw model string | Confusing |

---

## Senior Pick

**Use:** ModelPicker component + settings persist

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

> models config from API.

> Show $/1M tokens estimate.

> Latency tier badge.

> Disable unavailable models.

> Persist choice localStorage.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// ModelSelect options hint
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Default | Most expensive | Balanced default | Balanced |

---

## Follow-Up Questions

1. Org policy lock model?
2. A/B test models?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Model routing UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | ModelPicker component + settings persist |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-genai-react.md](../memory-map-genai-react.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

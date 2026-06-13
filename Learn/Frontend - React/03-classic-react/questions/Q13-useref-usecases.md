# useRef Use Cases

**Track:** Classic React
**Companies:** Google, Amazon, Unity
**Difficulty:** Easy
**Case Study ID:** R-C-13

---

## Memory Hook

> **Mutable box; DOM access; no re-render on .current change**

---

## What Interviewers Test

Refs vs state

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Store UI value in ref | Wrong for render |
| DOM focus | Correct |
| Previous value pattern | Correct |

---

## Senior Pick

**Use:** DOM, timers, mutable latest value without render

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

> ref.current change doesn't trigger re-render.

> Forward ref to child input.

> Store AbortController, interval id.

> Don't read ref during render for UI — use state.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Focus input on modal open
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Previous props | useState | useRef | useRef |

---

## Follow-Up Questions

1. callback refs?
2. ref object vs function ref?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Refs vs state |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | DOM, timers, mutable latest value without render |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [hooks-deep-dive.md](../../01-core-concepts/hooks-deep-dive.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

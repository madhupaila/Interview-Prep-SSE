# useEffect Dependencies & Stale Closures

**Track:** Classic React
**Companies:** Meta, Stripe, Coinbase
**Difficulty:** Hard
**Case Study ID:** R-C-10

---

## Memory Hook

> **Effect closes over render — deps must be exhaustive**

---

## What Interviewers Test

Effect correctness

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Empty deps always | Stale bug |
| Exhaustive deps | Correct |
| Disable eslint | Bad |

---

## Senior Pick

**Use:** Exhaustive deps + cleanup + abort

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

> Missing dep → stale count in interval.

> Functional updates reduce dep needs for setState.

> AbortController in cleanup for fetch.

> Don't lie to eslint-deps — fix root cause.

> Derived state doesn't belong in effect.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Interval logging stale count fix
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Fetch | No abort | AbortController | Abort |

---

## Follow-Up Questions

1. useEffectEvent?
2. When is empty deps OK?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Effect correctness |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Exhaustive deps + cleanup + abort |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [hooks-deep-dive.md](../../01-core-concepts/hooks-deep-dive.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

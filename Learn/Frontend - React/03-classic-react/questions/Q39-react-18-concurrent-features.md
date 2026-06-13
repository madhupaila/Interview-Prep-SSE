# React 18 Concurrent Features

**Track:** Classic React
**Companies:** Meta, Vercel, Shopify
**Difficulty:** Hard
**Case Study ID:** R-C-39

---

## Memory Hook

> **Transitions defer non-urgent updates**

---

## What Interviewers Test

Concurrent UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Sync setState filter | Input lag |
| startTransition | Smooth |
| debounce only | Partial |

---

## Senior Pick

**Use:** startTransition + useDeferredValue

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

> Mark heavy filter as transition.

> UI stays responsive.

> useDeferredValue for deferred display.

> Suspense for lazy/data.

> Automatic batching in 18.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Search filter startTransition
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Priority | All sync | Transition | Transition |

---

## Follow-Up Questions

1. useOptimistic React 19?
2. Suspense boundaries nesting?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Concurrent UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | startTransition + useDeferredValue |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [rendering-reconciliation.md](../../01-core-concepts/rendering-reconciliation.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

# Context API Performance Problem

**Track:** Classic React
**Companies:** Meta, Pinterest, Slack
**Difficulty:** Hard
**Case Study ID:** R-C-07

---

## Memory Hook

> **All consumers re-render on any value change**

---

## What Interviewers Test

Context scaling and mitigation

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| One giant context | Bad |
| Split contexts | Better |
| Zustand selector | High churn |

---

## Senior Pick

**Use:** Split by update frequency + memo value

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

> New object in Provider value → all consumers re-render.

> Split Theme vs Session contexts.

> Memoize value tuple.

> For high frequency use external store with selectors.

> Don't put entire app state in Context.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// ThemeContext vs CartContext split
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Store | Context only | Zustand selectors | Selectors at scale |

---

## Follow-Up Questions

1. context-selector pattern?
2. Pass dispatch-only context?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Context scaling and mitigation |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Split by update frequency + memo value |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [state-management.md](../../01-core-concepts/state-management.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

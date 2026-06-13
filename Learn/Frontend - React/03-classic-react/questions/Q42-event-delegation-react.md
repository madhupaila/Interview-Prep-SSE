# Synthetic Events and Delegation

**Track:** Classic React
**Companies:** Meta, Google, Microsoft
**Difficulty:** Medium
**Case Study ID:** R-C-42

---

## Memory Hook

> **React pools events; attach at root in legacy**

---

## What Interviewers Test

Event system

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Native addEventListener each node | Verbose |
| React onClick | Synthetic wrapper |
| Delegation pattern | List performance |

---

## Senior Pick

**Use:** React 17+ delegates to root on container

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

> e.stopPropagation still works.

> passive events for scroll perf.

> onClick on parent for dynamic child lists — careful with target check.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// List item click delegation
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Handler | Inline lambda every row | Stable callback | Stable |

---

## Follow-Up Questions

1. React 17 event delegation change?
2. preventDefault passive?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Event system |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | React 17+ delegates to root on container |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

# Generic React Components in TypeScript

**Track:** Classic React
**Companies:** Shopify, GitHub, Microsoft
**Difficulty:** Hard
**Case Study ID:** R-C-32

---

## Memory Hook

> **Props<T> with constraints; forwardRef generics**

---

## What Interviewers Test

Reusable typed components

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| props: any | Unsafe |
| Generic <T> | Reusable DataTable<T> |
| Duplicate per type | Verbose |

---

## Senior Pick

**Use:** Generic with extends constraint

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

> interface DataTableProps<T extends {id:string}>.

> forwardRef generic syntax tricky — use typed wrapper.

> ComponentPropsWithoutRef utility.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// DataTable<T> column defs
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Typing | any | Generic T | Generic |

---

## Follow-Up Questions

1. Generic custom hooks?
2. Type inference from props?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Reusable typed components |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Generic with extends constraint |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

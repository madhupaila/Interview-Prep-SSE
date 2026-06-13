# Build a Data Table with Sort/Filter

**Track:** Classic React
**Companies:** Bloomberg, Stripe Dashboard, AWS
**Difficulty:** Hard
**Case Study ID:** R-C-56

---

## Memory Hook

> **TanStack Table headless + virtualized rows**

---

## What Interviewers Test

Complex table UI

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| HTML table only | No scale |
| TanStack Table | Headless logic |
| AG Grid | Heavy full solution |

---

## Senior Pick

**Use:** TanStack Table + Virtual

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

> Column defs with accessorFn.

> Client vs server sort/filter.

> Virtualize tbody.

> Sticky header CSS.

> Selection state lifted.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// DataTable sort filter virtual
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Logic | Roll own sort | TanStack Table | TanStack Table |

---

## Follow-Up Questions

1. Server-side pagination?
2. Column resize persist?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Complex table UI |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | TanStack Table + Virtual |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [performance-optimization.md](../../01-core-concepts/performance-optimization.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

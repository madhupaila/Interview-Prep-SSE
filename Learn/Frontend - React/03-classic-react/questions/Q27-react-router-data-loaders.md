# React Router Data Loading

**Track:** Classic React
**Companies:** Remix, Shopify, Netflix
**Difficulty:** Medium
**Case Study ID:** R-C-27

---

## Memory Hook

> **Loaders defer data before render; errorElement**

---

## What Interviewers Test

Routing + data

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| fetch in useEffect on mount | Waterfall |
| Route loader | Parallel prefetch |
| Next.js server | Framework specific |

---

## Senior Pick

**Use:** Loader + defer + Await for React Router 6.4+

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

> loader runs before route renders.

> defer for non-critical data.

> errorElement for route errors.

> useLoaderData typed return.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Route loader user profile
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Framework | CRA only | Router/Next loaders | Loader pattern |

---

## Follow-Up Questions

1. Loader vs TanStack Query?
2. Client vs server loader?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Routing + data |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Loader + defer + Await for React Router 6.4+ |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

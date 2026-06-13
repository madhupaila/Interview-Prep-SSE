# React.lazy and Suspense

**Track:** Classic React
**Companies:** Google, YouTube, Netflix
**Difficulty:** Medium
**Case Study ID:** R-C-19

---

## Memory Hook

> **Code split routes; Suspense shows fallback**

---

## What Interviewers Test

Lazy loading

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Static import all | Large bundle |
| React.lazy + Suspense | Route split |
| Dynamic import manual | More boilerplate |

---

## Senior Pick

**Use:** lazy per route + Suspense fallback

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

> lazy(() => import('./Page')) returns component.

> Suspense boundary required.

> Nested Suspense for granular loading.

> Error boundary sibling for chunk fail.

> Next.js dynamic() similar.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Route lazy Dashboard
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Fallback | null | Skeleton | Skeleton |

---

## Follow-Up Questions

1. Suspense for data?
2. SSR lazy hydration?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Lazy loading |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | lazy per route + Suspense fallback |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [performance-optimization.md](../../01-core-concepts/performance-optimization.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

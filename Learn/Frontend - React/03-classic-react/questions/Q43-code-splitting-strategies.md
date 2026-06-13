# Code Splitting Strategies

**Track:** Classic React
**Companies:** Amazon, Google, Airbnb
**Difficulty:** Medium
**Case Study ID:** R-C-43

---

## Memory Hook

> **Route split first; component split for heavy libs**

---

## What Interviewers Test

Bundle optimization

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Single bundle | Slow FCP |
| Route lazy | Standard |
| Component lazy | Heavy chart/editor |

---

## Senior Pick

**Use:** Route-level lazy + prefetch on hover

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

> Analyze bundle visualizer.

> Split admin dashboard separately.

> Prefetch link hover import().

> Suspense fallback skeleton.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// lazy AdminDashboard
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Granularity | Every component | Routes + heavy | Balanced |

---

## Follow-Up Questions

1. Preload on intent?
2. SSR lazy chunks?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Bundle optimization |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Route-level lazy + prefetch on hover |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [performance-optimization.md](../../01-core-concepts/performance-optimization.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

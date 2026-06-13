# Core Web Vitals in React SPAs

**Track:** Classic React
**Companies:** Google, Shopify, Web.dev
**Difficulty:** Hard
**Case Study ID:** R-C-50

---

## Memory Hook

> **LCP FID INP — code split, images, defer JS**

---

## What Interviewers Test

Performance metrics

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Ignore metrics | SEO/UX hit |
| Optimize LCP image | Hero priority |
| Hydration cost | RSC/SSR helps |

---

## Senior Pick

**Use:** Measure → LCP element → split → lazy

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

> LCP: optimize hero image priority fetchpriority.

> INP: break long tasks transitions.

> CLS: reserve image dimensions.

> SSR/SSG for marketing pages.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// img fetchPriority high LCP
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Rendering | CSR only marketing | SSR/SSG | SSR/SSG |

---

## Follow-Up Questions

1. Partial hydration?
2. Streaming SSR metrics?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Performance metrics |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Measure → LCP element → split → lazy |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [performance-optimization.md](../../01-core-concepts/performance-optimization.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

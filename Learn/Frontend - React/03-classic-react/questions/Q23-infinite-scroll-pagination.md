# Infinite Scroll vs Pagination

**Track:** Classic React
**Companies:** Instagram, Pinterest, Amazon
**Difficulty:** Medium
**Case Study ID:** R-C-23

---

## Memory Hook

> **useInfiniteQuery + IntersectionObserver**

---

## What Interviewers Test

Large list data loading

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Load all | Bad |
| Page buttons | SEO friendly |
| Infinite scroll | Feed UX |

---

## Senior Pick

**Use:** Infinite for feeds; pages for admin tables

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

> IntersectionObserver sentinel at bottom.

> fetchNextPage when visible.

> getNextPageParam from API cursor.

> Virtualize combined with infinite.

> Accessibility: load more button alternative.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// useInfiniteQuery posts
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| UX | Infinite only | Button fallback | Button fallback a11y |

---

## Follow-Up Questions

1. Bidirectional infinite?
2. Cursor vs offset?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Large list data loading |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Infinite for feeds; pages for admin tables |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [data-fetching-caching.md](../../01-core-concepts/data-fetching-caching.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

# TanStack Query vs useEffect Fetch

**Track:** Classic React
**Companies:** Stripe, Vercel, Supabase
**Difficulty:** Hard
**Case Study ID:** R-C-21

---

## Memory Hook

> **Server state → Query; not useState cache**

---

## What Interviewers Test

Data fetching architecture

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| useEffect fetch | No cache dedupe |
| TanStack Query | Cache + retry |
| Redux for API | Boilerplate |

---

## Senior Pick

**Use:** TanStack Query default for server data

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

> Query key identifies cache entry.

> staleTime controls refetch.

> Mutations invalidate.

> Dedupes parallel same-key requests.

> useEffect lacks retry/backoff/stale-while-revalidate.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// useQuery users list
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Cache | useState | QueryClient | QueryClient |

---

## Follow-Up Questions

1. Prefetch on hover?
2. SSR dehydrate?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Data fetching architecture |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | TanStack Query default for server data |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [data-fetching-caching.md](../../01-core-concepts/data-fetching-caching.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

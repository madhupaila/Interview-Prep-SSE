# Cache Invalidation Strategies

**Track:** Classic React
**Companies:** Stripe, Supabase, PlanetScale
**Difficulty:** Hard
**Case Study ID:** R-C-44

---

## Memory Hook

> **Invalidate queries on mutation; granular keys**

---

## What Interviewers Test

Cache coherence

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Refetch everything | Wasteful |
| Targeted invalidate | Efficient |
| Manual setQueryData | Optimistic |

---

## Senior Pick

**Use:** Hierarchical query keys + invalidate prefixes

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

> ['posts'] and ['posts', id] hierarchy.

> invalidateQueries({queryKey:['posts']}).

> setQueryData for single entity update.

> staleTime tuning per entity type.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// invalidate after createPost
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Update | Refetch all | setQueryData + invalidate | Hybrid |

---

## Follow-Up Questions

1. Optimistic vs invalidate?
2. Real-time invalidate via WS?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Cache coherence |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Hierarchical query keys + invalidate prefixes |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [data-fetching-caching.md](../../01-core-concepts/data-fetching-caching.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

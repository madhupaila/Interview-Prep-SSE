# Optimistic Updates with Mutations

**Track:** Classic React
**Companies:** Twitter, Linear, Notion
**Difficulty:** Hard
**Case Study ID:** R-C-22

---

## Memory Hook

> **onMutate snapshot; rollback onError**

---

## What Interviewers Test

UX for instant feedback

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Wait for server | Slow UX |
| Optimistic UI | Instant |
| Pessimistic only | Safe but sluggish |

---

## Senior Pick

**Use:** Optimistic with rollback

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

> onMutate cancel outgoing queries.

> Snapshot previous cache.

> Apply optimistic patch.

> onError restore snapshot.

> onSettled invalidate.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Like button optimistic
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Conflict | Last write wins | Server reconcile | Server reconcile |

---

## Follow-Up Questions

1. Offline queue?
2. Idempotency keys?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | UX for instant feedback |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Optimistic with rollback |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [data-fetching-caching.md](../../01-core-concepts/data-fetching-caching.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

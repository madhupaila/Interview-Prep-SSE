# TanStack Query with Suspense

**Track:** Classic React
**Companies:** Remix, React 19 apps
**Difficulty:** Hard
**Case Study ID:** R-C-58

---

## Memory Hook

> **useSuspenseQuery throws promise to boundary**

---

## What Interviewers Test

Suspense data loading

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| isLoading branches | Verbose |
| Suspense boundary | Declarative |
| use + promise | React 19 |

---

## Senior Pick

**Use:** Suspense boundary per route segment

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

> useSuspenseQuery no isLoading.

> Error boundary sibling.

> Streaming SSR compatible patterns.

> Waterfall risk — prefetch parallel.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Suspense UserProfile query
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Loading UI | if loading | Suspense fallback | Suspense |

---

## Follow-Up Questions

1. Error boundary pairing?
2. Parallel suspense queries?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Suspense data loading |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Suspense boundary per route segment |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [data-fetching-caching.md](../../01-core-concepts/data-fetching-caching.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

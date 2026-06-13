# Redux Toolkit vs Zustand

**Track:** Classic React
**Companies:** Coinbase, Reddit, Discord
**Difficulty:** Medium
**Case Study ID:** R-C-38

---

## Memory Hook

> **Redux for middleware/debug; Zustand for simplicity**

---

## What Interviewers Test

Global client state pick

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Redux Toolkit | Large app tooling |
| Zustand | Minimal API |
| Context only | Perf limits |

---

## Senior Pick

**Use:** Zustand default; Redux if time-travel/middleware required

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

> RTK Query overlaps server cache.

> Zustand selectors prevent re-render.

> Redux DevTools.

> Don't put server cache in either — use Query.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Zustand cart store slice
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Boilerplate | Redux verbose | Zustand minimal | Zustand for MVP |

---

## Follow-Up Questions

1. Jotai vs Zustand?
2. When Redux still wins?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Global client state pick |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Zustand default; Redux if time-travel/middleware required |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [state-management.md](../../01-core-concepts/state-management.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

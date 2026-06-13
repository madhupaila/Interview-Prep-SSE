# useEffect vs useLayoutEffect

**Track:** Classic React
**Companies:** Apple, Adobe, Figma
**Difficulty:** Medium
**Case Study ID:** R-C-12

---

## Memory Hook

> **Layout = before paint; effect = after paint**

---

## What Interviewers Test

Effect timing

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| useEffect | Most side effects |
| useLayoutEffect | Measure DOM |
| useInsertionEffect | CSS-in-JS lib |

---

## Senior Pick

**Use:** useLayoutEffect only for measure/sync layout

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

> useLayoutEffect blocks paint — user-visible delay if slow.

> Use for tooltip position measure.

> Default useEffect for fetch/subscribe.

> SSR: useLayoutEffect warns — useEffect or client-only.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Tooltip position measure
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Fetch | useLayoutEffect | useEffect | useEffect |

---

## Follow-Up Questions

1. Flash of wrong layout?
2. SSR hydration mismatch?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Effect timing |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | useLayoutEffect only for measure/sync layout |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [hooks-deep-dive.md](../../01-core-concepts/hooks-deep-dive.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

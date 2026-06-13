# Design a Custom Hook

**Track:** Classic React
**Companies:** Vercel, Shopify, Notion
**Difficulty:** Medium
**Case Study ID:** R-C-11

---

## Memory Hook

> **Extract stateful logic; prefix use; compose hooks**

---

## What Interviewers Test

Custom hook architecture

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Hook returns JSX | Anti-pattern |
| Hook returns data + actions | Good |
| Class HOC | Legacy |

---

## Senior Pick

**Use:** Logic-only hook + presentational component

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

> Name useX — calls other hooks.

> Return stable API: { data, isLoading, mutate }.

> useDebounce, useLocalStorage, useMediaQuery examples.

> Test with renderHook.

> Share between containers without HOC.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// useDebouncedValue implementation
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Testing | Mount full tree | renderHook | renderHook |

---

## Follow-Up Questions

1. Hook calling hook rules?
2. Split useAuth vs useAuthProvider?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Custom hook architecture |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Logic-only hook + presentational component |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [hooks-deep-dive.md](../../01-core-concepts/hooks-deep-dive.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

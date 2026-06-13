# What Causes a Component to Re-render?

**Track:** Classic React
**Companies:** Google, Amazon, Apple
**Difficulty:** Easy
**Case Study ID:** R-C-03

---

## Memory Hook

> **State, parent, context — not props alone from stable parent**

---

## What Interviewers Test

Re-render triggers and propagation

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Only props change | Incomplete |
| State/context/parent re-render | Complete |
| Any hook call | Wrong |

---

## Senior Pick

**Use:** State change, parent re-render, context value change

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

> Own useState/useReducer update schedules re-render.

> Parent re-render re-renders children unless memoized.

> Context change re-renders all consumers.

> Changing ref.current does NOT re-render.

> Memo skips if props shallow-equal.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Parent state toggle re-renders child
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| memo | Skip equal props | Always render | Skip equal props |

---

## Follow-Up Questions

1. Does useContext always re-render?
2. React Compiler auto-memo?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Re-render triggers and propagation |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | State change, parent re-render, context value change |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

# useState vs useReducer — When to Use Which?

**Track:** Classic React
**Companies:** Stripe, Uber, LinkedIn
**Difficulty:** Medium
**Case Study ID:** R-C-06

---

## Memory Hook

> **Reducer when fields transition together**

---

## What Interviewers Test

Local state shape complexity

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| useState | Independent scalars |
| useReducer | Related transitions |
| useRef | Not for UI state |

---

## Senior Pick

**Use:** useReducer for wizard / state machine

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

> useState for toggles and single fields.

> useReducer when next state depends on prev across fields.

> Reducer pure function easy to unit test.

> Don't use reducer for everything — ceremony cost.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Checkout wizard step reducer
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Testing | Hook state | Pure reducer | Pure reducer |

---

## Follow-Up Questions

1. useReducer + Context as mini-Redux?
2. Immer with reducer?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Local state shape complexity |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | useReducer for wizard / state machine |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [state-management.md](../../01-core-concepts/state-management.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

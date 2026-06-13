# Lifting State Up

**Track:** Classic React
**Companies:** Google, Microsoft, Meta
**Difficulty:** Easy
**Case Study ID:** R-C-09

---

## Memory Hook

> **Siblings share state at common parent**

---

## What Interviewers Test

State colocation vs lift

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Duplicate state in siblings | Bug |
| Lift to parent | Correct |
| Global immediately | Overkill |

---

## Senior Pick

**Use:** Lift to nearest common ancestor

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

> Two components need same value → parent owns state.

> Pass callbacks down to update.

> Lift only as high as needed — not always to App.

> Pair with colocate principle.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Temperature converter two inputs
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| State location | Child | Parent | Parent |

---

## Follow-Up Questions

1. Lift vs Context threshold?
2. Colocate first rule?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | State colocation vs lift |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Lift to nearest common ancestor |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [state-management.md](../../01-core-concepts/state-management.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

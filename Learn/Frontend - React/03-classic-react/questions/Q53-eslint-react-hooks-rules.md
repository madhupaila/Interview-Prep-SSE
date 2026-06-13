# ESLint react-hooks Rules

**Track:** Classic React
**Companies:** Meta, Open source teams
**Difficulty:** Easy
**Case Study ID:** R-C-53

---

## Memory Hook

> **exhaustive-deps catches stale bugs**

---

## What Interviewers Test

Static analysis

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Disable rules | Ship bugs |
| Fix deps/cleanup | Correct |
| eslint-disable line | Last resort |

---

## Senior Pick

**Use:** Follow exhaustive-deps; extract functions

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

> Rules of hooks enforced.

> Missing deps warning.

> Extract stable callback or useCallback when needed.

> Custom eslint for design system.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Fix deps warning refactor
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Deps | Ignore | Fix root | Fix |

---

## Follow-Up Questions

1. React Compiler make deps moot?
2. Custom hook deps?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Static analysis |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Follow exhaustive-deps; extract functions |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [hooks-deep-dive.md](../../01-core-concepts/hooks-deep-dive.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

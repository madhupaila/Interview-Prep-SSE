# Prop Drilling — Solutions

**Track:** Classic React
**Companies:** Amazon, Walmart, Target
**Difficulty:** Medium
**Case Study ID:** R-C-08

---

## Memory Hook

> **Compose; Context; colocate; store — in that order of escalation**

---

## What Interviewers Test

Cross-component data passing

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Prop drilling 2 levels | OK |
| Context | Wide low-churn |
| Zustand | Many consumers high-churn |

---

## Senior Pick

**Use:** Props first; Context for theme/auth; store if needed

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

> Don't reach for Context on first drill.

> Component composition can flatten tree — children as props.

> Context for stable globals.

> Document drill vs context decision in design review.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Layout passes user vs UserContext
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Redux | All drilling | Minimal global | Minimal global |

---

## Follow-Up Questions

1. Component slots vs render props?
2. When is drilling actually fine?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Cross-component data passing |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Props first; Context for theme/auth; store if needed |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [component-patterns.md](../../01-core-concepts/component-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

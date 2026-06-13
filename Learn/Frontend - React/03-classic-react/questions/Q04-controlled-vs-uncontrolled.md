# Controlled vs Uncontrolled Components

**Track:** Classic React
**Companies:** Airbnb, Shopify, Microsoft
**Difficulty:** Medium
**Case Study ID:** R-C-04

---

## Memory Hook

> **Controlled = React owns value; uncontrolled = ref reads DOM**

---

## What Interviewers Test

Form input ownership model

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Controlled | value + onChange |
| Uncontrolled | defaultValue + ref |
| Hybrid | Avoid |

---

## Senior Pick

**Use:** Controlled for validation; uncontrolled for simple file input

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

> Controlled: single source of truth in state.

> Every keystroke setState — enables instant validation.

> Uncontrolled: ref.current.value on submit — less re-renders.

> React Hook Form often uncontrolled internally with register().

> File inputs typically uncontrolled.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// TextInput controlled vs ref read
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Validation timing | on submit | per keystroke | Per keystroke needs controlled |

---

## Follow-Up Questions

1. Fully controlled file upload?
2. Switch controlled mid-flight?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Form input ownership model |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Controlled for validation; uncontrolled for simple file input |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [component-patterns.md](../../01-core-concepts/component-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

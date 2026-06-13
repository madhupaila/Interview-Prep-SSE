# CSS-in-JS vs Tailwind in React

**Track:** Classic React
**Companies:** Vercel, Netflix, Stripe
**Difficulty:** Medium
**Case Study ID:** R-C-41

---

## Memory Hook

> **Tailwind for utility speed; CSS modules for isolation**

---

## What Interviewers Test

Styling architecture

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Inline styles | No pseudo |
| Tailwind | Rapid UI |
| Styled-components | Runtime cost RSC issue |

---

## Senior Pick

**Use:** Tailwind or CSS modules for RSC apps

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

> RSC pushes away runtime CSS-in-JS.

> Tailwind + design tokens.

> CSS modules scoped.

> Variant libraries cva.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Button with cva variants
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| RSC | styled-components default | Tailwind/CSS modules | Zero runtime CSS |

---

## Follow-Up Questions

1. Panda CSS?
2. Dark mode strategy?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Styling architecture |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Tailwind or CSS modules for RSC apps |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

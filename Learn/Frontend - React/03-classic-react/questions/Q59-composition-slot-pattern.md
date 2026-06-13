# Children and Slot Composition

**Track:** Classic React
**Companies:** Radix, shadcn/ui, Vercel
**Difficulty:** Medium
**Case Study ID:** R-C-59

---

## Memory Hook

> **children prop as composition slot**

---

## What Interviewers Test

Flexible layout API

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| title prop string only | Limited |
| children + header slot | Flexible |
| 12 layout props | Prop hell |

---

## Senior Pick

**Use:** children + optional named slots via props

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

> Card accepts children body.

> Optional header/footer props as ReactNode.

> Compound alternative.

> shadcn pattern cloneable components.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Card header={} children
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| API | Props | Composition | Composition |

---

## Follow-Up Questions

1. React 19 ref as prop?
2. Slot component pattern?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Flexible layout API |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | children + optional named slots via props |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [component-patterns.md](../../01-core-concepts/component-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

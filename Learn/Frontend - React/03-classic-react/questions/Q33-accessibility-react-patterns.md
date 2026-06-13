# Accessibility Patterns in React

**Track:** Classic React
**Companies:** Apple, Microsoft, GOV.UK
**Difficulty:** Hard
**Case Study ID:** R-C-33

---

## Memory Hook

> **Semantic HTML first; ARIA when needed; keyboard**

---

## What Interviewers Test

a11y senior signal

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| div onClick | Bad |
| button | Good |
| ARIA everything | Overkill |

---

## Senior Pick

**Use:** Semantic + keyboard + focus management

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

> Label linked with htmlFor/useId.

> Keyboard operable interactive elements.

> aria-live for dynamic updates.

> Focus visible styles.

> Test with axe and keyboard only.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Accessible modal dialog
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Custom widget | div | button + role if needed | Native first |

---

## Follow-Up Questions

1. Skip links?
2. Live region politeness levels?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | a11y senior signal |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Semantic + keyboard + focus management |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

# Design System Architecture in React

**Track:** Classic React
**Companies:** Shopify Polaris, Atlassian, IBM
**Difficulty:** Hard
**Case Study ID:** R-C-36

---

## Memory Hook

> **Tokens + primitives + patterns; headless optional**

---

## What Interviewers Test

Component library structure

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Copy-paste components | Drift |
| Design tokens + Storybook | Scale |
| Monolith UI folder | Chaos |

---

## Senior Pick

**Use:** Tokens → primitives → composites → docs

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

> CSS variables or Tailwind theme for tokens.

> Variant API via cva or similar.

> Storybook for docs and visual test.

> Semver independent package.

> Composition with Radix primitives.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Button variants token-driven
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Styling | Inline styles | Token system | Tokens |

---

## Follow-Up Questions

1. Theming dark mode?
2. Tree-shaking exports?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Component library structure |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Tokens → primitives → composites → docs |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [component-patterns.md](../../01-core-concepts/component-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

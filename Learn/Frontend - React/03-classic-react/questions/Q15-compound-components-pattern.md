# Compound Components Pattern

**Track:** Classic React
**Companies:** Radix, Shopify Polaris, Atlassian
**Difficulty:** Hard
**Case Study ID:** R-C-15

---

## Memory Hook

> **Implicit shared state via Context inside compound API**

---

## What Interviewers Test

Flexible component API design

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| 20 props on Select | Prop explosion |
| Compound Select.* | Composable |
| Single mega component | Inflexible |

---

## Senior Pick

**Use:** Compound + internal context

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

> Select, SelectTrigger, SelectContent share context.

> Consumer controls structure and styling.

> Used in Radix, Reach UI patterns.

> Alternative: headless hook + UI separate.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Tabs compound API sketch
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| API | Config object | Compound children | Compound |

---

## Follow-Up Questions

1. Headless UI vs compound?
2. Expose context hook?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Flexible component API design |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Compound + internal context |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [component-patterns.md](../../01-core-concepts/component-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

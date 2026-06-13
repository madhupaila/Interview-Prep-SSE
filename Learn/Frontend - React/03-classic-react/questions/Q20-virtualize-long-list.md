# Virtualize a Long List

**Track:** Classic React
**Companies:** Bloomberg, Robinhood, Meta
**Difficulty:** Hard
**Case Study ID:** R-C-20

---

## Memory Hook

> **Only render visible rows — react-window / tanstack virtual**

---

## What Interviewers Test

List performance

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| map 10k items | DOM explosion |
| Pagination | OK UX tradeoff |
| Virtualization | Best for feeds |

---

## Senior Pick

**Use:** TanStack Virtual or react-window

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

> Window scroll container with overscan.

> Fixed row height simplifies.

> Variable height needs measure.

> Preserve scroll anchor on prepend.

> Chat apps virtualize message list.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// VirtualizedMessageList
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Library | Manual | TanStack Virtual | TanStack Virtual |

---

## Follow-Up Questions

1. Reverse scroll chat?
2. Grid virtualization?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | List performance |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | TanStack Virtual or react-window |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [performance-optimization.md](../../01-core-concepts/performance-optimization.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

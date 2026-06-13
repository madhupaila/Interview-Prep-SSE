# Why Do Keys Matter in Lists?

**Track:** Classic React
**Companies:** Meta, Netflix, Stripe
**Difficulty:** Easy
**Case Study ID:** R-C-02

---

## Memory Hook

> **Key = row identity for reconciler**

---

## What Interviewers Test

List reconciliation and local state preservation

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Index key | Breaks on insert/sort |
| Random key each render | Full remount |
| Stable id from data | Correct |

---

## Senior Pick

**Use:** Stable unique id from domain data

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

> Keys tell React which item moved vs new.

> Index keys cause wrong component instance reuse.

> Focus and useState inside row jump to wrong item.

> Use item.id from API — never Math.random() in render.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// List with draggable rows — wrong keys demo
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Key source | index | item.id | item.id |
| UUID in render | Bad | Server id | Server id |

---

## Follow-Up Questions

1. Keys in Fragment lists?
2. Can two siblings share key?
3. React 19 key prop changes?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | List reconciliation and local state preservation |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Stable unique id from domain data |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [rendering-reconciliation.md](../../01-core-concepts/rendering-reconciliation.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

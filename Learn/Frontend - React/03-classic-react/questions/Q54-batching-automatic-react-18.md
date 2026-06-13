# Automatic Batching in React 18

**Track:** Classic React
**Companies:** Meta, React team
**Difficulty:** Medium
**Case Study ID:** R-C-54

---

## Memory Hook

> **Multiple setStates → one re-render in async too**

---

## What Interviewers Test

Update batching

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| React 17 async double render | Old behavior |
| React 18 auto batch | Default |
| flushSync escape hatch | Rare |

---

## Senior Pick

**Use:** Default batch; flushSync only when must sync DOM

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

> Event handlers always batched.

> setTimeout/promise batched in 18.

> flushSync forces sync for third-party lib.

> Fewer intermediate paints.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Three setStates one paint
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Sync need | Always flushSync | Rare flushSync | Rare |

---

## Follow-Up Questions

1. React 19 batch changes?
2. Batching with transitions?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Update batching |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Default batch; flushSync only when must sync DOM |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [rendering-reconciliation.md](../../01-core-concepts/rendering-reconciliation.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

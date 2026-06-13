# What is React Fiber?

**Track:** Classic React
**Companies:** Meta, Google, Discord
**Difficulty:** Hard
**Case Study ID:** R-C-05

---

## Memory Hook

> **Fiber = unit of work; enables interruptible rendering**

---

## What Interviewers Test

Concurrent React architecture

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Stack reconciler | Legacy sync |
| Fiber linked list | Incremental — pick |
| Web Worker render | Not React core |

---

## Senior Pick

**Use:** Fiber enables priority and splitting work

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

> Fiber is a JS object per component instance.

> Work loop can pause for high-priority updates.

> Enables Suspense, transitions, concurrent features.

> Commit phase still synchronous for DOM consistency.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Priority: typing > chart filter
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Rendering | Sync only | Interruptible | Interruptible |

---

## Follow-Up Questions

1. Scheduler package role?
2. Time slicing explained?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Concurrent React architecture |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Fiber enables priority and splitting work |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [rendering-reconciliation.md](../../01-core-concepts/rendering-reconciliation.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

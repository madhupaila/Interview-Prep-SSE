# Explain Virtual DOM and Reconciliation

**Track:** Classic React
**Companies:** Meta, Google, Amazon, Microsoft
**Difficulty:** Medium
**Case Study ID:** R-C-01

---

## Memory Hook

> **Trigger → render → diff → commit — keys = identity**

---

## What Interviewers Test

Rendering pipeline and why React batches updates

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Full DOM replace | Slow, loses focus |
| Virtual DOM + diff | Minimal mutations — default pick |
| Manual DOM | Error-prone |

---

## Senior Pick

**Use:** Virtual DOM + fiber reconciliation

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

> React doesn't touch the real DOM on every setState.

> It produces an element tree and diffs against the previous fiber tree.

> Only changed nodes commit to DOM.

> Keys identify list items — index keys break on reorder.

> Batching groups setStates in event handlers for one commit.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Diagram: state change → reconcile → commit
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Batching | Automatic in 18+ | Manual flushSync | Auto |
| Keys | Index | Stable ID | Stable ID |

---

## Follow-Up Questions

1. What is fiber?
2. Difference vs shadow DOM?
3. How does Concurrent mode interrupt work?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Rendering pipeline and why React batches updates |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Virtual DOM + fiber reconciliation |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [rendering-reconciliation.md](../../01-core-concepts/rendering-reconciliation.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

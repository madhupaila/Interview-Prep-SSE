# React.memo, useMemo, useCallback

**Track:** Classic React
**Companies:** Meta, Netflix, Bloomberg
**Difficulty:** Hard
**Case Study ID:** R-C-14

---

## Memory Hook

> **Profile first; memo needs stable props**

---

## What Interviewers Test

Memoization strategy

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Memo everything | Waste |
| Profile then memo | Senior |
| Never memo | Naive at scale |

---

## Senior Pick

**Use:** Profiler-driven memo + stable deps

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

> memo prevents re-render if props shallow equal.

> useMemo caches computation.

> useCallback stabilizes function reference.

> Inline objects break memo children.

> React Compiler may auto-memo in future.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Expensive list row memo
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| useCallback | Every handler | Only for memo child | Targeted |

---

## Follow-Up Questions

1. React Compiler impact?
2. useMemo for referential equality?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Memoization strategy |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Profiler-driven memo + stable deps |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [performance-optimization.md](../../01-core-concepts/performance-optimization.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

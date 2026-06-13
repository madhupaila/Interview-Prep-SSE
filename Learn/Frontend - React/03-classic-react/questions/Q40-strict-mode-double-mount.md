# React Strict Mode Double Mounting

**Track:** Classic React
**Companies:** Meta, Google, Microsoft
**Difficulty:** Medium
**Case Study ID:** R-C-40

---

## Memory Hook

> **Dev-only double invoke to find missing cleanup**

---

## What Interviewers Test

Development behavior

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Remove StrictMode | Hides bugs |
| Fix effect cleanup | Correct |
| Ignore duplicate fetch | Bad prod risk |

---

## Senior Pick

**Use:** Idempotent effects with cleanup

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

> useEffect runs mount-unmount-remount in dev.

> Missing cleanup → duplicate subscriptions.

> AbortController prevents duplicate fetch.

> Not a production behavior.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Fetch with abort on cleanup
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Dev UX | Disable Strict | Proper cleanup | Cleanup |

---

## Follow-Up Questions

1. Production double fetch?
2. React 19 Strict changes?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Development behavior |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Idempotent effects with cleanup |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [hooks-deep-dive.md](../../01-core-concepts/hooks-deep-dive.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

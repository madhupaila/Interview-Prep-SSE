# TypeScript Discriminated Unions for UI State

**Track:** Classic React
**Companies:** Linear, Notion, Figma
**Difficulty:** Hard
**Case Study ID:** R-C-31

---

## Memory Hook

> **status: loading | error | success narrows type**

---

## What Interviewers Test

Type-safe UI states

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| boolean flags isLoading isError | Impossible states |
| Discriminated union | Exhaustive switch |
| any | Avoid |

---

## Senior Pick

**Use:** Union on status field

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

> type State = {status:'loading'} | {status:'error',message:string} | {status:'success',data:T}.

> switch(status) exhaustiveness.

> No data access when loading without check.

> Use with TanStack Query status too.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// AsyncPanel discriminated union
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Flags | 3 booleans | 1 discriminant | Discriminant |

---

## Follow-Up Questions

1. Zod infer union?
2. React Query typed error?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Type-safe UI states |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Union on status field |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

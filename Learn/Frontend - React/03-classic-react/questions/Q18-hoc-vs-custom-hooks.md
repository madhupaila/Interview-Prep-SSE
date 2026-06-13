# HOC vs Custom Hooks

**Track:** Classic React
**Companies:** Meta, Twitter, Reddit
**Difficulty:** Medium
**Case Study ID:** R-C-18

---

## Memory Hook

> **Hooks replace most HOCs for logic sharing**

---

## What Interviewers Test

Code reuse patterns

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| HOC withAuth | Wrapper hell |
| useAuth hook | Preferred |
| Render props | Legacy |

---

## Senior Pick

**Use:** Custom hooks for logic; HOC rare for cross-cutting

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

> HOC adds wrapper nodes and prop collision.

> Hooks compose in one component.

> HOC still ok for truly cross-cutting analytics wrapper.

> displayName for HOC debug.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// useAuth vs withAuth
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Reuse | HOC default | Hook default | Hook |

---

## Follow-Up Questions

1. Hooks in class components?
2. Multiple hooks vs one HOC?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Code reuse patterns |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Custom hooks for logic; HOC rare for cross-cutting |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [component-patterns.md](../../01-core-concepts/component-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

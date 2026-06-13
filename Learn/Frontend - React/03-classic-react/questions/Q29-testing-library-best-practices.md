# React Testing Library Best Practices

**Track:** Classic React
**Companies:** GitHub, GitLab, Atlassian
**Difficulty:** Medium
**Case Study ID:** R-C-29

---

## Memory Hook

> **Query by role/label; test behavior not implementation**

---

## What Interviewers Test

Testing philosophy

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Enzyme shallow | Implementation detail |
| RTL user-centric | Preferred |
| Snapshot only | Brittle |

---

## Senior Pick

**Use:** RTL + userEvent + MSW

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

> getByRole button name submit.

> await userEvent.click.

> MSW mocks API.

> renderHook for custom hooks.

> Avoid testing internal state directly.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Login flow RTL test
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Mock | Fetch global | MSW | MSW |

---

## Follow-Up Questions

1. Testing async stream?
2. E2E vs unit split?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Testing philosophy |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | RTL + userEvent + MSW |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

# MSW for API Mocking in Tests

**Track:** Classic React
**Companies:** Stripe, Mock Service Worker team
**Difficulty:** Medium
**Case Study ID:** R-C-30

---

## Memory Hook

> **Network-level mock — same tests dev and CI**

---

## What Interviewers Test

API test doubles

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| jest.mock fetch | Brittle |
| MSW handlers | Realistic |
| Hard-coded in component | Bad |

---

## Senior Pick

**Use:** MSW server in test setup

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

> rest.get('/api/user') handler.

> Shared handlers with Storybook.

> Error scenario handlers.

> Reset handlers after each test.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// MSW handler 500 error test
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Scope | Unit only | Unit + Storybook | Shared handlers |

---

## Follow-Up Questions

1. GraphQL MSW?
2. Delay simulation?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | API test doubles |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | MSW server in test setup |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

# Prevent Double Form Submit

**Track:** Classic React
**Companies:** PayPal, Checkout.com, Amazon
**Difficulty:** Easy
**Case Study ID:** R-C-26

---

## Memory Hook

> **Disable button + isPending mutation state**

---

## What Interviewers Test

Form reliability

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Double click | Duplicate orders |
| Disabled while pending | Correct |
| Debounced submit only | Insufficient |

---

## Senior Pick

**Use:** isSubmitting guard + disable UI

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

> Set submitting true on submit start.

> Disable button and show spinner.

> useMutation isPending.

> Idempotency key on API for payments.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Submit button isLoading
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| API | Hope for best | Idempotency-Key header | Idempotency-Key |

---

## Follow-Up Questions

1. Optimistic duplicate risk?
2. Race two tabs?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Form reliability |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | isSubmitting guard + disable UI |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

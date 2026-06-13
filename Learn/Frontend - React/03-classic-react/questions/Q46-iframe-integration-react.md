# Integrating Third-Party Widgets (iframe)

**Track:** Classic React
**Companies:** Stripe Checkout, Intercom, Plaid
**Difficulty:** Medium
**Case Study ID:** R-C-46

---

## Memory Hook

> **postMessage bridge; sandbox attrs**

---

## What Interviewers Test

Safe embedding

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| eval script | Unsafe |
| iframe sandbox | Isolated |
| npm package | Preferred if available |

---

## Senior Pick

**Use:** Official SDK or sandboxed iframe

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

> Listen message event for height/payment done.

> Validate event.origin.

> React wrapper component lifecycle.

> Cleanup listener on unmount.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Stripe Embedded Checkout wrapper
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Security | inline script | iframe + origin check | iframe |

---

## Follow-Up Questions

1. OAuth popup pattern?
2. CSP frame-ancestors?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Safe embedding |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Official SDK or sandboxed iframe |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

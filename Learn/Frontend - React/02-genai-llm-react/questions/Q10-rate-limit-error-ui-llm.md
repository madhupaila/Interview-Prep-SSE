# Rate Limit & Quota Error UI

**Track:** Genai Llm React
**Companies:** OpenAI, Stripe AI, Vercel AI
**Difficulty:** Medium
**Case Study ID:** R-G-10

---

## Memory Hook

> **429 UI with retry-after countdown**

---

## What Interviewers Test

API limit UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Generic error | Unhelpful |
| 429 specific UI | Actionable |
| Silent fail | Bad |

---

## Senior Pick

**Use:** RateLimitBanner retryAfter

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

> Parse Retry-After header.

> Countdown timer.

> Upgrade CTA if quota.

> Disable send until window.

> Log for support.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// if status===429 show banner
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Retry | Immediate spam | Wait Retry-After | Wait |

---

## Follow-Up Questions

1. Tier upgrade flow?
2. Per-user vs org quota?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | API limit UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | RateLimitBanner retryAfter |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-genai-react.md](../memory-map-genai-react.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

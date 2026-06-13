# Thumbs Up/Down Feedback for LLM Responses

**Track:** Genai Llm React
**Companies:** OpenAI, Anthropic, Google
**Difficulty:** Medium
**Case Study ID:** R-G-13

---

## Memory Hook

> **Feedback mutation + optional comment modal**

---

## What Interviewers Test

Human eval signal collection

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| No feedback | Lost signal |
| Thumbs + trace id | ML ops |
| Feedback spam | Needs debounce |

---

## Senior Pick

**Use:** FeedbackButtons messageId traceId

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

> POST /feedback with message id.

> Disable after submit.

> Optional comment.

> Analytics event.

> Don't block chat on fail.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// submitFeedback mutation
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Identity | Anonymous ok | User id logged | Logged |

---

## Follow-Up Questions

1. A/B prompt eval?
2. Export feedback dataset?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Human eval signal collection |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | FeedbackButtons messageId traceId |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [00-genai-react-framework.md](../00-genai-react-framework.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

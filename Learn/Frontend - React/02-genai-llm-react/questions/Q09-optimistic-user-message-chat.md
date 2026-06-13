# Optimistic User Message in Chat

**Track:** Genai Llm React
**Companies:** WhatsApp, ChatGPT, Slack
**Difficulty:** Medium
**Case Study ID:** R-G-09

---

## Memory Hook

> **Instant user bubble; rollback on fail**

---

## What Interviewers Test

Chat send UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Wait server echo | Laggy |
| Optimistic append | Snappy |
| No error handle | Bad |

---

## Senior Pick

**Use:** Append user msg sending → sent/error

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

> Generate client temp id.

> Status sending until ACK.

> On error mark failed + retry.

> Dedupe on server id return.

> Disable input while sending optional.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// addMessage optimistic status
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Failure | Disappear | Show retry | Retry |

---

## Follow-Up Questions

1. Ordering with stream?
2. Offline queue?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Chat send UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Append user msg sending → sent/error |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [streaming-sse-chat-ui.md](../streaming-sse-chat-ui.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

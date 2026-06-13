# WebSocket vs SSE for Chat Apps

**Track:** Genai Llm React
**Companies:** Discord, Slack, OpenAI
**Difficulty:** Hard
**Case Study ID:** R-G-18

---

## Memory Hook

> **SSE one-way stream; WS bi-directional**

---

## What Interviewers Test

Transport choice

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| SSE + REST send | Simple |
| WebSocket | Real-time both ways |
| Long polling | Legacy |

---

## Senior Pick

**Use:** SSE stream + POST send for most LLM APIs

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

> OpenAI pattern POST then stream response.

> WS if server pushes multiple event types.

> SSE auto-reconnect.

> Auth easier on POST fetch.

> WS for collaborative cursors.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Architecture diagram POST+SSE vs WS
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Chat LLM | WS required | SSE typical | SSE |
| Collab | SSE enough | WS | WS |

---

## Follow-Up Questions

1. GraphQL subscriptions?
2. HTTP/3 streaming?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Transport choice |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | SSE stream + POST send for most LLM APIs |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [streaming-sse-chat-ui.md](../streaming-sse-chat-ui.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

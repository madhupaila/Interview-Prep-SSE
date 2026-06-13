# WebSocket vs Polling in React

**Track:** Classic React
**Companies:** Slack, Discord, Robinhood
**Difficulty:** Medium
**Case Study ID:** R-C-24

---

## Memory Hook

> **WebSocket for push; polling when simple**

---

## What Interviewers Test

Real-time UI

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Polling | Simple, wasteful |
| WebSocket | Low latency push |
| SSE | One-way server push |

---

## Senior Pick

**Use:** WebSocket for chat; SSE for notifications

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

> useEffect subscribe + cleanup close socket.

> Reconnect with exponential backoff.

> Update Query cache on message event.

> Don't store socket in useState.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// useEffect WebSocket cleanup
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| State | Global socket in module | Hook with cleanup | Hook |

---

## Follow-Up Questions

1. Socket.io vs raw WS?
2. Share socket across tabs?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Real-time UI |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | WebSocket for chat; SSE for notifications |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [data-fetching-caching.md](../../01-core-concepts/data-fetching-caching.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

# Implement Stop Generation Button

**Track:** Genai Llm React
**Companies:** OpenAI, Google Gemini, Copilot
**Difficulty:** Medium
**Case Study ID:** R-G-02

---

## Memory Hook

> **AbortController.abort() on active fetch**

---

## What Interviewers Test

Stream cancellation UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Ignore stop | Waste cost |
| AbortController | Correct |
| Close tab only | Bad UX |

---

## Senior Pick

**Use:** Shared abort ref per stream

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

> Store AbortController in ref.

> stop() calls abort.

> Catch AbortError silently.

> UI shows partial + Stopped.

> Cleanup abort on unmount.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// stop() abortRef.current.abort()
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Error | Show error toast | Treat abort as normal | Normal abort |

---

## Follow-Up Questions

1. Abort mid-token?
2. Server must handle disconnect?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Stream cancellation UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Shared abort ref per stream |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [streaming-sse-chat-ui.md](../streaming-sse-chat-ui.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

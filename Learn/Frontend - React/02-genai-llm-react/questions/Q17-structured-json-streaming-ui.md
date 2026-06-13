# Streaming Structured JSON (UI Schema)

**Track:** Genai Llm React
**Companies:** OpenAI JSON mode, Vercel AI SDK
**Difficulty:** Hard
**Case Study ID:** R-G-17

---

## Memory Hook

> **Partial JSON parse or schema-validated chunks**

---

## What Interviewers Test

Structured output rendering

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Wait full JSON | Slow UX |
| Incremental parse | Progressive UI |
| Regex extract | Fragile |

---

## Senior Pick

**Use:** Schema form fills as JSON streams

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

> Use zod schema.

> partial-json parser library.

> Show fields as validated.

> Error highlight invalid.

> Fallback raw view dev.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// useStructuredStream schema
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Parse | JSON.parse once | Partial parser | Partial |

---

## Follow-Up Questions

1. UI forms from schema?
2. Recover corrupt stream?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Structured output rendering |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Schema form fills as JSON streams |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [streaming-sse-chat-ui.md](../streaming-sse-chat-ui.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

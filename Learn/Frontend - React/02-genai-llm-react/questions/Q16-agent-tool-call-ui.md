# Display Agent Tool Calls in UI

**Track:** Genai Llm React
**Companies:** OpenAI Assistants, Anthropic, LangGraph
**Difficulty:** Hard
**Case Study ID:** R-G-16

---

## Memory Hook

> **Expandable tool steps running/done/error**

---

## What Interviewers Test

Agent transparency UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Hide tools | Black box |
| Step timeline | Trust |
| Raw JSON | Dev only |

---

## Senior Pick

**Use:** ToolCallStep accordion status

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

> Parse tool_call events from stream.

> Show name + args summary.

> Spinner running checkmark done.

> Error retry step.

> Collapse verbose args.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// ToolRunTimeline events
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Detail | Full JSON default | Human summary | Summary |

---

## Follow-Up Questions

1. Human approve tool?
2. Parallel tool calls?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Agent transparency UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | ToolCallStep accordion status |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [00-genai-react-framework.md](../00-genai-react-framework.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

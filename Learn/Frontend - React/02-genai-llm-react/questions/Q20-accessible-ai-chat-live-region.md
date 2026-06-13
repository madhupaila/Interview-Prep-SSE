# Accessible AI Chat (ARIA Live Regions)

**Track:** Genai Llm React
**Companies:** Microsoft, Apple, GOV.UK
**Difficulty:** Hard
**Case Study ID:** R-G-20

---

## Memory Hook

> **role=log aria-live polite; focus management**

---

## What Interviewers Test

a11y for streaming chat

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Silent stream | SR users miss updates |
| aria-live polite | Correct |
| aria-live assertive every token | Too aggressive |

---

## Senior Pick

**Use:** polite live region + manual review button

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

> New assistant message announced politely.

> Don't move focus on each token.

> Keyboard send Shift+Enter.

> Stop button focusable.

> High contrast mode support.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// div role=log aria-live=polite
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Announce | Every token assertive | Message complete polite | Polite |

---

## Follow-Up Questions

1. VoiceOver test plan?
2. Mobile a11y chat?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | a11y for streaming chat |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | polite live region + manual review button |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-genai-react.md](../memory-map-genai-react.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

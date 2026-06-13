# Inline Copilot Ghost Text Suggestion

**Track:** Genai Llm React
**Companies:** GitHub Copilot, Cursor, Superhuman
**Difficulty:** Hard
**Case Study ID:** R-G-15

---

## Memory Hook

> **Ghost completion Tab to accept Esc dismiss**

---

## What Interviewers Test

Inline AI assist UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Modal only | Disruptive |
| Inline ghost text | Copilot pattern |
| Auto-insert all | Dangerous |

---

## Senior Pick

**Use:** GhostText debounced inline API

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

> Debounce keystroke 300ms.

> Fetch completion.

> Show gray ghost suffix.

> Tab accepts Esc clears.

> Don't flash on fast typists.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// useInlineCompletion editor
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Accept | Auto apply | Explicit Tab | Tab |

---

## Follow-Up Questions

1. Multi-line ghost?
2. Privacy send code snippet?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Inline AI assist UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | GhostText debounced inline API |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-genai-react.md](../memory-map-genai-react.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

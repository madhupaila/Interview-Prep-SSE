# Conversation Thread History Sidebar

**Track:** Genai Llm React
**Companies:** ChatGPT, Claude, Slack AI
**Difficulty:** Medium
**Case Study ID:** R-G-06

---

## Memory Hook

> **Thread list + URL threadId + Query cache**

---

## What Interviewers Test

Multi-chat persistence UI

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Single thread only | MVP |
| Sidebar threads + URL | Product |
| LocalStorage only | No sync |

---

## Senior Pick

**Use:** TanStack Query threads + router param

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

> GET /threads list.

> Select sets route /chat/:id.

> New chat mutation.

> Rename/delete thread.

> Optimistic new thread.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// ThreadSidebar useQuery threads
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Persist | Memory | API + URL | API + URL |

---

## Follow-Up Questions

1. Search threads?
2. Archive vs delete?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Multi-chat persistence UI |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | TanStack Query threads + router param |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [00-genai-react-framework.md](../00-genai-react-framework.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

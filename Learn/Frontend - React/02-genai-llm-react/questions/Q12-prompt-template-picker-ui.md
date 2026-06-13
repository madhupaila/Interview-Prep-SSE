# Prompt Template Picker UI

**Track:** Genai Llm React
**Companies:** LangChain, Jasper, Copy.ai
**Difficulty:** Medium
**Case Study ID:** R-G-12

---

## Memory Hook

> **Template gallery inserts into input**

---

## What Interviewers Test

Prompt productivity UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Blank input only | Slow users |
| Template variables form | Guided |
| Hard-coded strings | Unmaintainable |

---

## Senior Pick

**Use:** TemplateGallery + variable modal

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

> Fetch templates API.

> Insert with {{var}} substitution.

> Preview filled prompt.

> Save custom template.

> Categories/tags filter.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// PromptTemplateModal variables
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Storage | Component state | API templates | API |

---

## Follow-Up Questions

1. Version templates?
2. Team shared templates?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Prompt productivity UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | TemplateGallery + variable modal |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [00-genai-react-framework.md](../00-genai-react-framework.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

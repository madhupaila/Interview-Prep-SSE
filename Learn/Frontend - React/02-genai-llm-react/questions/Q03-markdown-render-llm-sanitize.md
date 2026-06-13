# Safely Render LLM Markdown Output

**Track:** Genai Llm React
**Companies:** OpenAI, Notion AI, GitHub Copilot
**Difficulty:** Hard
**Case Study ID:** R-G-03

---

## Memory Hook

> **react-markdown + rehype-sanitize — no raw HTML**

---

## What Interviewers Test

XSS-safe rich text from model

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| dangerouslySetInnerHTML | XSS |
| react-markdown + sanitize | Pick |
| Plain text only | Safe limited |

---

## Senior Pick

**Use:** react-markdown + rehype-sanitize

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

> Models emit markdown not trusted HTML.

> Syntax highlight code blocks.

> Copy code button.

> Links open new tab rel noopener.

> Sanitize strips script/onclick.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// ReactMarkdown remarkPlugins rehypeSanitize
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| HTML | Raw | Sanitized pipeline | Sanitized |

---

## Follow-Up Questions

1. KaTeX math?
2. Mermaid diagrams sandbox?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | XSS-safe rich text from model |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | react-markdown + rehype-sanitize |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [rag-ui-patterns.md](../rag-ui-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

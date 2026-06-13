# XSS and dangerouslySetInnerHTML

**Track:** Classic React
**Companies:** Auth0, Okta, OpenAI
**Difficulty:** Hard
**Case Study ID:** R-C-34

---

## Memory Hook

> **Sanitize HTML; prefer markdown pipeline**

---

## What Interviewers Test

Security in rich text UI

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Raw HTML from LLM | XSS risk |
| DOMPurify sanitize | Safer |
| Plain text only | Safest |

---

## Senior Pick

**Use:** Sanitize + CSP + avoid inline scripts

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

> LLM output can contain script tags.

> Use DOMPurify or rehype-sanitize.

> Content-Security-Policy header.

> Never pass user HTML unsanitized.

> Markdown safer than raw HTML.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// sanitize(html) before render
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Render | dangerouslySetInnerHTML raw | sanitized | sanitized |

---

## Follow-Up Questions

1. Markdown vs HTML LLM?
2. CSP nonce with Next?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Security in rich text UI |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Sanitize + CSP + avoid inline scripts |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

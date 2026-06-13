# Multimodal Image Attachment UI

**Track:** Genai Llm React
**Companies:** GPT-4V, Gemini, Claude Vision
**Difficulty:** Hard
**Case Study ID:** R-G-11

---

## Memory Hook

> **Preview thumbnail + base64/upload + vision API**

---

## What Interviewers Test

Image + text prompt UI

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Text only | Limited |
| Attachment chip preview | Multimodal |
| Paste URL only | Fragile |

---

## Senior Pick

**Use:** AttachmentPreview + presigned upload

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

> Drag-drop images.

> Validate size/type.

> Upload then send URL to model.

> Remove attachment before send.

> Loading thumbnail state.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// ChatInput attachments array
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Upload | Base64 huge payload | Presigned S3 | Presigned |

---

## Follow-Up Questions

1. Multiple images?
2. Progress on upload?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Image + text prompt UI |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | AttachmentPreview + presigned upload |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-genai-react.md](../memory-map-genai-react.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

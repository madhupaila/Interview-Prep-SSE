# Document Upload with Ingestion Status

**Track:** Genai Llm React
**Companies:** Notion AI, Databricks, Anthropic
**Difficulty:** Hard
**Case Study ID:** R-G-05

---

## Memory Hook

> **Upload → job id → poll/SSE status → ready**

---

## What Interviewers Test

Async RAG ingest UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Instant query after upload | Wrong |
| Progress per doc | Correct |
| Block whole app | Bad UX |

---

## Senior Pick

**Use:** UploadZone + per-file status row

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

> Multipart upload to S3 presigned.

> Poll ingest job or SSE events.

> States: uploading parsing embedding ready error.

> Enable chat when doc ready.

> Cancel upload abort.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// DocumentRow status enum
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Feedback | Spinner only | Per-stage progress | Per-stage |

---

## Follow-Up Questions

1. Batch upload 50 PDFs?
2. Retry failed ingest?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Async RAG ingest UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | UploadZone + per-file status row |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [rag-ui-patterns.md](../rag-ui-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

# Degraded Mode When LLM API Is Down

**Track:** Genai Llm React
**Companies:** OpenAI, Enterprise SaaS
**Difficulty:** Medium
**Case Study ID:** R-G-19

---

## Memory Hook

> **Cached answers + banner + retry queue**

---

## What Interviewers Test

Resilience UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| White screen error | Bad |
| Graceful banner + cached FAQ | Enterprise |
| Infinite spinner | Bad |

---

## Senior Pick

**Use:** HealthCheck banner + fallback search

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

> Probe /health model status.

> Show banner degraded.

> Offer cached docs search.

> Queue messages retry later.

> Status page link.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// DegradedBanner health query
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| UX | Block app | Partial features | Partial |

---

## Follow-Up Questions

1. Multi-region failover?
2. Statuspage embed?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Resilience UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | HealthCheck banner + fallback search |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-genai-react.md](../memory-map-genai-react.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

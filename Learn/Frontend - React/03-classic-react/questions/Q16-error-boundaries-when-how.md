# Error Boundaries — When and How

**Track:** Classic React
**Companies:** Sentry, Datadog, Airbnb
**Difficulty:** Medium
**Case Study ID:** R-C-16

---

## Memory Hook

> **class component; catches render errors in children**

---

## What Interviewers Test

Error isolation

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| try/catch in render | Doesn't work |
| Error boundary | Catches render |
| Error in event handler | Handler try/catch |

---

## Senior Pick

**Use:** Boundary per route/feature + fallback UI

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

> getDerivedStateFromError + componentDidCatch.

> Doesn't catch event handlers, async, SSR alone.

> Log to Sentry in didCatch.

> Reset boundary with key prop on retry.

> react-error-boundary package wrapper.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// FeaturePanel ErrorBoundary fallback
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Granularity | Whole app | Per feature | Per feature |

---

## Follow-Up Questions

1. React 19 error boundaries?
2. Async server component errors?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Error isolation |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Boundary per route/feature + fallback UI |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [component-patterns.md](../../01-core-concepts/component-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

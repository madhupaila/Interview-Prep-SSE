# Feature Flags in React UI

**Track:** Classic React
**Companies:** LaunchDarkly, Netflix, GitHub
**Difficulty:** Medium
**Case Study ID:** R-C-49

---

## Memory Hook

> **Flag provider; skeleton while loading flags**

---

## What Interviewers Test

Gradual rollout UI

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| if (env) hardcode | Not dynamic |
| LaunchDarkly SDK | Runtime |
| Build-time only | No runtime toggle |

---

## Senior Pick

**Use:** Flag provider + hook useFlag('new-chat')

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

> Load flags on init.

> Fallback default false.

> Don't flash wrong UI — wait or skeleton.

> Analytics track flag exposure.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// useFeatureFlag newDashboard
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Source | Env var only | Flag service | Flag service |

---

## Follow-Up Questions

1. A/B assignment persist?
2. SSR flags?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Gradual rollout UI |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Flag provider + hook useFlag('new-chat') |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

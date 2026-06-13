# React vs React Native (Interview Bridge)

**Track:** Classic React
**Companies:** Meta, Expo, Discord
**Difficulty:** Medium
**Case Study ID:** R-C-51

---

## Memory Hook

> **Same React model; different primitives View Text**

---

## What Interviewers Test

Cross-platform mental model

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| DOM elements web | div span |
| Native components | View Text |
| Shared logic hooks | Reuse business hooks |

---

## Senior Pick

**Use:** Share hooks; platform-specific UI

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

> useState/useEffect same.

> StyleSheet vs CSS.

> Navigation React Navigation.

> Don't assume DOM APIs on native.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Shared useAuth hook
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| UI | Same components | Platform split | Platform split |

---

## Follow-Up Questions

1. Expo router?
2. Native performance lists?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Cross-platform mental model |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Share hooks; platform-specific UI |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

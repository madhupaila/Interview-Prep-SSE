# Micro Frontends in React

**Track:** Classic React
**Companies:** Spotify, IKEA, Zalando
**Difficulty:** Hard
**Case Study ID:** R-C-37

---

## Memory Hook

> **Module federation or iframe; shared design system**

---

## What Interviewers Test

Large org frontend scale

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Monolith SPA | Simple |
| Module Federation | Runtime integrate |
| Iframe MFE | Isolation heavy |

---

## Senior Pick

**Use:** Federation for team autonomy with shared shell

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

> Shell app handles routing/auth.

> Remote exposes exposed modules.

> Shared react singleton version.

> Independent deploy.

> Tradeoff: runtime coupling vs build complexity.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Webpack ModuleFederation config sketch
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Integration | Monorepo only | Federation | Team scale dependent |

---

## Follow-Up Questions

1. Single-spa?
2. CSS isolation?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Large org frontend scale |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Federation for team autonomy with shared shell |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

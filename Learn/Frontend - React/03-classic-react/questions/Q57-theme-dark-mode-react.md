# Dark Mode Implementation

**Track:** Classic React
**Companies:** GitHub, Twitter, Slack
**Difficulty:** Medium
**Case Study ID:** R-C-57

---

## Memory Hook

> **CSS variables + class on html; avoid flash**

---

## What Interviewers Test

Theming

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Inline theme state only | Flash |
| class dark on html | Standard |
| Separate CSS files | Maintain burden |

---

## Senior Pick

**Use:** ThemeProvider + localStorage + system pref

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

> Match media prefers-color-scheme.

> Persist user override.

> Script in head prevent flash FOUC.

> Context toggles theme.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// ThemeProvider useEffect flash script
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Storage | None | localStorage + system | Both |

---

## Follow-Up Questions

1. Tailwind dark:
2. Per-component tokens?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Theming |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | ThemeProvider + localStorage + system pref |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [state-management.md](../../01-core-concepts/state-management.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

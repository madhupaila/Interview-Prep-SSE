# i18n in React (react-i18next)

**Track:** Classic React
**Companies:** Airbnb, Booking.com, Uber
**Difficulty:** Medium
**Case Study ID:** R-C-48

---

## Memory Hook

> **Keys not concatenated strings; locale date/number**

---

## What Interviewers Test

Internationalization

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Hard-coded English | Bad |
| react-i18next | Standard |
| Google translate widget | Poor UX |

---

## Senior Pick

**Use:** i18next + namespace lazy load

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

> t('checkout.title') keys.

> Interpolation {{name}}.

> Format dates with Intl.

> RTL layout CSS.

> Suspense load language bundle.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// useTranslation checkout namespace
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Strings | Inline | Key files | Key files |

---

## Follow-Up Questions

1. Plural rules?
2. SSR locale detection?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Internationalization |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | i18next + namespace lazy load |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

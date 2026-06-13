# Portals, Modals, and Focus Trap

**Track:** Classic React
**Companies:** Stripe, LinkedIn, Discord
**Difficulty:** Medium
**Case Study ID:** R-C-17

---

## Memory Hook

> **createPortal escapes z-index; trap focus for a11y**

---

## What Interviewers Test

Modal accessibility

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Modal in tree | Stacking issues |
| Portal to body | Correct |
| No focus trap | a11y fail |

---

## Senior Pick

**Use:** Portal + focus trap + Esc close

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

> ReactDOM.createPortal for overlay.

> Focus first focusable on open.

> Restore focus on close.

> aria-modal role dialog.

> Use Radix Dialog or FocusTrap lib.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Modal open focus return
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Library | Roll own | Radix Dialog | Radix |

---

## Follow-Up Questions

1. Scroll lock body?
2. Nested modals?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Modal accessibility |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Portal + focus trap + Esc close |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [component-patterns.md](../../01-core-concepts/component-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

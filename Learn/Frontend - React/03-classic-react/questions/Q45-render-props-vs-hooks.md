# Render Props vs Hooks

**Track:** Classic React
**Companies:** React community, Airbnb legacy
**Difficulty:** Medium
**Case Study ID:** R-C-45

---

## Memory Hook

> **Hooks replaced most render prop patterns**

---

## What Interviewers Test

API evolution

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Render prop <Data fn={} /> | Callback nesting |
| useData hook | Clean |
| Both mixed | Confusing |

---

## Senior Pick

**Use:** Hooks for new code

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

> Render props still valid for inversion.

> Hooks easier to compose.

> No wrapper component nesting.

> Libraries migrated Mouse/useMouse.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// useMouse vs Mouse render prop
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| New code | Render props | Hooks | Hooks |

---

## Follow-Up Questions

1. When render props still better?
2. Children as function?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | API evolution |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Hooks for new code |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [component-patterns.md](../../01-core-concepts/component-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

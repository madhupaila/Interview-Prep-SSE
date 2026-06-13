# Drag and Drop in React

**Track:** Classic React
**Companies:** Trello, Notion, Figma
**Difficulty:** Hard
**Case Study ID:** R-C-47

---

## Memory Hook

> **dnd-kit or react-beautiful-dnd; keyboard a11y**

---

## What Interviewers Test

DnD UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| HTML5 DnD alone | Limited mobile |
| dnd-kit | Modern a11y |
| Manual mouse events | Reinvent |

---

## Senior Pick

**Use:** dnd-kit with sortable context

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

> Sensors for pointer and keyboard.

> Optimistic reorder local state.

> Persist order API on drop.

> Touch support.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// SortableList dnd-kit
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Library | react-beautiful-dnd unmaintained | dnd-kit | dnd-kit |

---

## Follow-Up Questions

1. Virtual list + DnD?
2. Multi-list drag?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | DnD UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | dnd-kit with sortable context |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

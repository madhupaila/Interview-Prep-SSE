# System Design: Build a Notion-like Editor UI

**Track:** Classic React
**Companies:** Notion, Coda, Linear
**Difficulty:** Hard
**Case Study ID:** R-C-60

---

## Memory Hook

> **Block model; lazy blocks; collaboration cursor**

---

## What Interviewers Test

Frontend system design

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| contentEditable alone | Fragile |
| ProseMirror/Slate | Battle-tested |
| Custom from scratch | High cost |

---

## Senior Pick

**Use:** Block-based editor library + virtualize

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

> Block array state normalized by id.

> Plugin architecture bold/link.

> Lazy load heavy blocks.

> OT/CRDT for collab — separate service.

> Undo stack command pattern.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// BlockEditor component architecture
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Collab | Lock file | CRDT layer | CRDT |
| State | One string | Block map | Block map |

---

## Follow-Up Questions

1. How scale 10k blocks?
2. Mobile editor UX?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Frontend system design |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Block-based editor library + virtualize |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [component-patterns.md](../../01-core-concepts/component-patterns.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

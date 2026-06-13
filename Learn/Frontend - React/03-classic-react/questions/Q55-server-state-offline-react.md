# Offline-First UI Patterns

**Track:** Classic React
**Companies:** Notion, Figma, Linear
**Difficulty:** Hard
**Case Study ID:** R-C-55

---

## Memory Hook

> **Optimistic queue; online detector; sync status**

---

## What Interviewers Test

Offline UX

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Block UI offline | Poor UX |
| Queue mutations | Better |
| Full PWA sync | Complex |

---

## Senior Pick

**Use:** Online banner + queued mutations replay

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

> navigator.onLine + events.

> Persist queue IndexedDB.

> Replay on reconnect.

> Conflict UI if server rejects.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// useOnlineStatus hook
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Storage | memory queue | IndexedDB | IndexedDB |

---

## Follow-Up Questions

1. CRDT vs last-write?
2. Service worker cache?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Offline UX |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Online banner + queued mutations replay |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [data-fetching-caching.md](../../01-core-concepts/data-fetching-caching.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

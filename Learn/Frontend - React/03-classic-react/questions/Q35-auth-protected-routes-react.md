# Protected Routes and Auth State

**Track:** Classic React
**Companies:** Auth0, Stripe, Plaid
**Difficulty:** Medium
**Case Study ID:** R-C-35

---

## Memory Hook

> **AuthProvider + redirect; token refresh**

---

## What Interviewers Test

Authentication UI flow

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Check token in each component | Duplicate |
| ProtectedRoute wrapper | Central |
| Middleware Next.js | Server gate |

---

## Senior Pick

**Use:** Context or Query for session + route guard

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

> Load session on app init.

> Show skeleton while validating.

> Redirect unauthenticated to login.

> Preserve return URL.

> Refresh token silent before expiry.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// ProtectedRoute outlet redirect
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Storage | localStorage only | httpOnly cookie + API | httpOnly cookie |

---

## Follow-Up Questions

1. RBAC UI gating?
2. SSR auth check?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Authentication UI flow |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | Context or Query for session + route guard |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

# Forms with React Hook Form + Zod

**Track:** Classic React
**Companies:** Stripe, Typeform, HubSpot
**Difficulty:** Medium
**Case Study ID:** R-C-25

---

## Memory Hook

> **RHF uncontrolled perf + Zod schema validation**

---

## What Interviewers Test

Form architecture

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Controlled every field | Re-render heavy |
| RHF register | Performant |
| Formik | Valid alternative |

---

## Senior Pick

**Use:** RHF + zodResolver

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

> Schema single source of validation rules.

> handleSubmit wraps async API.

> Field errors from formState.

> watch() for dependent fields.

> Reset on success.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
// Login form zod schema
// Expand in interview: types first → component shell → edge states
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Validation | Manual | Zod schema | Zod |

---

## Follow-Up Questions

1. Multi-step wizard?
2. Server-side errors map to fields?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | Form architecture |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | RHF + zodResolver |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [memory-map-master.md](../../01-core-concepts/memory-map-master.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

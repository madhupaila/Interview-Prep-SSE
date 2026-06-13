# State Management — Local, Global, Server

Where data lives determines architecture quality.

---

## Decision Tree

```
Is it from the API?
  YES → TanStack Query / SWR (server state)
  NO → Is it URL-reflectable?
    YES → Router search params / path
    NO → Used by 1 component?
      YES → useState / useReducer
      NO → Many distant components?
        YES → Context (low churn) OR Zustand/Redux (high churn / middleware)
```

---

## useState vs useReducer

| useState | useReducer |
|----------|------------|
| Independent values | Related fields that update together |
| Simple toggles | State machine (wizard steps, form) |
| | Easier to test reducer pure function |

---

## Context Performance

**Problem:** Any context value change re-renders **all** consumers.

**Fixes:**
1. Split contexts (ThemeContext vs UserContext)
2. Memoize value: `useMemo(() => ({ user, login }), [user, login])`
3. Move frequently changing state down or to external store
4. `useContextSelector` patterns (Zustand) or split provider components

---

## Server State vs Client State

| Server state | Client state |
|--------------|--------------|
| From API, cacheable | UI-only: modal open, selected tab |
| TanStack Query owns it | useState / Zustand |
| Stale-while-revalidate | Optimistic UI before server confirms |

**Senior line:** "I don't copy API responses into Redux unless I need offline editing with sync."

---

## Lifting State Up

Lift when **siblings** need the same state. Don't lift to root by default.

---

## Interview Script

> "I colocate state in the component that owns the UX. Server data goes in TanStack Query with staleTime and invalidation on mutations. I use Context for theme and auth snapshot — low update frequency. If many components need high-churn client state, Zustand is lighter than Redux for our scale. I use useReducer when transitions are explicit, like a multi-step form."

---

## Related

- [Decision Picker](../00-interview-framework/04-decision-picker.md)
- [Data Fetching](data-fetching-caching.md)

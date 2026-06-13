# Component Patterns & Composition

How to structure components for scale and interview clarity.

---

## Composition vs Inheritance

React favors **composition** (`children`, slots, render props replaced by hooks).

```typescript
// Compound component pattern
<Select>
  <Select.Trigger />
  <Select.Options>
    <Select.Option value="a">A</Select.Option>
  </Select.Options>
</Select>
```

---

## Pattern Picker

| Pattern | Use when |
|---------|----------|
| **Container/Presentational** | Separate data hook from pure UI (still valid via custom hooks) |
| **Compound components** | Flexible API (Tabs, Accordion, Select) |
| **Custom hook** | Shared stateful logic (preferred over HOC) |
| **Render props** | Legacy libraries; hooks usually cleaner |
| **HOC** | Cross-cutting auth/logging (hooks often replace) |
| **Portal** | Modal, tooltip, dropdown — escape stacking context |
| **Error boundary** | Catch render errors in subtree |

---

## Controlled vs Uncontrolled

| Controlled | Uncontrolled |
|------------|--------------|
| React owns value via state | DOM owns value; ref reads it |
| Instant validation | Simpler file inputs |
| Single source of truth | React Hook Form often uncontrolled internally |

---

## Prop Drilling vs Context vs Store

- **1–2 levels:** props
- **Static global:** Context
- **Dynamic global:** Zustand
- **Server:** Query cache

---

## Interview Script

> "I compose small focused components. Shared logic goes in custom hooks — useAuth, usePagination. For design-system primitives I use compound components so consumers control layout without prop explosion. Modals use createPortal with focus trap. Error boundaries wrap route features so one chart crash doesn't white-screen the app."

---

## Related Questions

- [Q15 Compound components](../03-classic-react/questions/Q15-compound-components-pattern.md)
- [Q16 Error boundaries](../03-classic-react/questions/Q16-error-boundaries-when-how.md)

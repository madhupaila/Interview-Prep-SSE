# TypeScript with React — Interview Essentials

---

## Props Typing

```typescript
interface ButtonProps {
  label: string;
  onClick: () => void;
  variant?: 'primary' | 'ghost';
  disabled?: boolean;
}

export function Button({ label, onClick, variant = 'primary', disabled }: ButtonProps) {
  return <button type="button" className={variant} disabled={disabled} onClick={onClick}>{label}</button>;
}
```

---

## Discriminated Unions for UI State

```typescript
type LoadState<T> =
  | { status: 'idle' }
  | { status: 'loading' }
  | { status: 'error'; message: string }
  | { status: 'success'; data: T };

function Panel({ state }: { state: LoadState<User> }) {
  switch (state.status) {
    case 'idle': return null;
    case 'loading': return <Spinner />;
    case 'error': return <Alert>{state.message}</Alert>;
    case 'success': return <Profile user={state.data} />;
  }
}
```

---

## Utility Types

| Type | Use |
|------|-----|
| `ComponentPropsWithoutRef<'button'>` | Extend native elements |
| `React.ReactNode` | children |
| `Pick<User, 'id' \| 'name'>` | Partial props from model |
| `ReturnType<typeof useAuth>` | Hook return type |

---

## Interview Script

> "I type props explicitly, use discriminated unions for async UI so impossible states don't compile, and infer hook return types for consumers. For generic DataTable I constrain T extends { id: string }."

---

## Related Questions

- [Q31 Discriminated unions](../03-classic-react/questions/Q31-typescript-discriminated-unions-ui.md)
- [Q32 Generic components](../03-classic-react/questions/Q32-generic-react-components.md)

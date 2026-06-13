# Hooks Deep Dive

Hooks are **composition units** — interviewers test rules, closures, and cleanup.

---

## Rules of Hooks

1. Only call at **top level** (not in if/for)
2. Only call from **React functions** (components or custom hooks)

**Why:** React stores hook state by **call order** in the fiber.

---

## Hook Reference (Interview Essentials)

| Hook | Purpose | Pitfall |
|------|---------|---------|
| `useState` | Local state | Stale state in async — use functional update |
| `useReducer` | Complex state | Overkill for single boolean |
| `useEffect` | Sync with external systems | Missing deps; missing cleanup |
| `useLayoutEffect` | DOM measure before paint | Blocks paint — use sparingly |
| `useRef` | Mutable box, DOM ref | Changing `.current` doesn't re-render |
| `useMemo` | Cache computation | Empty deps wrong → stale data |
| `useCallback` | Stable function ref | Pointless without memo child |
| `useContext` | Read context | Re-renders on any value change |
| `useId` | Stable SSR-safe IDs | Pair label + input |
| `useImperativeHandle` | Customize ref API | Rare; prefer declarative |

---

## Stale Closure in useEffect

```typescript
// Bug: count always logs 0
useEffect(() => {
  const id = setInterval(() => console.log(count), 1000);
  return () => clearInterval(id);
}, []); // missing count

// Fix: add count to deps OR use functional ref pattern
```

**Interview answer:** "Effects close over render values. Exhaustive deps or refs for mutable latest value."

---

## Custom Hooks

Extract **stateful logic**, not JSX. Prefix `use`. Can compose other hooks.

Examples: `useDebounce`, `useLocalStorage`, `useMediaQuery`, `useChatStream`.

---

## Anti-Patterns

| Anti-pattern | Instead |
|--------------|---------|
| useEffect to derive state from props | Calculate during render |
| useEffect for event handlers | Put logic in handler |
| Custom hook that returns JSX only | Keep hook logic-only |

---

## Interview Script

> "Hooks attach state and effects to fibers by call order — that's the rules constraint. useEffect is for synchronizing with systems outside React: subscriptions, timers, manual DOM. I include cleanup and AbortController for fetches. For derived data I compute in render; for expensive derived data useMemo with correct deps. Custom hooks share logic across components — my streaming chat uses useChatStream wrapping fetch and abort."

---

## Related Questions

- [Q10 useEffect dependencies](../03-classic-react/questions/Q10-useeffect-dependencies-stale-closure.md)
- [Q11 Custom hooks design](../03-classic-react/questions/Q11-custom-hooks-design.md)

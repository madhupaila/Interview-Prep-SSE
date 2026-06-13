# Performance Optimization

Senior engineers **profile first**, optimize second.

---

## When to Optimize

1. User reports jank / Lighthouse flag
2. React DevTools Profiler shows hot components
3. Long lists or heavy charts

**Not** on first render of a simple form.

---

## Toolkit

| Technique | When |
|-----------|------|
| `React.memo` | Pure child, expensive render, stable props |
| `useMemo` | Expensive filter/sort on large array |
| `useCallback` | Callback passed to memoized child |
| Code splitting | Route-level `React.lazy` |
| Virtualization | Lists > ~100 visible rows |
| `startTransition` | Non-urgent filter while typing |
| Web Workers | Heavy CPU off main thread (rare in typical CRUD) |

---

## memo Broken? Check Props

```typescript
// Parent creates new object every render → memo useless
<Child style={{ color: 'red' }} />

// Fix: stable reference or pass primitive
const style = useMemo(() => ({ color: 'red' }), []);
```

---

## Bundle Size

- Analyze with `vite-bundle-visualizer` / webpack analyzer
- Lazy load routes and heavy libs (markdown editor, charts)
- Tree-shake lodash → `lodash-es` or per-function imports

---

## Interview Script

> "I'd profile with React DevTools before adding memo. For a 10k-row table I'd virtualize with TanStack Virtual. For route-based apps I'd lazy-load dashboards. useMemo caches derived sort — useCallback stabilizes handlers for memoized rows. I'd avoid premature optimization on forms with five fields. For Concurrent React, startTransition keeps input responsive while filtering a large client list."

---

## Related Questions

- [Q20 React.memo useMemo useCallback](../03-classic-react/questions/Q20-react-memo-usememo-usecallback.md)
- [Q21 Virtualize long list](../03-classic-react/questions/Q21-virtualize-long-list.md)

# How to Explain React in Interviews

Interviewers score **clarity of mental model**, not memorized API lists. Use this narration template.

---

## The Universal Opening (15 seconds)

> "I'll start with the user-facing behavior, then where state lives, then how React schedules updates and what re-renders. I'll call out loading, error, and accessibility before we go deep."

---

## Explain Like a Senior: Core Topics

### Rendering & Reconciliation

> "When state changes, React creates a new element tree and diffs it against the previous fiber tree. For lists, **keys** tell React which items moved vs were added/removed — wrong keys cause bugs and lost local state. The render phase is pure; commits apply DOM updates."

**Diagram verbally:** Parent state change → child re-renders unless memoized with stable props.

### State: Local vs Global vs Server

> "**Local state** for UI that dies with the component — modal open, input value. **Context** for low-churn global data — theme, auth user snapshot — but not high-frequency updates. **Server state** belongs in TanStack Query or similar — cache, dedupe, stale-while-revalidate. **Client global** (Zustand/Redux) when many distant components need the same client-only state with middleware."

### Hooks Rules

> "Hooks run in call order every render — that's why they can't be conditional. Effects run **after** paint; use them for subscriptions, DOM sync, and fetch orchestration — though I prefer data libraries for fetch. useLayoutEffect runs before paint when I need to measure DOM to avoid flicker."

### Performance

> "Don't memoize prematurely. Profile first. When needed: **React.memo** for expensive pure children, **useMemo** for expensive derived data, **useCallback** for stable function refs passed to memoized children. For long lists, **virtualization**. For routes, **lazy + Suspense**."

### Error Handling

> "Error boundaries catch render errors in children — not event handlers or async. I'd wrap route segments or feature panels. Async errors go in try/catch or query error state."

---

## GenAI / LLM UI Narration

> "Streaming responses use **fetch with ReadableStream** or **EventSource** for SSE. I append tokens to message state incrementally, use **AbortController** for stop generation, and debounce markdown rendering for long outputs. I show citation chips from RAG metadata and disable send while streaming to prevent duplicate requests."

---

## Phrases That Signal Seniority

| Say this | Not this |
|----------|----------|
| "Colocate state until you need to lift" | "Always use Redux" |
| "Stale-while-revalidate for dashboards" | "Fetch in useEffect every time" |
| "Keys must be stable IDs, not index" | "Index is fine for static lists" |
| "Focus management on modal open" | "Modal just works" |
| "Abort in-flight stream on unmount" | "Ignore cleanup" |

---

## When Stuck: Pivot Template

> "I'd validate with React DevTools Profiler and the Network tab. For this constraint, I'd trade X for Y — e.g. simpler state shape vs fewer re-renders."

---

## Related

- [React Round Flow](01-react-round-flow.md)
- [Memory Map Master](../01-core-concepts/memory-map-master.md)

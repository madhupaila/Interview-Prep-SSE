# Decision Picker — What Hook, Pattern, or Library When?

**Print this page.** Use in every interview when choosing an approach.

---

## State Location

| Need | Use | Avoid when |
|------|-----|------------|
| Single component UI | `useState` | Shared across many trees |
| Related fields / transitions | `useReducer` | Simple boolean toggle |
| Low-frequency global (theme, locale) | Context | High-frequency updates (cursor position) |
| Many components, client-only | Zustand / Jotai | Simple parent-child pass |
| Complex app + middleware + time-travel | Redux Toolkit | Small app / MVP |
| Server/API cache | TanStack Query / SWR | Duplicating cache in useState |
| URL as state | React Router search params | Sensitive data in URL |

---

## Data Fetching

| Need | Use |
|------|-----|
| Simple one-off fetch | TanStack Query `useQuery` |
| Mutations + invalidate | `useMutation` + `queryClient.invalidateQueries` |
| Infinite scroll | `useInfiniteQuery` |
| Optimistic update | `onMutate` + rollback in mutation |
| Real-time push | WebSocket + query cache update OR SSE |
| LLM streaming | `fetch` + ReadableStream / EventSource + local message state |

---

## Performance

| Symptom | Fix |
|---------|-----|
| Expensive child re-renders | `React.memo` + stable props |
| Expensive calculation | `useMemo` |
| Unstable callback breaking memo | `useCallback` |
| Long list | `react-window` / `@tanstack/react-virtual` |
| Large bundle | `React.lazy` + `Suspense` + route split |
| Layout thrash | `useLayoutEffect` for measure-then-set |

---

## Component Patterns

| Need | Pattern |
|------|---------|
| Shared logic | Custom hook |
| Cross-cutting UI | Composition (children) |
| Flexible API | Compound components |
| Inject behavior | Render props (legacy) / hooks (preferred) |
| Modal / tooltip / dropdown | Portal + focus trap |
| Form with validation | React Hook Form + Zod |
| Controlled vs uncontrolled | Controlled for instant validation; uncontrolled for simple file inputs |

---

## Effects

| Need | Hook |
|------|------|
| Subscribe / DOM / sync external | `useEffect` |
| Measure DOM before paint | `useLayoutEffect` |
| Event handler logic | Handler function — NOT effect |
| Derived from props/state | Calculate during render — NOT effect |
| Stable ref to value | `useRef` |
| Expose imperative handle | `useImperativeHandle` |

---

## GenAI UI Components

| Feature | Approach |
|---------|----------|
| Chat message list | Virtualized list if >100 messages |
| Streaming text | Append to string state; `flushSync` only if needed |
| Markdown + code | `react-markdown` + `remark-gfm` + sanitize |
| Syntax highlight | `react-syntax-highlighter` or Shiki |
| Stop generation | `AbortController` passed to fetch |
| Citations | Chips from message metadata array |
| Auto-scroll | `useEffect` on messages + "stick to bottom" flag |
| Prompt input | Textarea + Enter submit + Shift+Enter newline |

---

## Testing

| Test | Tool |
|------|------|
| User behavior | React Testing Library |
| Hooks in isolation | `@testing-library/react` `renderHook` |
| API mock | MSW |
| E2E | Playwright / Cypress |

---

## Quick Interview Line

> "I'll colocate state, use TanStack Query for server data, Context only for theme, memo only if Profiler shows a problem, and for streaming I'll use AbortController with incremental state updates."

---

## Related

- [Memory Map Master](../01-core-concepts/memory-map-master.md)
- [State Management](../01-core-concepts/state-management.md)

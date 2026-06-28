# Data Fetching & Caching

Server state is **not** the same as React state.

---

## TanStack Query (Recommended Default)

| Concept | Meaning |
|---------|---------|
| `queryKey` | Cache identity `['users', userId]` |
| `staleTime` | How long data is fresh without refetch |
| `gcTime` | Cache retention after unused |
| `enabled` | Conditional fetch |
| `placeholderData` | Show old while loading new |

---

## Patterns

| Pattern | Implementation |
|---------|----------------|
| Parallel queries | Multiple `useQuery` in component |
| Dependent query | `enabled: !!userId` on second query |
| Mutation | `useMutation` + `onSuccess` invalidate |
| Optimistic update | `onMutate` snapshot + rollback `onError` |
| Pagination | `useInfiniteQuery` + fetchNextPage |
| Prefetch | `queryClient.prefetchQuery` on hover |

---

## useEffect + fetch (When Discussed)

Acceptable for learning; in production prefer Query for dedupe/cache/retry.

Must include: **AbortController**, loading/error state, avoid setState on unmounted component.

---

## Interview Script

> "Server state belongs in TanStack Query — it handles caching, deduplication, background refetch, and retry. I key queries by entity and ID. Mutations invalidate related lists. For optimistic likes I use onMutate with rollback. I avoid storing API responses in useState at root — that duplicates cache and misses stale-while-revalidate. For SSR with Next.js App Router, I prefetch on server and hydrate with dehydrate."

---

## Related Questions

- [Q21 TanStack Query vs useEffect](../03-classic-react/questions/Q21-tanstack-query-vs-useeffect.md)
- [Q22 Optimistic updates](../03-classic-react/questions/Q22-optimistic-updates-mutation.md)

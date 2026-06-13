# React Memory Map — Flashcards (Trigger → Answer)

**How to use:** Cover the Answer column. Read Trigger aloud. Answer in **one sentence**. Check. Mark misses for tomorrow's drill.

---

## Z1 — Render (TRAC)

| # | Trigger | Answer |
|---|---------|--------|
| 1 | What is Virtual DOM? | Reconciliation diff — minimal DOM updates, not full replace each render. |
| 2 | Why keys in lists? | Stable identity for reconciler; index keys break on reorder/filter. |
| 3 | What causes re-render? | Own state/reducer, parent re-render, context value change — not ref.current. |
| 4 | What is Fiber? | Unit of work enabling interruptible/concurrent rendering. |
| 5 | Render vs commit? | Render is pure diff; commit applies DOM + runs layout effects. |
| 6 | useEffect vs useLayoutEffect? | Layout before paint (measure DOM); effect after paint (fetch/subscribe). |
| 7 | React 18 batching? | Multiple setStates batch into one render — including in promises. |
| 8 | startTransition? | Mark update low-priority so typing stays responsive. |

---

## Z2 — State (LOCUS)

| # | Trigger | Answer |
|---|---------|--------|
| 9 | Where to put state? | Colocate locally; lift to parent if siblings need it; Query for server. |
| 10 | useState vs useReducer? | Reducer when multiple related fields or explicit transitions. |
| 11 | Context performance? | All consumers re-render — split contexts, memo value, or use Zustand. |
| 12 | Redux vs Zustand? | Zustand simpler; Redux for middleware/time-travel; neither for server cache. |
| 13 | Server state in useState? | Anti-pattern — use TanStack Query cache instead. |
| 14 | URL as state? | searchParams for shareable filters/tabs — not secrets. |
| 15 | Prop drilling OK? | Yes for 1–2 levels; Context/store when wide or high-churn. |

---

## Z3 — Hooks (REFUSE)

| # | Trigger | Answer |
|---|---------|--------|
| 16 | Rules of hooks? | Top level only; same order every render — React indexes by call order. |
| 17 | Stale closure in effect? | Missing deps — add them, functional setState, or ref for latest. |
| 18 | Derived state in effect? | Wrong — compute during render or useMemo. |
| 19 | useRef vs useState? | Ref change doesn't re-render; state does. |
| 20 | Custom hooks? | Extract stateful logic; prefix use; return data/actions not JSX. |
| 21 | Strict Mode double effect? | Dev-only remount to expose missing cleanup — fix abort/cleanup. |
| 22 | eslint exhaustive-deps? | Follow it — deps list is the contract for effect freshness. |

---

## Z4 — Data (QUERY)

| # | Trigger | Answer |
|---|---------|--------|
| 23 | Fetch on mount? | useQuery with queryKey — dedupe, cache, retry, staleTime. |
| 24 | POST then refresh list? | useMutation + invalidateQueries on success. |
| 25 | Optimistic like button? | onMutate patch cache; onError rollback snapshot. |
| 26 | Infinite scroll data? | useInfiniteQuery + IntersectionObserver sentinel. |
| 27 | useEffect fetch problems? | No cache, race conditions, duplicate fetch — prefer Query. |
| 28 | WebSocket updates? | Subscribe in effect; update Query cache; cleanup close. |

---

## Z5 — Performance (VAMP)

| # | Trigger | Answer |
|---|---------|--------|
| 29 | React.memo not working? | Unstable props — new object/function reference each parent render. |
| 30 | useMemo vs useCallback? | Memo caches value; callback stabilizes function for memo children. |
| 31 | 10k row table slow? | Virtualize with TanStack Virtual — don't render all DOM nodes. |
| 32 | Large bundle? | Route-level React.lazy + Suspense; analyze bundle. |
| 33 | Premature optimization? | Profile first — don't memo every component. |
| 34 | Inline arrow in JSX? | New function each render — breaks memoized child. |

---

## Z6 — Product (SCREAM)

| # | Trigger | Answer |
|---|---------|--------|
| 35 | Error boundary catches? | Render errors in children — not events, async, or SSR alone. |
| 36 | Modal a11y? | Portal, focus trap, Esc close, restore focus, aria-modal. |
| 37 | Controlled vs uncontrolled? | Controlled for validation; uncontrolled OK for simple/file inputs. |
| 38 | Forms at scale? | React Hook Form + Zod schema; disable submit while pending. |
| 39 | XSS from LLM HTML? | Sanitize — react-markdown + rehype-sanitize, never raw innerHTML. |
| 40 | Test React how? | RTL getByRole + userEvent; MSW for API; behavior not implementation. |
| 41 | TypeScript UI states? | Discriminated union on status — impossible states don't compile. |
| 42 | Next.js Server Component? | Server default — no hooks; 'use client' for interactivity. |

---

## Z7 — GenAI (STREAM)

| # | Trigger | Answer |
|---|---------|--------|
| 43 | Streaming chat transport? | fetch POST + ReadableStream or SSE; not polling. |
| 44 | Stop generation? | AbortController.abort() on active fetch; handle AbortError. |
| 45 | Message state shape? | id, role, content, status enum: sending/streaming/complete/error/aborted. |
| 46 | Markdown from model? | react-markdown + sanitize — models output untrusted content. |
| 47 | RAG citations UI? | Citation chips + source drawer; empty retrieval = refuse UI. |
| 48 | Optimistic user send? | Append user bubble immediately; rollback/retry on error. |
| 49 | Rate limit 429 UI? | Show Retry-After countdown; disable send until window. |
| 50 | a11y streaming chat? | role=log aria-live=polite; don't assertive every token. |

---

## Mixed — Route the question (advanced)

| Question | Zone | Mnemonic |
|----------|------|----------|
| "Design Notion editor" | Z6 + Z5 | Block model + virtualize |
| "ChatGPT clone" | Z7 | STREAM + message array |
| "Dashboard slow" | Z5 + Z4 | Query staleTime + memo + virtualize |
| "Auth + protected routes" | Z2 + Z6 | Query session + redirect guard |
| "Real-time stock ticker" | Z4 | WebSocket + Query cache update |

---

## Drill scorecard

| Session date | Cards /50 | Misses | Review files |
|--------------|-----------|--------|--------------|
| | | | |

**Target:** 45/50 consistently before scheduling interviews.

---

## Related

- [Structured preparation guide](../00-interview-framework/05-structured-preparation-and-memory-mapping.md)
- [Master memory map](memory-map-master.md)

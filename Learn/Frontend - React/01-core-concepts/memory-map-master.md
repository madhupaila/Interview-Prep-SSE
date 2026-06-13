# Master Memory Map — React (Senior Interview)

**Print this page.** One-glance reference — maps every common question to a concept slot.

> **New to memory mapping?** Start with [Structured Preparation & Memory Mapping](../00-interview-framework/05-structured-preparation-and-memory-mapping.md) — then use this as your reference poster.
>
> **Daily drill:** [Flashcards (50 triggers)](memory-map-flashcards.md) | **One-page poster:** [visual one-page](memory-map-visual-one-page.md)

---

## The 7 Zones (File Every Question Here)

| Zone | Mnemonic | Covers |
|------|----------|--------|
| **Z1 Render** | **TRAC** | Virtual DOM, keys, fiber, batching, concurrent |
| **Z2 State** | **LOCUS** | useState, lift, Context, URL, Query/Zustand/Redux |
| **Z3 Hooks** | **REFUSE** | Rules, effects, refs, reducer, memoization |
| **Z4 Data** | **QUERY** | TanStack Query, mutations, optimistic, infinite |
| **Z5 Perf** | **VAMP** | Virtualize, avoid inline props, memo, lazy split |
| **Z6 Product** | **SCREAM** | State, composition, render, errors, a11y, measure |
| **Z7 GenAI** | **STREAM** | Chat stream, abort, sanitize, citations, tokens |

---

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SENIOR REACT MEMORY MAP (Z1–Z7)                          │
├─────────────────────────────────────────────────────────────────────────────┤
│ ANSWER FLOW (MEMOP)                                                         │
│   Mental model → Options → My pick → Outline → Pitfalls                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ Z1 RENDER [TRAC]                                                            │
│   Trigger → Render (pure) → reconcile (diff) → Commit (DOM)                   │
│   → useLayoutEffect → Paint → useEffect                                     │
│   Keys = identity │ Fiber = interruptible work                              │
├─────────────────────────────────────────────────────────────────────────────┤
│ Z2 STATE [LOCUS]                                                            │
│   Local useState │ Lift parent │ Context (low churn) │ URL params             │
│   Server cache = TanStack Query │ Client global = Zustand/Redux             │
│   Rule: colocate until lift required                                        │
├─────────────────────────────────────────────────────────────────────────────┤
│ Z3 HOOKS [REFUSE]                                                           │
│   Rules: top-level, same order every render                                 │
│   useEffect = after paint + cleanup │ useLayoutEffect = before paint        │
│   useRef = mutable, no re-render │ useMemo/useCallback = after profile      │
├─────────────────────────────────────────────────────────────────────────────┤
│ Z4 DATA [QUERY]                                                             │
│   queryKey │ staleTime │ invalidateQueries │ useMutation optimistic         │
│   Anti-pattern: bare fetch in useEffect without abort/cache                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ Z5 PERF [VAMP]                                                              │
│   Virtualize long lists │ Avoid inline object/function props                │
│   Memo after Profiler │ lazy + Suspense per route                           │
├─────────────────────────────────────────────────────────────────────────────┤
│ Z6 PRODUCT [SCREAM]                                                         │
│   State colocate │ Composition │ Render pure │ Error boundary               │
│   A11y roles/keyboard │ Measure before optimize                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ Z7 GENAI [STREAM] — full map: genai-react/memory-map-genai-react.md         │
│   fetch stream │ AbortController │ sanitize markdown │ citation UI          │
│   message.status: sending|streaming|complete|error|aborted                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ TESTING          RTL getByRole + userEvent │ MSW │ behavior not impl detail │
│ TYPESCRIPT       Props interface │ discriminated union UI states            │
│ SECURITY         Sanitize LLM HTML │ CSP │ no secrets in bundle             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## TRAC — Render pipeline (Z1) — memorize first

| Step | Letter | Meaning |
|------|--------|---------|
| 1 | **T** | **Trigger** — setState, parent render, context |
| 2 | **R** | **Render** — pure, returns elements |
| 3 | **A** | **reconcile** — diff fibers, keys identify lists |
| 4 | **C** | **Commit** — DOM update, then effects |

---

## LOCUS — State placement (Z2)

| Letter | When | Tool |
|--------|------|------|
| **L** | Single component UI | `useState` / `useReducer` |
| **O** | Siblings need same data | Lift to parent |
| **C** | App-wide, rarely changes | Context |
| **U** | Shareable navigation state | URL searchParams |
| **S** | API / server data | TanStack Query |

---

## Concept → Zone → Question Map

| If they ask about… | Zone | Quick answer | Question |
|--------------------|------|--------------|----------|
| Virtual DOM | Z1 | Reconcile, not replace | [Q01](../03-classic-react/questions/Q01-virtual-dom-reconciliation.md) |
| Keys in lists | Z1 | Stable ID, not index | [Q02](../03-classic-react/questions/Q02-react-keys-lists.md) |
| Re-render triggers | Z1 | State, parent, context | [Q03](../03-classic-react/questions/Q03-rerender-triggers.md) |
| Where to put state | Z2 | LOCUS decision tree | [Q08](../03-classic-react/questions/Q08-prop-drilling-solutions.md) |
| Context slow | Z2 | Split + memo | [Q07](../03-classic-react/questions/Q07-context-performance.md) |
| useEffect deps | Z3 | Stale closure + cleanup | [Q10](../03-classic-react/questions/Q10-useeffect-dependencies-stale-closure.md) |
| Custom hooks | Z3 | Logic only, prefix use | [Q11](../03-classic-react/questions/Q11-custom-hooks-design.md) |
| Fetch data | Z4 | TanStack Query | [Q21](../03-classic-react/questions/Q21-tanstack-query-vs-useeffect.md) |
| Optimistic UI | Z4 | onMutate rollback | [Q22](../03-classic-react/questions/Q22-optimistic-updates-mutation.md) |
| memo not working | Z5 | Unstable props | [Q14](../03-classic-react/questions/Q14-react-memo-usememo-usecallback.md) |
| Long list slow | Z5 | Virtualize | [Q20](../03-classic-react/questions/Q20-virtualize-long-list.md) |
| Error boundary | Z6 | Render errors only | [Q16](../03-classic-react/questions/Q16-error-boundaries-when-how.md) |
| Modal a11y | Z6 | Portal + focus trap | [Q17](../03-classic-react/questions/Q17-portal-modal-focus-trap.md) |
| Streaming chat | Z7 | STREAM | [Q01 GenAI](../02-genai-llm-react/questions/Q01-build-streaming-chat-ui.md) |
| RAG citations | Z7 | Source panel | [Q04 GenAI](../02-genai-llm-react/questions/Q04-rag-citation-source-panel.md) |

---

## SCREAM — Senior product checklist (Z6)

- **S**tate where it's used
- **C**omposition over prop drilling
- **R**ender pure; effects for sync
- **E**rrors: boundary + query error UI
- **A**11y: roles, labels, keyboard
- **M**easure before memoizing

---

## Confidence levels (self-assess)

| Level | You can… |
|-------|----------|
| **L0** | Read concepts but can't speak without notes |
| **L1** | Recite TRAC + LOCUS from memory |
| **L2** | Route any question to zone in <5 sec |
| **L3** | MEMOP answer + code sketch without opening files |
| **L4** | 45-min mock: concept + live build + tradeoffs |

**Target for interviews:** **L3** minimum on Z1–Z6, **L2** on Z7 if GenAI role.

---

## Related

- [Structured preparation (start here)](../00-interview-framework/05-structured-preparation-and-memory-mapping.md)
- [Flashcards](memory-map-flashcards.md)
- [One-page poster](memory-map-visual-one-page.md)
- [Decision Picker](../00-interview-framework/04-decision-picker.md)
- [GenAI Memory Map](../02-genai-llm-react/memory-map-genai-react.md)

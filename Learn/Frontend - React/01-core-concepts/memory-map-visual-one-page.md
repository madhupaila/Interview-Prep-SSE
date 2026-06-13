# React Memory Map — One Page Poster

**Print this. Tape it near your desk. Recite once each morning.**

---

```
╔══════════════════════════════════════════════════════════════════════════════╗
║                     REACT INTERVIEW — ONE PAGE MEMORY MAP                   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  ANSWER FLOW:  M mental model → E options → M my pick → O outline → P pits   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Z1 RENDER [TRAC]                                                            ║
║    Trigger → Render pure → reconcile(diff+KEYS) → Commit → layout → effect   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Z2 STATE [LOCUS]                                                            ║
║    Local useState │ Lift parent │ Context low-churn │ URL params │ Query API ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Z3 HOOKS [REFUSE]                                                           ║
║    Rules top-level │ Effects after paint+cleanup │ Ref no re-render          ║
║    useState/Reducer │ Stable memo only after profile                         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Z4 DATA [QUERY]                                                             ║
║    TanStack Query: key, staleTime, invalidate, optimistic — NOT useEffect    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Z5 PERF [VAMP]                                                              ║
║    Virtualize lists │ Avoid inline props │ Memo after profile │ lazy Split   ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Z6 PRODUCT [SCREAM]                                                         ║
║    State colocate │ Composition │ Render pure │ Errors │ A11y │ Measure      ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  Z7 GENAI [STREAM]                                                           ║
║    Signal abort │ Token append │ Render sanitize │ Error │ A11y │ Msg status   ║
║    status: sending | streaming | complete | error | aborted                  ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  TOP TRADEOFFS (say aloud)                                                   ║
║    Context vs Zustand │ Query vs useEffect │ memo vs simplicity              ║
║    Controlled vs uncontrolled │ SSE vs WebSocket │ 301 vs client route       ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  SENIOR PHRASES                                                              ║
║    "I'd colocate state until lift is required."                              ║
║    "Server state belongs in Query, not useState."                            ║
║    "I'll profile before memoizing."                                          ║
║    "Streaming needs AbortController and sanitized markdown."                 ║
╚══════════════════════════════════════════════════════════════════════════════╝
```

---

## Zone router (10-second version)

| Hear… | Say zone… |
|-------|-----------|
| DOM, key, fiber, batch | **Z1 TRAC** |
| state, context, redux | **Z2 LOCUS** |
| effect, hook, closure | **Z3 REFUSE** |
| fetch, API, cache | **Z4 QUERY** |
| slow, memo, list | **Z5 VAMP** |
| modal, form, test | **Z6 SCREAM** |
| chat, stream, RAG | **Z7 STREAM** |

---

## 7-day mini bootcamp (confidence sprint)

| Day | Memorize | Drill |
|-----|----------|-------|
| 1 | TRAC | Draw pipeline 5× |
| 2 | LOCUS | Label state on 3 apps |
| 3 | REFUSE + QUERY | Flashcards #16–28 |
| 4 | VAMP + SCREAM | Flashcards #29–42 |
| 5 | STREAM | Explain chat UI 3 min |
| 6 | Full poster blank | From memory |
| 7 | Mock interview | 1 concept + 1 code |

---

## Related

- [Structured preparation](../00-interview-framework/05-structured-preparation-and-memory-mapping.md)
- [Flashcards](memory-map-flashcards.md)
- [Master map (expanded)](memory-map-master.md)

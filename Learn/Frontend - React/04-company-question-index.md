# Company × React Question Index

Lookup for **3–5 YOE → Senior SWE** React interviews. Read [Memory Map](01-core-concepts/memory-map-master.md) first, then drill into tagged questions.

---

## By Company

### Meta / Facebook
| Topic | Question |
|-------|----------|
| Reconciliation | [Q01 Virtual DOM](03-classic-react/questions/Q01-virtual-dom-reconciliation.md) |
| Keys | [Q02 Keys in lists](03-classic-react/questions/Q02-react-keys-lists.md) |
| Context perf | [Q07 Context performance](03-classic-react/questions/Q07-context-performance.md) |
| Memoization | [Q14 memo/useMemo/useCallback](03-classic-react/questions/Q14-react-memo-usememo-usecallback.md) |
| Fiber | [Q05 React Fiber](03-classic-react/questions/Q05-react-fiber-architecture.md) |
| Concurrent | [Q39 React 18 concurrent](03-classic-react/questions/Q39-react-18-concurrent-features.md) |
| News feed scale | [Q20 Virtualize list](03-classic-react/questions/Q20-virtualize-long-list.md) |

### Google
| Topic | Question |
|-------|----------|
| Re-render | [Q03 Re-render triggers](03-classic-react/questions/Q03-rerender-triggers.md) |
| Performance | [Q50 Core Web Vitals](03-classic-react/questions/Q50-performance-lighthouse-react.md) |
| Testing | [Q29 RTL best practices](03-classic-react/questions/Q29-testing-library-best-practices.md) |
| Next/RSC | [Q28 App Router RSC](03-classic-react/questions/Q28-nextjs-app-router-rsc.md) |
| Code split | [Q43 Code splitting](03-classic-react/questions/Q43-code-splitting-strategies.md) |

### Amazon / AWS
| Topic | Question |
|-------|----------|
| State / scale | [Q38 Redux vs Zustand](03-classic-react/questions/Q38-state-management-redux-zustand.md) |
| Forms | [Q25 RHF + Zod](03-classic-react/questions/Q25-forms-react-hook-form-zod.md) |
| Tables | [Q56 Data table](03-classic-react/questions/Q56-react-table-large-datasets.md) |
| Micro FE | [Q37 Micro frontends](03-classic-react/questions/Q37-micro-frontends-react.md) |

### OpenAI / Anthropic / GenAI
| Topic | Question |
|-------|----------|
| Streaming chat | [Q01 Build streaming chat](02-genai-llm-react/questions/Q01-build-streaming-chat-ui.md) |
| Stop / abort | [Q02 AbortController](02-genai-llm-react/questions/Q02-stop-generation-abortcontroller.md) |
| Markdown XSS | [Q03 Sanitize markdown](02-genai-llm-react/questions/Q03-markdown-render-llm-sanitize.md) |
| RAG citations | [Q04 Citation panel](02-genai-llm-react/questions/Q04-rag-citation-source-panel.md) |
| Agent tools | [Q16 Tool call UI](02-genai-llm-react/questions/Q16-agent-tool-call-ui.md) |
| Token budget | [Q08 Context warning](02-genai-llm-react/questions/Q08-token-budget-context-warning.md) |
| a11y chat | [Q20 Live regions](02-genai-llm-react/questions/Q20-accessible-ai-chat-live-region.md) |

### Stripe / Fintech
| Topic | Question |
|-------|----------|
| useEffect | [Q10 Stale closure](03-classic-react/questions/Q10-useeffect-dependencies-stale-closure.md) |
| TanStack Query | [Q21 Query vs useEffect](03-classic-react/questions/Q21-tanstack-query-vs-useeffect.md) |
| Optimistic UI | [Q22 Optimistic mutation](03-classic-react/questions/Q22-optimistic-updates-mutation.md) |
| Double submit | [Q26 Prevent double submit](03-classic-react/questions/Q26-prevent-double-form-submit.md) |
| Auth routes | [Q35 Protected routes](03-classic-react/questions/Q35-auth-protected-routes-react.md) |
| Rate limit AI | [Q10 Rate limit UI](02-genai-llm-react/questions/Q10-rate-limit-error-ui-llm.md) |

### Netflix / Spotify / Media
| Topic | Question |
|-------|----------|
| Virtualization | [Q20 Virtualize list](03-classic-react/questions/Q20-virtualize-long-list.md) |
| Infinite scroll | [Q23 Infinite scroll](03-classic-react/questions/Q23-infinite-scroll-pagination.md) |
| Lazy routes | [Q19 Suspense lazy](03-classic-react/questions/Q19-react-suspense-lazy.md) |
| Performance | [Q14 Memoization](03-classic-react/questions/Q14-react-memo-usememo-usecallback.md) |

### Shopify / E-commerce
| Topic | Question |
|-------|----------|
| Custom hooks | [Q11 Custom hooks](03-classic-react/questions/Q11-custom-hooks-design.md) |
| Design system | [Q36 Design system](03-classic-react/questions/Q36-design-system-architecture.md) |
| Forms | [Q25 RHF + Zod](03-classic-react/questions/Q25-forms-react-hook-form-zod.md) |
| i18n | [Q48 i18n](03-classic-react/questions/Q48-internationalization-react.md) |

### Microsoft / LinkedIn / Slack
| Topic | Question |
|-------|----------|
| Accessibility | [Q33 a11y patterns](03-classic-react/questions/Q33-accessibility-react-patterns.md) |
| Real-time | [Q24 WebSocket vs polling](03-classic-react/questions/Q24-websocket-vs-polling-react.md) |
| Modals | [Q17 Portal focus trap](03-classic-react/questions/Q17-portal-modal-focus-trap.md) |
| Thread history | [Q06 Conversation threads](02-genai-llm-react/questions/Q06-conversation-thread-history.md) |

### Vercel / Next.js ecosystem
| Topic | Question |
|-------|----------|
| RSC | [Q28 App Router](03-classic-react/questions/Q28-nextjs-app-router-rsc.md) |
| TanStack Query | [Q21 Query](03-classic-react/questions/Q21-tanstack-query-vs-useeffect.md) |
| Tailwind | [Q41 CSS architecture](03-classic-react/questions/Q41-css-in-js-vs-tailwind-react.md) |
| Streaming | [Q01 Chat UI](02-genai-llm-react/questions/Q01-build-streaming-chat-ui.md) |

---

## By Difficulty

| Easy | Medium | Hard |
|------|--------|------|
| Q02 Keys | Q04 Controlled | Q05 Fiber |
| Q03 Re-renders | Q06 useReducer | Q07 Context perf |
| Q09 Lift state | Q10 useEffect | Q14 Memo trio |
| Q13 useRef | Q11 Custom hooks | Q15 Compound |
| Q26 Double submit | Q17 Modal a11y | Q20 Virtualize |
| Q53 ESLint hooks | Q21 TanStack Query | Q28 RSC |
| | Q25 Forms | Q31 TS unions |
| | Q35 Auth | Q34 XSS |
| | GenAI Q02 Stop | Q60 System design |
| | GenAI Q07 Model | GenAI Q01 Chat build |

---

## Senior Loop (Recommended Mock Set)

1. [Q01 Virtual DOM](03-classic-react/questions/Q01-virtual-dom-reconciliation.md) — concepts warm-up  
2. [Q21 TanStack Query](03-classic-react/questions/Q21-tanstack-query-vs-useeffect.md) — architecture  
3. [Q01 Streaming chat](02-genai-llm-react/questions/Q01-build-streaming-chat-ui.md) — live build  
4. [Q60 Notion editor system design](03-classic-react/questions/Q60-senior-react-system-design-prompt.md) — senior capstone  

---

## Related

- [6-Week Study Plan](05-study-schedule/6-week-plan.md)
- [Decision Picker](00-interview-framework/04-decision-picker.md)

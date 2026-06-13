# Senior SWE Signals — React Interviews

What separates **Senior** from **Mid** in React rounds at Meta, Google, Stripe, OpenAI, etc.

---

## Senior Signals Checklist

| Signal | What it looks like |
|--------|-------------------|
| **Scope control** | MVP first; defers Redux/router complexity until needed |
| **Options + pick** | Names 2–3 approaches; chooses with tradeoffs |
| **Product awareness** | Loading, empty, error, offline, rate limits |
| **Accessibility** | Keyboard nav, labels, focus, live regions for chat |
| **Performance literacy** | Knows when NOT to memo; virtualizes lists |
| **Server vs client state** | Doesn't put API cache in useState |
| **TypeScript discipline** | Props interfaces, discriminated unions for UI states |
| **Testing strategy** | RTL for behavior; what to mock (router, query client) |
| **GenAI UX** | Streaming, stop, retry, citations, cost/token hints |
| **Security** | XSS in dangerouslySetInnerHTML, sanitizing markdown |

---

## Red Flags Interviewers Notice

- Mutating state directly
- useEffect for everything including derived state
- Index as key on dynamic lists
- Giant Context for frequently changing values
- No cleanup in useEffect (subscriptions, abort)
- "I'd use Redux" without justification
- Ignoring Strict Mode double-mount behavior in dev

---

## Full-Stack + GenAI Differentiator

For 3–5 YOE targeting Senior with LLM products:

1. **End-to-end story:** "API streams SSE → React parses chunks → markdown + citations → optimistic user message"
2. **Cost/latency UX:** token estimate, model selector, degraded mode when API slow
3. **Multi-tenancy UI:** org switcher, feature flags, RBAC-gated routes
4. **Observability:** log client errors to Sentry with session replay context

---

## Mock Grading Rubric (Self-Score)

| Score | Criteria |
|-------|----------|
| 5/5 | Mental model + options + code + edge cases + tradeoffs unprompted |
| 4/5 | Solid code; needs prompt for a11y or error states |
| 3/5 | Works but single approach; weak state placement |
| 2/5 | API trivia only; can't implement |
| 1/5 | Incorrect mental model (e.g. "Virtual DOM replaces DOM every time") |

---

## Related

- [Decision Picker](04-decision-picker.md)
- [GenAI React Memory Map](../02-genai-llm-react/memory-map-genai-react.md)

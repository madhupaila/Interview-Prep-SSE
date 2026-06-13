# GenAI React Framework — Interview Approach

How to discuss **building LLM products in React** at senior level.

---

## Typical Build Question

> "Design the frontend for a ChatGPT-like interface with streaming, history, and stop button."

### 6-Step Answer

1. **Clarify:** Multi-model? Citations? File upload? Mobile?
2. **Component tree:** Layout → ThreadList → ChatWindow → MessageList → Input
3. **State:** messages array; activeThreadId; streaming flag; abort ref
4. **API:** POST `/chat` returns SSE stream; or WebSocket for bi-directional
5. **Edge cases:** abort, retry, empty, rate limit, long markdown perf
6. **Tradeoffs:** SSE vs WebSocket; client vs server thread storage

---

## State Shape (TypeScript)

```typescript
type MessageStatus = 'sending' | 'streaming' | 'complete' | 'error' | 'aborted';

interface ChatMessage {
  id: string;
  role: 'user' | 'assistant' | 'system';
  content: string;
  status: MessageStatus;
  citations?: { title: string; url: string }[];
  createdAt: number;
}
```

---

## Architecture Layers

```
UI Components → Custom hooks (useChatStream) → API client → SSE/REST
                     ↓
              TanStack Query (thread list, persist)
```

---

## Senior Differentiators

- Token/cost estimate before send
- Model picker with latency hint
- PII warning before paste
- Session replay friendly error boundaries
- Feature flag for new model rollout

---

## Related

- [Streaming SSE Chat UI](streaming-sse-chat-ui.md)
- [RAG UI Patterns](rag-ui-patterns.md)
- [GenAI Questions](questions/)

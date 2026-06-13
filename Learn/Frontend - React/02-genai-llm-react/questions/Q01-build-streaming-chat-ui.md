# Build a Streaming ChatGPT-like UI

**Track:** Genai Llm React
**Companies:** OpenAI, Anthropic, Character.AI, Meta AI
**Difficulty:** Hard
**Case Study ID:** R-G-01

---

## Memory Hook

> **SSE/fetch stream + message state + Stop**

---

## What Interviewers Test

End-to-end GenAI chat shell

---

## Options / Approaches

| Option | Issue / note |
|--------|--------------|
| Poll for response | Bad latency |
| SSE/fetch stream | Standard |
| WebSocket | Bi-directional |

---

## Senior Pick

**Use:** fetch ReadableStream + AbortController

---

## Clarifying Questions (If Build / System Question)

| # | Question | Why it matters |
|---|----------|----------------|
| 1 | Mobile vs desktop? | Layout, virtual keyboard |
| 2 | SSR required? | Next.js vs SPA |
| 3 | Real-time / streaming? | SSE vs polling |
| 4 | Accessibility level? | WCAG, live regions |
| 5 | Error / offline behavior? | Degraded UX |

---

## Interview Answer Script (Speak Aloud)

> Clarify: multi-turn? file upload? model select?

> State: messages array with status enum.

> Optimistic user bubble.

> Stream append assistant content.

> Stop aborts fetch.

> Markdown render sanitized.

> aria-live for new tokens.

> **Tradeoff close:** "I'd validate with Profiler and RTL tests, and document the decision in a short ADR if this is a team-wide pattern."

---

## Code Sketch (TypeScript + React 18+)

```typescript
type MessageStatus = 'sending' | 'streaming' | 'complete' | 'error' | 'aborted';

interface ChatMessage {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  status: MessageStatus;
}

export function ChatPage() {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState('');
  const abortRef = useRef<AbortController | null>(null);

  const send = async () => {
    const userMsg: ChatMessage = {
      id: crypto.randomUUID(),
      role: 'user',
      content: input,
      status: 'complete',
    };
    const assistantId = crypto.randomUUID();
    setMessages((m) => [
      ...m,
      userMsg,
      { id: assistantId, role: 'assistant', content: '', status: 'streaming' },
    ]);
    setInput('');
    abortRef.current?.abort();
    abortRef.current = new AbortController();

    const res = await fetch('/api/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ prompt: userMsg.content }),
      signal: abortRef.current.signal,
    });
    const reader = res.body!.getReader();
    const decoder = new TextDecoder();
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      const chunk = decoder.decode(value, { stream: true });
      setMessages((m) =>
        m.map((msg) =>
          msg.id === assistantId ? { ...msg, content: msg.content + chunk } : msg
        )
      );
    }
    setMessages((m) =>
      m.map((msg) =>
        msg.id === assistantId ? { ...msg, status: 'complete' } : msg
      )
    );
  };

  const stop = () => {
    abortRef.current?.abort();
    setMessages((m) =>
      m.map((msg) =>
        msg.status === 'streaming' ? { ...msg, status: 'aborted' } : msg
      )
    );
  };

  return (
    <div>
      <div role="log" aria-live="polite" aria-relevant="additions">
        {messages.map((m) => (
          <div key={m.id}>{m.role}: {m.content}</div>
        ))}
      </div>
      <textarea value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={send} disabled={messages.some((m) => m.status === 'streaming')}>
        Send
      </button>
      <button onClick={stop}>Stop</button>
    </div>
  );
}
```

---

## Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Transport | Polling | SSE/stream | Stream |
| Stop | Ignore | AbortController | Abort |

---

## Follow-Up Questions

1. How handle reconnect?
2. Rate limit UI?
3. Thread persistence?

---

## How to Remember (Memory Mapping)

| Slot | Anchor |
|------|--------|
| Concept | End-to-end GenAI chat shell |
| Trigger word | Maps to [Master Memory Map](../../01-core-concepts/memory-map-master.md) section |
| Default pick | fetch ReadableStream + AbortController |
| Senior signal | Name options → pick → edge cases |

---

## Related

- [streaming-sse-chat-ui.md](../streaming-sse-chat-ui.md)
- [Decision Picker](../../00-interview-framework/04-decision-picker.md)
- [Master Memory Map](../../01-core-concepts/memory-map-master.md)

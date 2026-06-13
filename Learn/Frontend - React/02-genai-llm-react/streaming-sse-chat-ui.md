# Streaming & SSE Chat UI

Implementation patterns for **token-by-token** LLM responses.

---

## SSE vs fetch stream

| Approach | Pros | Cons |
|----------|------|------|
| **EventSource** | Simple SSE protocol | GET only; limited headers |
| **fetch + ReadableStream** | POST body, auth headers | Manual SSE parse |
| **WebSocket** | Bi-directional | More infra complexity |

**Senior pick:** `fetch` + stream for authenticated POST chat APIs (OpenAI-style).

---

## Core Hook Sketch

```typescript
function useChatStream() {
  const abortRef = useRef<AbortController | null>(null);

  const send = useCallback(async (prompt: string, onToken: (t: string) => void) => {
    abortRef.current?.abort();
    abortRef.current = new AbortController();
    const res = await fetch('/api/chat', {
      method: 'POST',
      body: JSON.stringify({ prompt }),
      signal: abortRef.current.signal,
      headers: { 'Content-Type': 'application/json' },
    });
    const reader = res.body!.getReader();
    const decoder = new TextDecoder();
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      onToken(decoder.decode(value, { stream: true }));
    }
  }, []);

  const stop = useCallback(() => abortRef.current?.abort(), []);
  return { send, stop };
}
```

---

## UI States

| State | UI |
|-------|-----|
| Idle | Input enabled |
| Sending | User bubble + disabled send |
| Streaming | Assistant bubble growing + Stop button |
| Complete | Copy, feedback, re-enable input |
| Error | Retry + message preserved |
| Aborted | Partial content + "Stopped" label |

---

## Performance

- Batch token updates with `requestAnimationFrame` or 16ms throttle for huge streams
- `startTransition` for markdown re-parse
- Virtualize message list > 100 items

---

## Interview Script

> "I POST the prompt and read the response body as a stream with AbortController for stop. I append tokens to the assistant message immutably. On unmount I abort. I sanitize markdown before render. For accessibility I use aria-live polite so screen readers get new content without stealing focus. I disable send during stream to prevent duplicate requests."

---

## Related Questions

- [Q01 Build streaming chat UI](../02-genai-llm-react/questions/Q01-build-streaming-chat-ui.md)
- [Q02 Stop generation abort](../02-genai-llm-react/questions/Q02-stop-generation-abortcontroller.md)

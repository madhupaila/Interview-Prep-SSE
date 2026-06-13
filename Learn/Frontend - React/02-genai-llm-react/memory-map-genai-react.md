# GenAI React Memory Map

**Print this page.** LLM product UI patterns for senior full-stack interviews.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    GENAI / LLM REACT MEMORY MAP                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ CHAT SHELL                                                                  │
│   MessageList (virtualized) │ MessageBubble user/assistant │ InputBar       │
│   StreamingIndicator │ StopButton │ Retry │ Copy │ Feedback thumbs          │
├─────────────────────────────────────────────────────────────────────────────┤
│ STREAMING                                                                   │
│   fetch + ReadableStream OR EventSource (SSE)                               │
│   Parse SSE: data: {"token":"..."} │ Append to assistant message state      │
│   AbortController on Stop / unmount │ Disable send while streaming          │
├─────────────────────────────────────────────────────────────────────────────┤
│ MARKDOWN & CODE                                                             │
│   react-markdown + remark-gfm │ rehype-sanitize (XSS)                       │
│   Code blocks: Shiki / syntax-highlighter │ Copy button                     │
│   Defer heavy render: startTransition for long streams                      │
├─────────────────────────────────────────────────────────────────────────────┤
│ RAG UI                                                                      │
│   Citation chips [1][2] │ Source panel sidebar │ Highlight retrieved chunk  │
│   "No sources" empty state │ Confidence / refuse UI                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ CONVERSATION MEMORY                                                         │
│   Thread list │ persist threadId in URL │ truncate context UX warning       │
│   Token budget bar │ model selector (cost/latency tradeoff)                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ OPTIMISTIC UX                                                               │
│   User message instant │ Assistant placeholder "Thinking…" then stream      │
│   Rollback on error │ Toast + retry                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ A11Y                                                                        │
│   role="log" aria-live="polite" for new assistant text                      │
│   Focus input after send │ Keyboard shortcuts                               │
├─────────────────────────────────────────────────────────────────────────────┤
│ STATE SHAPE                                                                 │
│   messages: { id, role, content, status, citations?, createdAt }[]        │
│   status: sending | streaming | complete | error | aborted                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ PRODUCT REFERENCES                                                          │
│   ChatGPT: stream + stop │ Claude: artifacts │ Copilot: inline ghost text   │
│   Notion AI: selection context │ Perplexity: citation-first layout           │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Hook: `useChatStream` Mnemonic **STREAM**

- **S**tart fetch with signal
- **T**oken append to buffer
- **R**ender markdown sanitized
- **E**rror / abort handling
- **A**11y live region
- **M**essage state immutable updates

## Related

- [GenAI React Framework](00-genai-react-framework.md)
- [Streaming SSE Chat UI](streaming-sse-chat-ui.md)

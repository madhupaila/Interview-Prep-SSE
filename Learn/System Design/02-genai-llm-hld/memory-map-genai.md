# Gen AI Memory Map

**Print this page.** One-glance reference for LLM HLD interviews.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    GEN AI / LLM MEMORY MAP                              │
├─────────────────────────────────────────────────────────────────────────┤
│ FOUR LAYERS                                                             │
│   Ingestion → Retrieval → Inference → Safety/Ops                        │
├─────────────────────────────────────────────────────────────────────────┤
│ RAG PIPELINE                                                            │
│   Upload → Parse → Chunk(512tok,10%overlap) → Embed → VectorDB          │
│   Query: embed → hybrid search → rerank(top5) → prompt → LLM → cite     │
├─────────────────────────────────────────────────────────────────────────┤
│ CHUNKING                                                                │
│   Fixed | Semantic | Parent-child │ Code: AST per function              │
├─────────────────────────────────────────────────────────────────────────┤
│ RETRIEVAL                                                               │
│   Vector (semantic) + BM25 (keyword) = hybrid │ Metadata filter (tenant)│
│   Reranker: 20 → 5 chunks │ Low score → "I don't know"                  │
├─────────────────────────────────────────────────────────────────────────┤
│ INFERENCE                                                               │
│   LLM Gateway: auth, rate limit, router, stream SSE                     │
│   TTFT < 500ms │ Self-host vLLM if > 50M tokens/mo                      │
│   Model router: small (FAQ) vs large (complex)                          │
├─────────────────────────────────────────────────────────────────────────┤
│ AGENTS                                                                  │
│   Loop: plan → tool_call → execute → observe │ max_steps=10             │
│   Sandbox tools │ JSON schema validation │ supervisor pattern           │
├─────────────────────────────────────────────────────────────────────────┤
│ SAFETY                                                                  │
│   Input: PII redact, prompt injection │ Output: toxicity, cite check    │
├─────────────────────────────────────────────────────────────────────────┤
│ EVAL & COST                                                             │
│   Golden set regression │ LLM-as-judge │ A/B models                       │
│   Cache: semantic + prompt prefix │ Route to cheap model                │
├─────────────────────────────────────────────────────────────────────────┤
│ STORAGE ESTIMATE                                                        │
│   100M chunks × 6KB vector ≈ 600GB │ Embeddings: batch on ingest        │
├─────────────────────────────────────────────────────────────────────────┤
│ RAG vs FINE-TUNE vs PROMPT                                              │
│   RAG: dynamic knowledge │ Fine-tune: style/format │ Prompt: quick MVP  │
└─────────────────────────────────────────────────────────────────────────┘
```

## Component Quick Pick

| Need | Pick |
|------|------|
| Vector search at scale | Pinecone |
| Already on Postgres | pgvector |
| LLM MVP | OpenAI API |
| LLM scale / privacy | vLLM self-host |
| Hybrid search | Elasticsearch + vector |
| Agent workflows | Custom orchestrator + tool registry |
| Streaming UX | SSE |

## Diagram: Query Path

```
User → API → Retriever → Reranker → LLM Gateway → Guardrails → SSE stream
                  ↑
              VectorDB
```

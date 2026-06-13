# LLM Inference & Serving

How to serve LLMs at scale in production.

---

## Serving Options

| Option | Latency | Cost | Ops |
|--------|---------|------|-----|
| OpenAI/Anthropic API | Low (managed) | Per-token | None |
| vLLM (self-host) | Tunable | GPU hourly | High |
| TGI (Hugging Face) | Tunable | GPU hourly | Medium |
| AWS Bedrock / Azure OpenAI | Low | Per-token | Low |

**Break-even:** Self-host often wins at > 50–100M tokens/month depending on model size.

---

## vLLM Key Concepts

- **PagedAttention:** Efficient KV cache memory management
- **Continuous batching:** Batch requests dynamically for GPU utilization
- **Tensor parallelism:** Split large models across GPUs

---

## LLM Gateway Responsibilities

```
Client → LLM Gateway → [Router] → Model instances
                │
                ├── Rate limiting (per user/tenant)
                ├── Auth & API keys
                ├── Request/response logging
                ├── Token counting & billing
                ├── Semantic cache lookup
                ├── Fallback model on timeout
                └── Stream aggregation (SSE)
```

---

## Streaming (SSE)

- Return tokens as generated — improves perceived latency
- Client: EventSource or fetch with ReadableStream
- **Time to first token (TTFT)** is key UX metric

---

## Model Routing

| Query signal | Route to |
|--------------|----------|
| Classifier: simple FAQ | Small model (Haiku, GPT-4o-mini) |
| Complex reasoning | Large model (Opus, GPT-4) |
| Code | Code-specialized model |
| Low retrieval confidence | Escalate or refuse |

**Router:** Lightweight classifier or heuristic on query length/intent.

---

## Context Window Management

- Max tokens: model limit (8K–200K+)
- Budget: system prompt + retrieved chunks + history + user query
- **Summarization:** Compress old conversation turns
- **Prompt caching:** Cache prefix (system + docs) for repeated queries

---

## GPU Capacity Planning

```
Throughput ≈ (batch_size × tokens/sec) per GPU
7B model: ~1 GPU handles ~50-100 concurrent streams (varies)
70B model: 4-8 GPUs with tensor parallelism

Queue requests when GPUs saturated; return 503 or async webhook
```

---

## Caching

| Cache type | Key | Hit benefit |
|------------|-----|-------------|
| Exact prompt cache | hash(prompt) | Full response skip |
| Semantic cache | embed(query) | Similar query reuse |
| Embedding cache | hash(chunk) | Skip re-embed on ingest |

---

## Interview Phrases

> "SSE streaming — target TTFT under 300ms."
> "Model router sends 80% of queries to small model, saving 70% cost."
> "LLM gateway centralizes rate limits, auth, and observability."

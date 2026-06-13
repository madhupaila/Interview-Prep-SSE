# Design Fine-Tuning Pipeline

**Track:** Gen AI / LLM  
**Companies:** OpenAI, Hugging Face  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-HLD-G07-fine-tuning-pipeline.md](../../../Case Studies/hld/genai/CS-HLD-G07-fine-tuning-pipeline.md)
> **Read order:** Case Study → this question (timed mock)

**Business context:** Real-world context modeled after Leading products in the Design Fine-Tuning Pipeline domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## Problem Statement

Design a production system for: **Fine-Tuning Pipeline**.

---

## Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | B2B multi-tenant or consumer? | Assume 10K fine-tunes/month unless stated |
| 2 | Latency target for first token? | < 500ms TTFT, full response < 15s |
| 3 | Must answers be grounded/cited? | Depends on use case |
| 4 | Self-host models or API? | Start API; self-host at > 50M tokens/day |
| 5 | Data residency / compliance? | Mention GDPR, SOC2; HIPAA if medical |
| 6 | Human in the loop? | Escalation path for low-confidence |
| 7 | Scale? | 10K fine-tunes/month, GPU clusters |
| 8 | Offline/batch vs real-time? | Per focus: LoRA, eval gates, model registry |
| 9 | Multi-modal input? | Text primary |
| 10 | Evaluation before deploy? | Golden set + regression gate |

---

## Functional Requirements

- Core user-facing capability for fine-tuning pipeline
- Session/history management where applicable
- Admin: model version, prompt version, usage dashboards
- LoRA, eval gates, model registry

## Non-Functional Requirements

- Availability: 99.9%
- p99 latency: TTFT < 500ms for streaming
- Cost visibility per tenant/query
- Audit log for prompts, retrieval sources, responses
- Security: auth, PII handling, prompt injection defense

---

## Capacity Estimation

| Metric | Estimate |
|--------|----------|
| Scale | 10K fine-tunes/month |
| Throughput | GPU clusters |
| Avg tokens/query | 2K in + 500 out |
| Peak factor | 3× average |
| Embedding storage | ~6KB per 1536-dim vector |
| GPU need (if self-host) | 1 GPU ~ 50-100 concurrent streams (7B class) |

**Bottleneck callout:** LLM inference GPU pool or vector DB QPS at peak — scale horizontally with queue + autoscale.

---

## HLD Diagram

```
Clients → API Gateway → Core Service → LLM/Embed Layer → Data Stores
```

---

## Component Choices

| Component | Choice | Alternative |
|-----------|--------|-------------|
| API | FastAPI / Go gateway | Node for SSE-heavy |
| LLM | OpenAI API → vLLM at scale | Anthropic, Bedrock |
| Vector DB | pgvector → Pinecone | Weaviate, Milvus |
| Cache | Redis (sessions, semantic cache) | — |
| Queue | Kafka (ingestion, events) | SQS for simpler |
| Object storage | S3 | GCS, Azure Blob |
| Observability | Datadog + OpenTelemetry | Prometheus/Grafana |

---

## Deep Dive Topics

### 1. Retrieval & grounding
Hybrid BM25 + vector search; rerank top 20 → 5; refuse when max score < threshold.

### 2. Context window budget
System prompt + retrieved chunks + history + user query must fit model limit; summarize old turns.

### 3. Model routing
Classifier routes simple queries to small model (70% cost savings); complex to large model.

### 4. Safety & eval
Input/output guardrails; golden dataset blocks deploy on faithfulness regression > 5%.

---

## Tradeoffs

| Decision | Option A | Option B | Recommendation |
|----------|----------|----------|----------------|
| Knowledge | RAG | Fine-tune | RAG for dynamic data |
| LLM | API | Self-host | API until token volume justifies GPU ops |
| Vector DB | pgvector | Pinecone | pgvector < 50M vectors |
| Agent vs chain | Single-shot RAG | Multi-step agent | Agent only when tools needed |

---

## Failure Modes & Degradation

| Failure | Mitigation |
|---------|------------|
| LLM timeout | Fallback smaller model; return partial stream |
| Empty retrieval | "I don't know" — no hallucination |
| Vector DB down | Keyword-only fallback or graceful 503 |
| GPU saturation | Queue + 503 with retry-after |
| Prompt injection | Input guard + delimiter isolation |

---

## Interview Answer Script

> **Opening:** "Before I draw the architecture, I want to confirm scope. We're designing fine-tuning pipeline at scale — roughly 10K fine-tunes/month with GPU clusters. I'll focus on the core query path and ingestion if needed, and cover safety and cost."

> **Estimates:** "At peak 3× average, we need horizontal scaling on the stateless API and LLM gateway layers. Token throughput is the main cost driver — I'll add model routing and semantic caching."

> **Diagram:** "I'll draw two paths: ingestion pipeline for knowledge updates, and the online query path. User hits API gateway for auth and rate limits. The orchestrator builds the prompt — for RAG systems, we embed the query, hybrid search vector DB + BM25, rerank to top 5 chunks, then call LLM gateway with streaming SSE."

> **Deep dive:** "Key decision: LoRA, eval gates, model registry. For hallucination mitigation, we require citations grounded in retrieved chunks and block answers when retrieval confidence is low. Prompt injection is handled by isolating system instructions from user and document content."

> **Tradeoffs:** "I'd start with managed LLM API and pgvector on existing Postgres for vectors under 50M chunks. Migrate to self-hosted vLLM when token spend exceeds ops breakeven — typically 50-100M tokens per month."

> **Failure modes:** "LLM gateway has circuit breakers. If retrieval is empty, we don't ask the model to invent — we return a honest limitation message. All requests logged for audit and eval sampling."

> **Close:** "Happy to deep-dive on chunking strategy, agent tool loop, or GPU capacity planning."

---

## Follow-Up Questions

1. How would you evaluate answer quality before production deploy?
2. How do you handle document updates and stale chunks?
3. Walk through prompt injection attack and defense.
4. How would you reduce cost by 50% without hurting quality?
5. Design multi-tenant isolation for enterprise customers.

---

## Related

- [Gen AI Framework](../00-genai-hld-framework.md)
- [RAG Deep Dive](../01-rag-pipeline-deep-dive.md)
- [Interview Framework](../../00-interview-framework/01-hld-round-flow.md)

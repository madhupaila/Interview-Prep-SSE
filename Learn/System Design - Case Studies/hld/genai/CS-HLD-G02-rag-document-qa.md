# Design Enterprise RAG Document Q&A — Case Study

**Case Study ID:** CS-HLD-G02
**Track:** Gen AI / LLM HLD
**Companies:** Anthropic, Databricks, Notion, Harvey, Glean
**Difficulty:** Hard
**Related question:** [Q02-rag-document-qa.md](../../System Design - High Level Design/02-genai-llm-hld/questions/Q02-rag-document-qa.md)
**Paired case study:** [CS-PAIR-01-enterprise-rag.md](../paired/CS-PAIR-01-enterprise-rag.md)

---

## Part 1 — Business Context

**Industry analog:** Glean and Notion AI — employees search internal docs with AI-generated answers.

Acme Corp (fictional enterprise) has 10K B2B tenants, 10M documents, and 50M queries/day. Legal and compliance require **citations on every answer** and **zero cross-tenant data leaks**. The product team must ship MVP in 8 weeks with a team of 4 engineers.

**Why now:** GenAI made semantic search accessible, but enterprises won't adopt without ACL-aware retrieval and hallucination controls.

**Success:** p99 query latency < 8s, citation accuracy > 95%, SOC2 Type II within 12 months.

---

## Part 2 — Stakeholders & Personas

| Persona | Goals | Pain points | Success metric |
|---------|-------|-------------|----------------|
| End user | Complete core flows quickly | Slow, unreliable UX | Task completion rate > 95% |
| Product owner | Ship MVP on schedule | Scope creep | On-time V1 delivery |
| SRE / platform | Meet SLO with observability | Opaque failures | Error budget > 0 monthly |
| Security / compliance | Data protection, audit trail | Regulatory breach | Zero critical findings |

---

## Part 3 — Requirements

### Functional Requirements (MoSCoW)

| Priority | Requirement | Acceptance criteria |
|----------|-------------|---------------------|
| Must | Document upload + Drive/Confluence sync | E2E ingest → query in staging |
| Must | Q&A with page-level citations | Eval set faithfulness > 95% |
| Must | Tenant admin + usage dashboard | Admin can view audit log |
| Must | GDPR delete purges vectors in 24h | Integration test confirms zero chunks |
| Won't (MVP) | Multi-region active-active | Documented in PRD |
| Won't (MVP) | Advanced ML personalization | Documented in PRD |

### Non-Functional Requirements

| Attribute | Target | Measurement |
|-----------|--------|-------------|
| Latency | p99 < 8s end-to-end query | Distributed tracing |
| Availability | 99.9% | Monthly error budget |
| Isolation | Zero cross-tenant retrieval in pen test | Security CI suite |
| Ingestion lag | < 15 min for connector updates | Pipeline lag metric |

**From requirements analysis:**
- 99.9% availability
- Tenant data isolation (logical + encryption)
- Audit log: who queried what, which chunks retrieved
- Ingestion lag < 15 min for updates

---

### Clarifying Questions (Discovery Phase)

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | Document types? | PDF, DOCX, HTML, Markdown, Slack export |
| 2 | Tenants? | 10K enterprises, strict isolation |
| 3 | Citations required? | Yes — page/section references |
| 4 | Update frequency? | Daily sync from Confluence/Drive + manual upload |
| 5 | Max doc size? | 500 pages; 10M docs total across platform |
| 6 | ACL? | User only sees docs they have permission to |
| 7 | Latency? | p99 < 8s end-to-end |
| 8 | Hallucination tolerance? | Near zero — must cite or refuse |
| 9 | Languages? | English MVP; multilingual extension |
| 10 | Compliance? | SOC2, GDPR delete, optional HIPAA |

---

---

## Part 4 — Constraints

| Constraint | Detail | Impact on design |
|------------|--------|------------------|
| Budget | $80K/mo infra + $120K/mo LLM API at scale | Semantic cache + model routing |
| Team | 2 backend, 1 ML, 1 infra | Buy Pinecone; build orchestration |
| Timeline | MVP 8 weeks | English only; 3 connector types |
| Compliance | SOC2, GDPR delete within 24h | Audit log on every query |
| Hallucination | Near-zero tolerance | Citation validator + refuse path |

---

## Part 5 — Tradeoffs & Architecture Decision Records

### ADR-001: Vector store at 100M chunks

**Status:** Accepted  
**Context:** 100M vectors × 1536 dims ≈ 600 GB; need hybrid search.  
**Decision:** Pinecone managed + Elasticsearch BM25 with reciprocal rank fusion.  
**Consequences:** Vendor cost; ops simplicity; proven at scale.  
**Alternatives considered:** pgvector — rejected above 30M vectors per index.


### ADR-002: ACL enforcement point

**Status:** Accepted  
**Context:** Users must never retrieve unauthorized chunks.  
**Decision:** Metadata filter in vector DB query before ranking — never post-filter only.  
**Consequences:** Slightly slower queries; security invariant testable in CI.  
**Alternatives considered:** Post-filter after retrieval — rejected (leak risk + wasted compute).


### ADR-003: Answer format

**Status:** Accepted  
**Context:** Need machine-verifiable citations.  
**Decision:** Structured JSON: `{answer, citations[]}` + NLI faithfulness check.  
**Consequences:** Easier validation; slightly higher latency.  
**Alternatives considered:** Free text — rejected for enterprise compliance.


### Tradeoffs Summary (from design analysis)


| Decision | A | B | Pick |
|----------|---|---|------|
| Vector store | pgvector | Pinecone | Pinecone at 100M vectors |
| Chunk size | 256 | 512 | 512 with overlap for contracts |
| Answer style | Free text | Structured JSON | JSON with `answer` + `citations[]` for validation |

---



---

## Part 6 — Capacity & Cost Estimation

```
10K tenants × 1K docs avg = 10M documents
10 pages/doc avg × 10 chunks/page = 100M chunks

Vector storage: 100M × 1536 dims × 4 bytes ≈ 600 GB
Metadata Postgres: ~200 GB
Queries: 50M/day → 580 QPS avg, ~1,750 peak

Embedding on ingest: batch 100 chunks/call → ~1M API calls on full reindex
```

---

### Cost ballpark (V1)

- Compute: $5–15K/mo\n- Managed DB/cache: $3–8K/mo\n- LLM API (if applicable): usage-based; budget caps per tenant

---

## Part 7 — High-Level Design

### Problem recap

Design an enterprise document Q&A system: employees upload PDFs, Word docs, wikis; ask natural language questions; receive grounded answers with citations. Multi-tenant B2B SaaS.

---

### Architecture

**Ingestion:**
```
Connector/Webhook → S3 → SQS → Parser Worker → Chunker → Embed Batch API → VectorDB
                              ↓
                         Metadata DB (doc_id, tenant_id, ACL, version)
```

**Query:**
```
User → API GW → AuthZ (doc ACL filter) → Query Embed → Hybrid Search → Reranker
    → Prompt Builder → LLM Gateway → Citation Validator → Response
```

```mermaid
flowchart TB
  subgraph ingest [Ingestion]
    S3[S3] --> W[Workers]
    W --> E[Embedder]
    E --> VDB[(VectorDB)]
    W --> MDB[(MetadataDB)]
  end
  subgraph query [Query]
    U[User] --> API[API]
    API --> R[Retriever]
    R --> VDB
    R --> Rank[Reranker]
    Rank --> LLM[LLM]
    LLM --> U
  end
```

---

### Component choices

| Component | Choice | Alternative |
|-----------|--------|-------------|
| Vector DB | Pinecone (managed) | pgvector if < 30M vectors per tenant |
| Hybrid search | Elasticsearch + vector | Weaviate native hybrid |
| Parser | Unstructured.io | Custom per format |
| Chunking | 512 tokens, 10% overlap | Semantic chunking for contracts |
| Reranker | Cohere rerank-3 | cross-encoder self-host |
| LLM | GPT-4 class with strict system prompt | Claude for long context |

---

### Deep dive topics

### 1. ACL enforcement
Every chunk stores `tenant_id`, `doc_id`, `allowed_groups[]`. Query adds metadata filter BEFORE vector search — never post-filter only.

### 2. Chunking for citations
Store `page_number`, `section_heading`, `char_offset` in metadata. Prompt: "Answer only from context; cite as [doc_name, p.X]."

### 3. Hybrid retrieval
BM25 catches SKUs and legal clause numbers; vectors catch paraphrases. Reciprocal Rank Fusion merges lists.

### 4. Freshness
On doc update: increment `version`, delete old chunk IDs async, re-ingest. Query excludes `version < current`.

### 5. Hallucination guard
Post-LLM: extract citation markers; verify each claim sentence has supporting chunk via NLI model; else regenerate or refuse.

---

### Failure modes

| Failure | Mitigation |
|---------|------------|
| No chunks above score threshold | Return "No relevant documents found" |
| LLM invents citation | Citation validator strips or regenerates |
| Ingestion backlog | Scale workers; priority queue for premium tenants |
| Cross-tenant leak | Filter in DB query; security test in CI |

---

---

## Part 8 — Low-Level Design (LLD Boundary)

At the HLD level, defer class-level design to the LLD round. Sketch the **object model** the interviewer may ask for:

### Core object clusters

- **Service facade** — orchestrates use cases\n- **Domain entities** — hold business state\n- **Strategy interfaces** — swappable algorithms

### Patterns to mention in LLD follow-up

| Pattern | Use |
|---------|-----|
| Strategy | Swappable algorithms (allocation, routing, pricing) |
| Repository | Persistence abstraction behind domain |
| Factory | Complex object creation |
| Observer | Event notifications |

### Pivot script

> "At object level I'd model the core domain entities with a service facade and Strategy for variation points. "
> "For distributed scale, I'd add the cache, queue, and shard layers from the HLD — happy to go deeper on either."


## Part 9 — Implementation Roadmap

| Phase | Timeline | Scope | Out of scope |
|-------|----------|-------|--------------|
| MVP | 2 weeks | Single-region, core user flows, manual ops | Multi-region, advanced analytics |
| V1 | 3 months | Production SLO, auth, monitoring, connector integrations | Custom ML models |
| Scale | 12 months | Auto-scaling, cost optimization, enterprise compliance | Edge deployment |

**MVP success criteria for Design Enterprise RAG Document Q&A:** Core flows demo-ready; p99 within 2× target; on-call runbook draft.

---

## Part 10 — Operations

### SLI / SLO

| SLI | Definition | SLO |
|-----|------------|-----|
| Availability | successful_requests / total_requests | 99.9% monthly |
| Latency | p99 response time | < 8s |

### Observability

- **Metrics:** Request rate, error rate, latency histograms, queue depth, cache hit ratio
- **Logs:** Structured JSON with `trace_id`, `tenant_id`, `user_id`
- **Traces:** OpenTelemetry across API → workers → DB/cache/LLM

### Deployment

- Blue/green or canary via CI/CD; feature flags for risky changes
- Database migrations backward-compatible; expand-contract pattern

### Incident Runbook

**Scenario:** Retrieval returns empty for known-good documents.

1. Check embedding model version drift vs index
2. Verify ACL filter not over-restrictive for user groups
3. Compare BM25 vs vector recall on failing queries
4. Roll back recent chunking config change if regression

### Security Checklist

- Authentication via org SSO (OIDC)
- Authorization at API + data layer
- Encryption at rest (AES-256) and in transit (TLS 1.3)
- Audit log for admin and sensitive reads
- Secrets in vault; no keys in code
- Prompt injection tests in CI
- Output guardrails on PII and policy violations


---

## Part 11 — Interview Walkthrough (30 min)

> This is a 30-minute senior loop for **Design Enterprise RAG Document Q&A**. Spend 5 minutes on context, 10 on HLD, 10 on LLD/boundaries, 5 on ops.

> "I'm designing enterprise RAG for 10K tenants and 10M documents, 50M queries daily, with mandatory citations and strict tenant isolation."

> "Ingestion is async: documents land in S3 from upload or connectors. Workers parse, chunk at 512 tokens with 10% overlap, batch-embed, and upsert to Pinecone with metadata — tenant_id, doc_id, ACL groups, page number, version. A Postgres metadata DB tracks document state and permissions."

> "On query, we authenticate, embed the question, and run hybrid search — BM25 in Elasticsearch plus vector search in Pinecone, merged with reciprocal rank fusion. Critically, ACL filters apply in the retrieval query, not after — so we never retrieve unauthorized chunks."

> "Top 20 chunks go to a reranker; we keep top 5. The prompt instructs answer-only-from-context with citations like [Policy Handbook, p.12]. LLM generates; then a citation validator checks that claims map to retrieved text using an NLI model. If faithfulness fails, we regenerate once or return a safe refusal."

> "For updates, CDC from connectors triggers re-ingestion; we version chunks and delete stale vectors. GDPR delete purges all vectors for a tenant within 24 hours."

> "Cost: batch embeddings on ingest; semantic cache for repeated enterprise FAQs. Model routing sends simple definitional questions to a smaller model."

> "This design prioritizes correctness over creativity — enterprise users prefer 'I don't know' over a confident wrong answer."

> ---

> If the interviewer pivots to object design, I sketch the service boundaries and DTOs — detailed classes are in the LLD case study.



---

## Part 11b — Practical Learning Lab

### Hands-on exercises

1. **Whiteboard (15 min):** Draw HLD distributed components from memory after reading Parts 1–5.
2. **Tradeoff drill (10 min):** Pick one ADR and argue the rejected alternative for 2 minutes.
3. **Failure mode (10 min):** Pick one failure from Part 7/10; write a 5-step runbook.
4. **Pivot practice (5 min):** Practice the HLD↔LLD pivot script aloud.
5. **Timed mock (45 min):** Use the linked question file without looking at this case study.

### Production readiness checklist

- [ ] SLO defined and dashboarded
- [ ] Load test at 2× expected peak QPS
- [ ] Chaos test: kill one dependency; verify degradation
- [ ] Security review: auth, encryption, audit
- [ ] Runbook linked from on-call playbook
- [ ] Cost model reviewed with FinOps
- [ ] ADRs stored in repo `docs/adr/`

### Industry comparison

| Capability | Glean and Notion AI — enterprise knowledge search with grounded answers (reference) | This design (MVP) | Scale phase |
|------------|----------------------|-------------------|-------------|
| Core flow | Production-grade | MVP scope in Part 9 | Part 9 Scale column |
| Reliability | Multi-region | Single-region 99.9% | Multi-region failover |
| Observability | Full APM + SRE | Metrics + traces + logs | SLO error budgets |
| Security | Enterprise compliance | Checklist in Part 10 | SOC2 / pen test |


### OWASP LLM Top 10 Mapping

| Risk | Mitigation in this design |
|------|---------------------------|
| LLM01 Prompt injection | Input sanitization; separate system/user channels |
| LLM06 Sensitive disclosure | ACL on retrieval; redact PII in logs |
| LLM09 Overreliance | Citations, confidence scores, refuse when uncertain |
| LLM10 Model theft | API keys in vault; rate limits per tenant |


### Senior interviewer rubric

| Signal | Strong | Weak |
|--------|--------|------|
| Requirements | Measurable NFRs stated upfront | Vague "it should scale" |
| Constraints | Names budget, team, timeline | Ignores constraints |
| Tradeoffs | ADR with rejected alternative | Single option only |
| Depth | Failure modes unprompted | Happy path only |
| Communication | Structured 30-min narrative | Jumps to diagram |



---

## Part 12 — Related Links

- **Question file:** [Q02-rag-document-qa.md](../../System Design - High Level Design/02-genai-llm-hld/questions/Q02-rag-document-qa.md)
- **End-to-end pair:** [CS-PAIR-01-enterprise-rag.md](../paired/CS-PAIR-01-enterprise-rag.md)
- **Template:** [case-study-template.md](../00-framework/case-study-template.md)
- **Industry standards:** [industry-standards-reference.md](../00-framework/industry-standards-reference.md)

- [RAG Deep Dive](../01-rag-pipeline-deep-dive.md)
- [Evaluation & Safety](../04-evaluation-safety-cost.md)

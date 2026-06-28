# RAG Orchestrator — Case Study

**Case Study ID:** CS-LLD-A01
**Track:** Gen AI LLD
**Companies:** OpenAI, Anthropic, Google
**Difficulty:** Hard
**Related question:** [Q01-rag-orchestrator.md](../../../System%20Design%20-%20Low%20Level%20Design/05-genai-llm-lld/questions/Q01-rag-orchestrator.md)
**Paired case study:** [CS-PAIR-01-enterprise-rag.md](../../paired/CS-PAIR-01-enterprise-rag.md)

---

## Part 1 — Business Context

**Industry analog:** LangChain/LlamaIndex in-process RAG pipeline.

Design the **object model** for retrieve → rerank → assemble context → generate. Vector DB and LLM API are external (HLD). Focus on SOLID, testability, and swappable components.

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
| Must | **Functional:** | Verified in integration tests |
| Must | answer(query) → retrieve → rerank → assemble context → generate | Verified in integration tests |
| Must | Pluggable retriever (keyword stub, vector stub) | Verified in integration tests |
| Must | Token budget awareness before generation | Verified in integration tests |
| Must | Return answer with optional source citations | Verified in integration tests |
| Won't (MVP) | Multi-region active-active | Documented in PRD |
| Won't (MVP) | Advanced ML personalization | Documented in PRD |

### Non-Functional Requirements

| Attribute | Target | Measurement |
|-----------|--------|-------------|
| Latency | p99 < 500ms sync API; p99 < 8s LLM | APM / distributed tracing |
| Availability | 99.9% | Uptime SLO dashboard |
| Throughput | 10K peak QPS (scale phase) | Load test report |
| Security | AuthN/Z, encryption at rest/transit | Annual pen test |
| Maintainability | Modular services, ADRs documented | Change failure rate < 15% |
| LLM faithfulness | Citation accuracy > 95% on eval set | Offline eval pipeline |

**From requirements analysis:**
:**
- Clear separation of concerns (SOLID)
- Open-Closed via Retriever interface at variation points
- Constructor injection for testability
- Swappable pipeline stages behind interfaces
- Explicit boundary to HLD for vector DB, model serving, queues

---

### Clarifying Questions (Discovery Phase)

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | Distributed or in-process? | In-process object model; vector DB is HLD |
| 2 | Swappable components? | Retriever, Reranker, Generator as interfaces |
| 3 | Streaming response? | Extension via StreamAggregator |
| 4 | Safety filters? | Extension — GuardrailChain on input/output |
| 5 | Multi-tenant? | Optional tenantId in Query context |
| 6 | Token budget? | Yes — truncate context before generate |
| 7 | Citation required? | Return source ids with RetrievedChunk |
| 8 | Reranker optional? | Yes — passthrough if not injected |

---

---

## Part 4 — Constraints

| Constraint | Detail | Impact on design |
|------------|--------|------------------|
| Budget | $50K/month infra at V1 scale | Prefer managed services over self-host |
| Team | 2 backend, 1 frontend, 1 ML engineer | MVP scope strictly bounded |
| Timeline | MVP in 8 weeks | Defer nice-to-have features |
| Tech | Cloud-native on AWS/GCP | Use existing org SSO and VPC |
| Build vs buy | Buy vector DB / LLM API; build orchestration | Focus engineering on differentiation |

---

## Part 5 — Tradeoffs & Architecture Decision Records

### ADR-001: Primary architecture pattern

**Status:** Accepted  
**Context:** Need to balance delivery speed, operability, and scale for RAG Orchestrator.  
**Decision:** Event-driven async for writes; cache-heavy sync read path.  
**Consequences:** Higher eventual consistency on analytics; simpler peak handling.  
**Alternatives considered:** Fully synchronous CRUD — rejected due to peak QPS.


### ADR-002: Data store selection

**Status:** Accepted  
**Context:** Mixed OLTP, cache, and search/vector needs.  
**Decision:** PostgreSQL for source of truth; Redis for hot path; specialized index where needed.  
**Consequences:** Operational complexity of multiple stores; optimal per access pattern.  
**Alternatives considered:** Single document DB — rejected for strong consistency requirements.


### ADR-003: Multi-tenancy model

**Status:** Accepted  
**Context:** B2B SaaS with strict isolation requirements.  
**Decision:** Logical tenant_id on all rows + encryption per tenant for sensitive payloads.  
**Consequences:** Cost-effective vs physical isolation; requires rigorous integration tests.  
**Alternatives considered:** Database-per-tenant — rejected at 10K tenant scale.


### Tradeoffs Summary (from design analysis)


| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Chain of Responsibility | Chain of Responsibility — 2+ behaviors |
| State | enum | State pattern | enum for simple lifecycles |
| Storage | in-memory | Repository | in-memory MVP |
| API return | primitive | domain object | domain object — type safety |

---



---

## Part 6 — Capacity & Cost Estimation

**Scale projection:** Start with single-region MVP; model QPS and storage at 10× current load before Scale phase.

### Cost ballpark (V1)

- Compute: $5–15K/mo\n- Managed DB/cache: $3–8K/mo\n- LLM API (if applicable): usage-based; budget caps per tenant

---

## Part 7 — High-Level Design (Scale Projection / HLD Boundary)

The LLD object model is correct for **single-process / in-memory MVP**. When the interviewer pivots to scale:

### Scale triggers

| Signal | HLD addition |
|--------|--------------|
| Multiple instances | Stateless API behind load balancer |
| Shared state | Redis / distributed cache |
| Write contention | Message queue + async workers |
| Global users | Multi-region read replicas; CDN |



### Distributed sketch

```
Client → CDN → LB → API (stateless) → Cache → DB
                              ↓
                         Message queue → Workers
```

### Pivot script

> "My object model stays — ParkingLotService, Strategy, entities. "
> "At scale I'd add a central occupancy registry in Redis, event bus for cross-garage sync, and shard by buildingId."


---

## Part 8 — Low-Level Design

### Problem recap

Design in-process RAG orchestrator: retrieve, rerank, assemble context, generate.

---

### Core entities

| Entity | Role |
|--------|------|
| `RAGOrchestrator` | Pipeline |
| `Retriever` | Fetch chunks |
| `Reranker` | Score order |
| `ContextAssembler` | Prompt build |
| `Generator` | LLM interface |

**Nouns → classes:** `RAGOrchestrator`, `Retriever`, `Reranker`, `ContextAssembler`, `Generator`  
**Verbs → methods:** `answer(Query)`, `retrieve(Query)`, `assemble(chunks)`

---

### Class diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  RAGOrchestrator    │──────>│ Pipeline         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcretePipeline │
│  RAGOrchestrator    │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Retriever          │────>│  Reranker        │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class RAGOrchestrator {
        +String answer(Query query)
        +List<RetrievedChunk> retrieve(Query query)
        +String assemble(List<RetrievedChunk> chunks)
    }
    class Retriever {
        <<interface>>
        +retrieve(Query) List
    }
    class Reranker {
        <<interface>>
        +rerank(Query, List) List
    }
    class ContextAssembler {
        +assemble(List) String
    }
    class Generator {
        <<interface>>
        +generate(Query, String) String
    }
```

---

### Public API

```java
public class RAGOrchestrator {
    public String answer(Query query);
    public List<RetrievedChunk> retrieve(Query query);
    public String assemble(List<RetrievedChunk> chunks);
}
```

---

### Design patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Pipeline | Sequential stages with shared Query context |
| Strategy | Swappable Retriever/Reranker/Generator |

**SOLID:**
- **S:** RAGOrchestrator orchestrates; entities hold state
- **O:** New behavior via new Retriever impl
- **D:** Depend on Retriever interface

---

### Sequence diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant R as RAGOrchestrator
participant Ret as Retriever
participant Rank as Reranker
participant G as Generator
U->>R: answer(query)
R->>Ret: retrieve(query)
Ret-->>R: chunks
R->>Rank: rerank(query, chunks)
Rank-->>R: topK
R->>G: generate(query, context)
G-->>R: answer
R-->>U: answer + citations
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant R as RAGOrchestrator
participant Ret as Retriever
U->>R: answer(query)
R->>Ret: retrieve(query)
Ret-->>R: empty
R-->>U: NoContextException
```

---

### Concurrency & edge cases

- Pipeline stages sequential in MVP — parallel retrieve+embed is HLD
- Empty retrieval → NoContextException or fallback message
- Token overflow → TruncationStrategy trims oldest chunks
- Generator timeout → wrap in CompletableFuture at HLD layer

---

---

## Part 9 — Implementation Roadmap

| Phase | Timeline | Scope | Out of scope |
|-------|----------|-------|--------------|
| MVP | 2 weeks | Single-region, core user flows, manual ops | Multi-region, advanced analytics |
| V1 | 3 months | Production SLO, auth, monitoring, connector integrations | Custom ML models |
| Scale | 12 months | Auto-scaling, cost optimization, enterprise compliance | Edge deployment |

**MVP success criteria for RAG Orchestrator:** Core flows demo-ready; p99 within 2× target; on-call runbook draft.

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

**Scenario:** p99 latency spike 3× baseline.

1. Check error budget burn in Grafana
2. Identify hot shard / tenant via trace tags
3. Scale workers or enable degradation mode
4. Post-incident: ADR if architecture change needed

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

> This is a 30-minute senior loop for **RAG Orchestrator**. Spend 5 minutes on context, 10 on HLD, 10 on LLD/boundaries, 5 on ops.

> "RAGOrchestrator coordinates retrieve-rerank-generate pipeline behind single answer() API."
>
> "Query carries user text, tenantId, maxTokens, and metadata."
>
> "Retriever interface abstracts vector DB — LLD uses in-memory stub."
>
> "Reranker re-scores chunks; default passthrough if not configured."
>
> "ContextAssembler builds prompt string respecting TokenBudget."
>
> "Generator interface wraps LLMProvider — returns completion text."
>
> "Each stage is independently testable with mocks — OCP."
>
> "HLD adds Pinecone, embedding service, queue; LLD pipeline shape unchanged."

> ---

> If the interviewer asks about millions of users, I pivot: same object model, but add Redis cache, message queue, and sharded DB — see HLD case study.



---

## Part 11b — Practical Learning Lab

### Hands-on exercises

1. **Whiteboard (15 min):** Draw LLD object model and patterns from memory after reading Parts 1–5.
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

| Capability | LangChain / LlamaIndex RAG pipeline — retrieve, rerank, generate (reference) | This design (MVP) | Scale phase |
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

- **Question file:** [Q01-rag-orchestrator.md](../../../System%20Design%20-%20Low%20Level%20Design/05-genai-llm-lld/questions/Q01-rag-orchestrator.md)
- **End-to-end pair:** [CS-PAIR-01-enterprise-rag.md](../../paired/CS-PAIR-01-enterprise-rag.md)
- **Template:** [case-study-template.md](../../00-framework/case-study-template.md)
- **Industry standards:** [industry-standards-reference.md](../../00-framework/industry-standards-reference.md)

- [Gen AI LLD memory map](../../../System%20Design%20-%20Low%20Level%20Design/05-genai-llm-lld/memory-map-genai-lld.md)
- [Strategy pattern](../../../System%20Design%20-%20Low%20Level%20Design/01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../../System%20Design%20-%20Low%20Level%20Design/01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../../System%20Design%20-%20Low%20Level%20Design/01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../../System Design - Low Level Design/09-code-implementations/java/genai/rag-orchestrator/) (full)
- [HLD counterpart](../../../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q02-rag-document-qa.md)

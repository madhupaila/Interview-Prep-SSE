# Component Picker — When to Use What

Decision guide for common HLD components. Use in interviews to justify choices.

---

## Caching

| Component | Use when | Avoid when |
|-----------|----------|------------|
| **Redis** | Need data structures (sorted sets, pub/sub), TTL, session store | Pure key-value at huge scale with simpler needs |
| **Memcached** | Simple key-value, multi-threaded, RAM-only | Need persistence or complex types |
| **CDN** | Static assets, video segments, API cache at edge | Highly personalized dynamic content |
| **Application cache** | In-process, ultra-low latency | Multi-instance consistency needed |

**Pattern picker:**

| Pattern | Use when |
|---------|----------|
| Cache-aside | Default; app manages cache |
| Write-through | Cache and DB must stay in sync |
| Write-behind | Write burst tolerance, eventual DB sync |

---

## Databases

| Component | Use when | Avoid when |
|-----------|----------|------------|
| **PostgreSQL** | ACID, joins, complex queries, < ~10K write QPS per shard | Massive horizontal write scale |
| **MySQL** | Similar to Postgres, legacy ecosystems | Need advanced JSON/window functions |
| **DynamoDB** | Key-value/document at AWS scale, predictable access patterns | Ad-hoc joins, complex analytics |
| **Cassandra** | Write-heavy, multi-region, time-series | Strong consistency across regions |
| **MongoDB** | Flexible schema, document model | Multi-document ACID across collections |
| **S3 / Blob** | Files, images, videos, backups | Low-latency random access |

**Sharding triggers:** Single primary > 70% CPU, write QPS > 5–10K, storage > few TB.

---

## Search

| Component | Use when |
|-----------|----------|
| **Elasticsearch** | Full-text, facets, aggregations, log search |
| **Postgres FTS** | Simple search, already on Postgres, < millions of docs |
| **Vector DB** (Pinecone, Weaviate, pgvector) | Semantic / embedding search |
| **Hybrid** (ES + vector) | Keyword + semantic (common in RAG) |

---

## Messaging

| Component | Use when | Avoid when |
|-----------|----------|------------|
| **Kafka** | Event log, replay, high throughput, stream processing | Simple task queue, low ops tolerance |
| **SQS** | Managed queue, decouple services, AWS native | Need replay or ordering guarantees |
| **RabbitMQ** | Complex routing, lower volume | Extreme throughput |
| **Redis Streams** | Lightweight queue, already using Redis | Long retention, multi-consumer groups at scale |

**Delivery semantics:**

| Need | Choice |
|------|--------|
| At-most-once | Fire and forget |
| At-least-once | Kafka/SQS + idempotent consumers |
| Exactly-once | Kafka transactions + idempotent writes (complex) |

---

## API & Communication

| Component | Use when |
|-----------|----------|
| **REST** | Public APIs, CRUD, broad compatibility |
| **gRPC** | Internal services, low latency, streaming |
| **GraphQL** | Flexible client queries, BFF pattern |
| **WebSocket** | Bi-directional real-time (chat, games) |
| **SSE** | Server push one-way (LLM token streaming) |
| **Webhook** | Async notifications to clients |

---

## Load Balancing & Gateway

| Component | Use when |
|-----------|----------|
| **L4 LB** (NLB) | TCP, extreme performance |
| **L7 LB** (ALB) | HTTP routing, path-based rules |
| **API Gateway** | Rate limiting, auth, API keys, request transformation |
| **Service mesh** (Istio) | mTLS, observability, many microservices |

---

## Gen AI / LLM Stack

| Component | Use when |
|-----------|----------|
| **OpenAI / Anthropic API** | Fast MVP, no GPU ops |
| **vLLM / TGI** | Self-host, cost at scale, data residency |
| **Embedding API** (OpenAI, Cohere) | Quality, speed to market |
| **Self-host embeddings** | Cost, privacy, custom models |
| **Pinecone** | Managed vector search at scale |
| **pgvector** | Already on Postgres, < 100M vectors |
| **LangChain / LlamaIndex** | Orchestration prototyping (not for prod scale alone) |
| **Reranker** (Cohere, cross-encoder) | Improve retrieval precision |

**Model routing:**

| Query type | Route to |
|------------|----------|
| Simple FAQ | Small/cheap model |
| Complex reasoning | Large model |
| Code generation | Code-specialized model |
| Low confidence | Escalate to larger model or human |

---

## Observability

| Component | Use when |
|-----------|----------|
| **Prometheus + Grafana** | Metrics, alerting |
| **Datadog / New Relic** | Managed APM |
| **ELK / OpenSearch** | Log aggregation |
| **Jaeger / Zipkin** | Distributed tracing |
| **PagerDuty** | On-call escalation |

**Metrics to mention:** RED (Rate, Errors, Duration) for services; USE (Utilization, Saturation, Errors) for resources.

---

## Security

| Component | Use when |
|-----------|----------|
| **OAuth 2.0 + OIDC** | Third-party login, SSO |
| **JWT** | Stateless API auth |
| **API keys** | Service-to-service, developer APIs |
| **KMS / Vault** | Secrets, encryption keys |
| **WAF** | DDoS, SQL injection at edge |

---

## Decision Tree (Quick Reference)

```
Need storage?
├── Structured + transactions → PostgreSQL
├── Key-value at massive scale → DynamoDB
├── Files/media → S3
└── Semantic search → Vector DB

Need async?
├── Replay + streams → Kafka
├── Simple decouple → SQS
└── Real-time to client → WebSocket or SSE

Need AI?
├── MVP / no GPUs → External LLM API
├── Scale / privacy → Self-host vLLM
├── Knowledge grounding → RAG (vector + hybrid search)
└── Tool use → Agent loop + function calling
```

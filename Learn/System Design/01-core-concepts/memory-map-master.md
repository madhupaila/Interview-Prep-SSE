# Master Memory Map — Core HLD Concepts

**Print this page.** One-glance reference for interviews.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SENIOR HLD MEMORY MAP                                │
├─────────────────────────────────────────────────────────────────────────┤
│ INTERVIEW FLOW                                                          │
│   Clarify → Scope MVP → Estimate → Diagram → Deep Dive → Tradeoff →   │
│   Failure modes                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│ SCALE                                                                   │
│   Horizontal (stateless) │ LB: round-robin, least-conn, consistent-hash│
│   Shard: hash(user_id) │ Hot key → dedicated cache/shard               │
├─────────────────────────────────────────────────────────────────────────┤
│ CACHE                                                                   │
│   Aside (default) │ TTL + invalidate on write │ CDN for static           │
│   Stampede → lock / singleflight                                        │
├─────────────────────────────────────────────────────────────────────────┤
│ DATABASE                                                                │
│   SQL: ACID, joins (Postgres) │ NoSQL: scale (Dynamo, Cassandra)        │
│   Primary + read replicas │ Shard when write QPS > ~5-10K                │
│   CAP: partition → Consistency OR Availability                          │
├─────────────────────────────────────────────────────────────────────────┤
│ MESSAGING                                                               │
│   Kafka: replay, streams │ SQS: simple queue                            │
│   At-least-once + idempotent consumer │ DLQ for failures                │
├─────────────────────────────────────────────────────────────────────────┤
│ API                                                                     │
│   REST public │ gRPC internal │ WebSocket chat │ SSE LLM stream         │
│   Circuit breaker │ Retry + backoff │ Idempotency keys                   │
├─────────────────────────────────────────────────────────────────────────┤
│ CONSISTENCY                                                             │
│   Strong: payments │ Eventual: feeds │ Saga for distributed txns         │
├─────────────────────────────────────────────────────────────────────────┤
│ SECURITY                                                                │
│   OAuth/JWT │ tenant_id multi-tenancy │ TLS + KMS encryption            │
├─────────────────────────────────────────────────────────────────────────┤
│ OBSERVABILITY                                                           │
│   RED metrics │ Distributed traces │ SLO + error budget                 │
├─────────────────────────────────────────────────────────────────────────┤
│ ESTIMATION FORMULAS                                                     │
│   QPS = requests/day ÷ 86,400 │ Peak ≈ 3× avg                           │
│   Storage = records × size × replication × growth years                 │
├─────────────────────────────────────────────────────────────────────────┤
│ CLASSIC PATTERNS                                                        │
│   Feed: fan-out on write (normal) + merge on read (celebrities)         │
│   Chat: WebSocket + message queue + Cassandra by conversation_id        │
│   URL shortener: base62 encode │ counter or hash │ cache hot links      │
│   Rate limiter: token bucket │ sliding window in Redis                  │
│   Search: inverted index (Elasticsearch) │ Crawler: BFS + bloom filter    │
└─────────────────────────────────────────────────────────────────────────┘
```

## Quick Component Picker

| Need | Pick |
|------|------|
| Fast reads | Redis cache-aside |
| Files/media | S3 + CDN |
| Full-text search | Elasticsearch |
| Simple queue | SQS |
| Event log | Kafka |
| Transactions | PostgreSQL |
| Massive KV writes | DynamoDB |
| Real-time push | WebSocket |
| LLM streaming | SSE |

## Diagram Layers (Top → Bottom)

```
Clients → CDN → LB → API Gateway → Services → Cache → DB
                                      ↓
                                   Queue → Workers
```

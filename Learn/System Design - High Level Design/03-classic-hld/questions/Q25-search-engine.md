# Design Search Engine

**Track:** Classic HLD  
**Companies:** Google, Microsoft  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-HLD-C25-search-engine.md](../../../Case Studies/hld/classic/CS-HLD-C25-search-engine.md)
> **Read order:** Case Study → this question (timed mock)

**Business context:** Real-world context modeled after Google Search — crawl, index, rank, serve. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## Problem Statement

Design a scalable system for: **Search Engine**.

---

## Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | Scale (DAU, QPS)? | 1B queries/day |
| 2 | Read vs write ratio? | inverted index |
| 3 | Latency requirements? | p99 < 200ms for reads unless media |
| 4 | Consistency requirements? | Eventual OK for feeds; strong for payments/booking |
| 5 | Geographic scope? | Global with multi-region if large scale |
| 6 | Mobile vs web? | Both — design API-first |
| 7 | MVP scope? | Core PageRank basics |
| 8 | Durability? | No data loss for user content/transactions |
| 9 | CAP preference? | Depends on domain — state explicitly |
| 10 | Out of scope? | Admin UI, ML model training internals |

---

## Functional Requirements

- Core features for search engine
- User authentication and authorization
- PageRank basics

## Non-Functional Requirements

- High availability: 99.9%+
- Low latency on hot read path
- Horizontally scalable
- Observable: metrics, tracing, alerting

---

## Capacity Estimation

| Metric | Estimate |
|--------|----------|
| Scale | 1B queries/day |
| Traffic pattern | inverted index |
| QPS (derived) | Calculate: daily requests / 86400 × peak factor 3 |
| Storage (5 yr) | Estimate records × size × replication |
| Bandwidth | QPS × avg payload size |

**Example math to say aloud:**
> "If 100M DAU × 50 requests/day = 5B requests/day ≈ 58K QPS average, ~175K peak. Storage: [run numbers for this domain]."

**Bottleneck:** Identify primary — DB writes, fan-out, geo index, or bandwidth.

---

## HLD Diagram

```
Query → API → Elasticsearch (inverted index) → Results
Indexer ← Kafka ← Content changes
```

---

## Component Choices

| Component | Choice | Alternative |
|-----------|--------|-------------|
| API | REST + internal gRPC | GraphQL for mobile BFF |
| Load balancer | L7 ALB | NLB for TCP-heavy |
| Cache | Redis | Memcached for simple KV |
| Primary DB | PostgreSQL / Cassandra* | *Cassandra for chat/write-heavy |
| Search | Elasticsearch | Postgres FTS if simple |
| Queue | Kafka | SQS for simpler workloads |
| Blob storage | S3 | For media/files |
| CDN | CloudFront/Akamai | Static and media delivery |

---

## Deep Dive Topics

### 1. Data model
Define primary entities, partition/shard key, and indexes for hot queries.

### 2. Hot path optimization
Caching strategy (cache-aside, TTL), CDN for static/media, read replicas.

### 3. Scaling strategy
Horizontal stateless services; shard DB by natural key (user_id, conversation_id, region).

### 4. Consistency & conflicts
Eventual consistency where OK; optimistic locking for inventory/booking; idempotency for payments.

---

## Tradeoffs

| Decision | Option A | Option B | Recommendation |
|----------|----------|----------|----------------|
| Architecture | Monolith | Microservices | Monolith early; split hot paths at scale |
| DB | SQL | NoSQL | SQL for transactions; Cassandra for chat/logs |
| Fan-out | On write | On read | Hybrid for social feeds |
| Consistency | Strong | Eventual | Match to business requirement |

---

## Failure Modes & Degradation

| Failure | Mitigation |
|---------|------------|
| DB primary down | Failover to replica; brief write unavailability |
| Cache down | Fall through to DB; circuit breaker prevents overload |
| Queue lag | Scale consumers; backpressure on producers |
| Region outage | DNS failover; multi-region replicas |
| Dependency timeout | Circuit breaker; cached fallback response |

---

## Interview Answer Script

> **Opening:** "Let me clarify requirements for search engine. We're targeting 1B queries/day with a inverted index pattern. I'll design the MVP core flow, estimate scale, draw the architecture, and we can deep-dive where you prefer."

> **Estimates:** "Working through the math: [DAU × actions / 86400]. Peak is roughly 3× average. The bottleneck will be [writes to DB / fan-out / geo queries] — I'll address that in the deep dive."

> **Diagram:** "I draw top-down: clients through CDN and load balancer to API gateway, then domain services, then cache and database. Async work goes through Kafka to workers — for example notifications, indexing, or fan-out."

> **Deep dive:** "The critical design decision here is PageRank basics. [Explain pattern-specific logic — e.g., for feed: hybrid fan-out; for payments: idempotency keys and ledger.]"

> **Tradeoffs:** "I chose [component] because at this scale [quantified reason]. Alternative would be [B] which trades [X] for [Y]."

> **Failure modes:** "If Redis is unavailable, we tolerate higher DB load with rate limiting. If Kafka lags, feed updates may be delayed but core writes still succeed. Multi-AZ deployment for the database with automated failover."

> **Close:** "I can go deeper on data schema, sharding, or the async pipeline."

---

## Follow-Up Questions

1. How would you shard the database?
2. What happens when a celebrity user posts? (if social)
3. How do you ensure idempotency? (if financial/async)
4. Design for multi-region deployment.
5. What metrics and alerts would you set up?

---

## Related

- [Classic Patterns](../00-classic-patterns.md)
- [Component Picker](../../00-interview-framework/04-component-picker.md)
- [Memory Map](../../01-core-concepts/memory-map-master.md)

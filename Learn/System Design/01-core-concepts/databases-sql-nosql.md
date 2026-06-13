# Databases — SQL vs NoSQL

## Definition

**SQL (relational):** Structured tables, ACID transactions, joins.
**NoSQL:** Flexible schemas, horizontal scale, eventual consistency models.

---

## When to Use What

| Need | Choice |
|------|--------|
| ACID transactions | PostgreSQL, MySQL |
| Complex joins, analytics | PostgreSQL, warehouse |
| Massive key-value writes | DynamoDB, Cassandra |
| Document / flexible schema | MongoDB |
| Time-series | TimescaleDB, InfluxDB |
| Graph relationships | Neo4j |
| Full-text + vectors | Elasticsearch, pgvector |

---

## Indexing

- B-tree indexes for equality and range queries
- Composite indexes: `(tenant_id, created_at)` — leftmost prefix rule
- Covering indexes avoid table lookups
- Avoid over-indexing — slows writes

---

## Replication

| Model | Description |
|-------|-------------|
| Leader-follower | Writes to primary, async/sync replicate to replicas |
| Multi-leader | Writes to multiple nodes — conflict resolution needed |
| Leaderless | Quorum reads/writes (Dynamo-style) |

**Read replicas:** Scale reads; replication lag causes stale reads.

---

## Partitioning / Sharding

- Split data across nodes by shard key
- Cross-shard queries are expensive — design to avoid
- Resharding: consistent hashing, virtual nodes

---

## CAP Theorem (Senior Level)

In a partition, choose **Consistency** or **Availability** (not both for writes).

- **CP:** Strong consistency, may reject requests (banking)
- **AP:** Always available, eventual consistency (social feed)

---

## Interview Phrases

> "Postgres for transactional data; DynamoDB for high-write session store."
> "Read replicas for feed reads; writes go to primary."
> "Shard by user_id — all user data co-located."

---

## Memory Map

```
DATABASES
├── SQL: ACID, joins → Postgres
├── NoSQL: scale, flexible → Dynamo, Cassandra
├── Replication: primary + replicas (lag!)
├── Sharding: hash(key) → partition
└── CAP: partition → C or A
```

# Consistency & Availability

## Definition

**Consistency:** All nodes see the same data. **Availability:** System responds to every request.

---

## Consistency Models

| Model | Description | Example |
|-------|-------------|---------|
| Strong | Read sees latest write | Bank balance |
| Eventual | Replicas converge over time | Social likes count |
| Causal | Preserves cause-effect order | Chat messages |
| Read-your-writes | User sees own writes | Profile update |

---

## CAP Theorem

During a **network partition**, you cannot have all three of Consistency, Availability, and Partition tolerance. Partition tolerance is required in distributed systems — so you choose CP or AP.

---

## Quorum

For N replicas:
- **W** writes acknowledged by W nodes
- **R** reads from R nodes
- **R + W > N** → strong consistency possible

DynamoDB, Cassandra use tunable consistency via quorum.

---

## Conflict Resolution

| Strategy | Use |
|----------|-----|
| Last-write-wins (LWW) | Simple, may lose data |
| Version vectors | Track causality |
| CRDTs | Conflict-free replicated data types (counters, sets) |
| Application merge | Custom logic (e.g., shopping cart) |

**CRDTs:** Mention for collaborative editing (Google Docs), chat.

---

## Distributed Transactions

- **2PC:** Coordinator — blocking, doesn't scale well
- **Saga:** Choreography or orchestration with compensating transactions
- **Outbox pattern:** Write DB + event in same transaction, async publish

---

## Interview Phrases

> "Feed can be eventually consistent — 30s staleness is fine."
> "Payment ledger requires strong consistency — single leader DB."
> "We use saga pattern for order → payment → inventory."

---

## Memory Map

```
CONSISTENCY
├── Strong → banking, inventory
├── Eventual → feeds, analytics
├── CAP: partition → CP or AP
├── Quorum: R + W > N
├── Conflicts: LWW | CRDT | app merge
└── Saga: compensating transactions
```

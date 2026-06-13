# Scalability & Load Balancing

## Definition

**Scalability** is the ability of a system to handle increased load by adding resources. **Load balancing** distributes incoming traffic across multiple servers.

---

## Horizontal vs Vertical Scaling

| Type | Action | Pros | Cons |
|------|--------|------|------|
| Vertical | Bigger machine | Simple | Hardware ceiling, downtime to resize |
| Horizontal | More machines | No ceiling, fault tolerance | Requires stateless design, data sharding |

**Interview default:** Horizontal scaling for web services; vertical for databases until sharding needed.

---

## Stateless Services

- Session data in Redis, not in-memory on app server
- Any request can hit any instance behind LB
- Enables auto-scaling based on CPU/request count

---

## Load Balancing Algorithms

| Algorithm | Use when |
|-----------|----------|
| Round robin | Homogeneous servers, stateless |
| Least connections | Long-lived connections (WebSocket) |
| Consistent hashing | Cache servers, minimal redistribution on add/remove |
| Weighted | Mixed instance sizes |
| Geo-based | Multi-region, route to nearest |

**Layers:** DNS (geo) → L4 LB (TCP) → L7 LB (HTTP path routing).

---

## Auto-Scaling

- Scale on CPU, memory, request queue depth, custom metrics
- Cooldown periods to avoid thrashing
- Pre-warm before known traffic spikes (product launches)

---

## Sharding Strategies

| Strategy | Key | Good for |
|----------|-----|----------|
| Range | user_id ranges | Range queries |
| Hash | hash(user_id) % N | Even distribution |
| Geographic | region | Data locality |
| Directory | lookup service | Flexible rebalancing |

**Hot partition problem:** Celebrity users — use separate shard or cache layer.

---

## Interview Phrases

> "Services are stateless; we scale horizontally behind an ALB."
> "We shard by user_id using consistent hashing — 256 partitions initially."
> "DNS geo-routing sends users to the nearest region."

---

## Memory Map

```
SCALABILITY
├── Vertical (↑ machine) — quick, limited
├── Horizontal (↑ servers) — stateless required
├── LB: round-robin | least-conn | consistent-hash
├── Sharding: hash(user_id) → partition
└── Hot key → dedicated cache / shard
```

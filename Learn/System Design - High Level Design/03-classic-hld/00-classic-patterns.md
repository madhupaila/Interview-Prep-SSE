# Classic HLD Patterns

Reusable patterns across the 65 classic questions.

---

## Pattern 1: Read-Heavy with Cache

**Examples:** URL shortener, news feed, product catalog

```
Read → CDN/Redis → DB on miss
Write → DB → invalidate cache → async index update
```

---

## Pattern 2: Fan-Out (Social Feed)

**Examples:** Twitter, Instagram feed

| Approach | Pros | Cons |
|----------|------|------|
| Fan-out on write | Fast reads | Slow writes for celebrities |
| Fan-out on read | Fast writes | Slow reads |
| Hybrid | Best of both | More complex |

**Celebrity problem:** Pre-compute for normal users; merge celebrity tweets on read.

---

## Pattern 3: Real-Time Messaging

**Examples:** WhatsApp, Slack, Chat

- WebSocket gateway for persistent connections
- Message store: Cassandra (partition by conversation_id)
- Delivery: online via WS; offline via push notification queue
- Ordering: per-conversation sequence numbers

---

## Pattern 4: Geospatial / Matching

**Examples:** Uber, Yelp, Tinder

- Geohash or quadtree index in Redis/PostGIS
- Match drivers/riders in radius
- WebSocket for live location updates

---

## Pattern 5: Media Pipeline

**Examples:** Netflix, YouTube, Instagram

- Upload → object storage (S3)
- Transcode workers (multiple resolutions)
- CDN for delivery
- Metadata DB separate from blobs

---

## Pattern 6: Search & Indexing

**Examples:** Google search, autocomplete, Yelp search

- Inverted index (Elasticsearch)
- Autocomplete: trie or prefix index in Redis
- Crawler: BFS frontier queue + bloom filter for visited URLs

---

## Pattern 7: Distributed Coordination

**Examples:** Rate limiter, job scheduler, distributed lock

- Redis: token bucket, sorted sets for sliding window
- Leader election: ZooKeeper/etcd
- Idempotent job processing with at-least-once delivery

---

## Pattern 8: Financial / Strong Consistency

**Examples:** Stripe payments, stock trading

- ACID database per shard
- Idempotency keys on all money APIs
- Ledger pattern (append-only, double-entry)
- Saga for multi-service flows

---

## Pattern 9: Collaboration

**Examples:** Google Docs, Figma

- OT or CRDT for conflict-free editing
- WebSocket sync
- Operational transform server or peer-to-peer with server reconcile

---

## Pattern 10: Analytics Pipeline

**Examples:** Ad click aggregator, web analytics

- Event collection API (fire-and-forget)
- Kafka → stream processing (Flink) → warehouse
- Batch + real-time lambda architecture

---

## How to Pick a Pattern in Interviews

1. Identify read/write ratio
2. Identify consistency requirements
3. Identify real-time needs
4. Map to pattern above
5. Customize with scale numbers

See [questions/](questions/) for full scripts per system.

# Messaging, Queues & Streams

## Definition

**Message queues** decouple producers and consumers for async processing. **Streams** (Kafka) are durable, ordered logs with replay.

---

## Queue vs Stream

| Feature | Queue (SQS) | Stream (Kafka) |
|---------|-------------|----------------|
| Ordering | Per-queue, limited | Per-partition, guaranteed |
| Replay | No | Yes |
| Retention | Until consumed | Time/size based |
| Use case | Task processing | Event sourcing, analytics |

---

## Delivery Guarantees

| Guarantee | Meaning | Implementation |
|-----------|---------|----------------|
| At-most-once | May lose messages | No retry |
| At-least-once | May duplicate | Retry + idempotent consumer |
| Exactly-once | Hard | Kafka transactions + idempotent writes |

**Interview default:** At-least-once + idempotent consumers.

---

## Consumer Groups (Kafka)

- Multiple consumers in group share partitions
- Scale consumers up to partition count
- Rebalance on consumer join/leave

---

## Dead Letter Queue (DLQ)

- Failed messages after N retries → DLQ
- Alert on DLQ depth
- Manual replay or fix-and-reprocess

---

## Common Patterns

| Pattern | Use |
|---------|-----|
| Work queue | Distribute tasks to workers |
| Pub/sub | Broadcast events to many subscribers |
| Event sourcing | Store state changes as events |
| CQRS | Separate read/write models via events |
| Saga | Distributed transactions via compensating events |

---

## Backpressure

- Monitor queue depth
- Reject or throttle producers when consumers lag
- Scale consumers based on lag metric

---

## Interview Phrases

> "Kafka for fan-out — tweet created event consumed by timeline, notification, search indexers."
> "Idempotency keys on consumers — duplicate delivery is expected."
> "DLQ for failed jobs with alerting."

---

## Memory Map

```
MESSAGING
├── Queue (SQS): simple async tasks
├── Stream (Kafka): replay, ordering, analytics
├── Delivery: at-least-once + idempotent consumer
├── DLQ: failed messages
└── Backpressure: throttle when lag high
```

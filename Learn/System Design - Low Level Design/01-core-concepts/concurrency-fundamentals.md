# Concurrency Fundamentals — LLD

When the problem involves **multiple threads** or **shared mutable state**.

---

## Primitives

| Mechanism | Use |
|-----------|-----|
| `synchronized` method/block | Mutual exclusion, simple |
| `ReentrantLock` | tryLock, fairness, conditions |
| `volatile` | Visibility for single flag (not compound ops) |
| `AtomicInteger` | Lock-free counters |
| `ConcurrentHashMap` | Thread-safe map |
| `BlockingQueue` | Producer-consumer |

---

## Check-Then-Act Bug

```java
// UNSAFE
if (spot.isAvailable()) {
    spot.assign(vehicle);  // another thread may take spot
}

// SAFE
synchronized (spot) {
    if (!spot.isAvailable()) throw new OccupiedException();
    spot.assign(vehicle);
}
```

---

## ReadWriteLock

Many readers, few writers — e.g. config cache, leaderboard read-heavy.

---

## Thread Pool (Conceptual)

```java
ExecutorService pool = Executors.newFixedThreadPool(4);
pool.submit(() -> processJob(job));
```

Design `ThreadPoolExecutor` as LLD: task queue, worker threads, rejection policy.

---

## Interview Callout

> "park() is check-then-act on shared spots — I'll synchronize on the spot object or use per-floor locks for better concurrency."

---

## Related

- [Concurrency LLD Track](../04-concurrency-lld/questions/)
- [How to Write Code in Interview](../00-interview-framework/06-how-to-write-code-in-interview.md)

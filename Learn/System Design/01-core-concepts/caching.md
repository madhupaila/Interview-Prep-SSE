# Caching

## Definition

**Caching** stores frequently accessed data in fast storage (memory) to reduce latency and database load.

---

## Cache Patterns

| Pattern | Flow | Use when |
|---------|------|----------|
| **Cache-aside** | App reads cache → miss → read DB → write cache | Default pattern |
| **Read-through** | Cache loads from DB on miss (cache manages) | Simpler app code |
| **Write-through** | Write to cache + DB synchronously | Strong consistency needed |
| **Write-behind** | Write to cache, async flush to DB | Write burst absorption |

**Cache-aside write:** Update DB first, then invalidate (or update) cache.

---

## Cache Invalidation

> "There are only two hard things: cache invalidation and naming things."

| Strategy | Description |
|----------|-------------|
| TTL | Time-based expiry — simple, allows stale data |
| Event-driven | Invalidate on write via message/event |
| Version keys | Cache key includes version: `user:123:v5` |

---

## Cache Stampede (Thundering Herd)

**Problem:** Cache expires → thousands of requests hit DB simultaneously.

**Solutions:**
- **Locking:** One request rebuilds, others wait
- **Probabilistic early expiry:** Refresh before TTL ends
- **Request coalescing:** Singleflight pattern

---

## What to Cache

| Data | TTL | Notes |
|------|-----|-------|
| User profile | 5–60 min | Invalidate on update |
| Feed | 1–5 min | Stale OK for social |
| Static assets | Days | CDN |
| Session | 24h | Redis |
| LLM responses | Varies | Semantic cache for similar queries |

---

## CDN Caching

- Edge locations close to users
- Cache-Control headers control behavior
- Purge API for invalidation

---

## Interview Phrases

> "Cache-aside with 60s TTL — stale feed is acceptable."
> "On write, we invalidate the cache key, not update in place."
> "CDN for static media; Redis for hot API responses."

---

## Memory Map

```
CACHING
├── Patterns: aside | read-through | write-through | write-behind
├── Invalidation: TTL | event | version key
├── Stampede fix: lock | early refresh | singleflight
├── Redis: sessions, feeds, rate limits
└── CDN: static, video segments
```

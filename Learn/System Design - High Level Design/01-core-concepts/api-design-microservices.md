# API Design & Microservices

## Definition

**API design** defines how clients interact with services. **Microservices** split a monolith into independently deployable services.

---

## API Styles

| Style | Pros | Cons |
|-------|------|------|
| REST | Simple, cacheable, universal | Over/under-fetching |
| gRPC | Fast, typed, streaming | Browser support limited |
| GraphQL | Flexible queries | Complexity, caching harder |
| WebSocket | Real-time bidirectional | Connection management |

**Internal:** gRPC. **Public:** REST or GraphQL. **Real-time:** WebSocket/SSE.

---

## API Design Best Practices

- Versioning: `/v1/` in path or header
- Pagination: cursor-based for feeds (stable under writes)
- Rate limiting: per API key / user
- Idempotency: `Idempotency-Key` header for POST
- Error format: consistent JSON with error codes

---

## Microservices vs Monolith

| Monolith | Microservices |
|----------|---------------|
| Simple deploy, debug | Independent scale and deploy |
| Tight coupling risk | Network latency, distributed failures |
| Good for small teams | Good for large orgs, clear boundaries |

**Senior take:** Start monolith; extract services when scaling or team boundaries demand it.

---

## Resilience Patterns

| Pattern | Purpose |
|---------|---------|
| Circuit breaker | Stop calling failing service |
| Retry + exponential backoff | Transient failures |
| Timeout | Prevent hung requests |
| Bulkhead | Isolate thread pools per dependency |
| Saga | Multi-service transactions via compensating actions |

---

## BFF (Backend for Frontend)

- Separate API layer per client type (mobile vs web)
- Aggregates microservice calls
- Reduces chatty client requests

---

## Service Mesh

- Sidecar proxy (Envoy) per pod
- mTLS, retries, observability
- Worth it at 20+ services; overkill early

---

## Interview Phrases

> "Public REST API; internal gRPC between services."
> "Circuit breaker on payment service — fail fast, don't cascade."
> "Cursor pagination on feed — `?cursor=xyz&limit=20`."

---

## Memory Map

```
API / MICROSERVICES
├── REST (public) | gRPC (internal) | GraphQL (flexible)
├── Resilience: circuit breaker | retry | timeout
├── Monolith → extract when scale/team needs
├── BFF: per-client aggregation
└── Idempotency keys on writes
```

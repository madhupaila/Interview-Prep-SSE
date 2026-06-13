# Rate Limiter (Concurrent)

**Track:** Concurrency LLD  
**Companies:** Stripe, Cloudflare  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-X08-rate-limiter-concurrent.md](../../../Case Studies/lld/concurrency/CS-LLD-X08-rate-limiter-concurrent.md)
> **End-to-end pair:** [Distributed Rate Limiter](../../../Case Studies/paired/CS-PAIR-18-distributed-rate-limiter.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Stripe rate limiter and Envoy local rate limit. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design distributed-safe token bucket rate limiter with atomic updates.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Rate Limiter (Concurrent)? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Lock vs synchronized? | Justify choice |
| 5 | Deadlock prevention? | Ordering or timeout |
| 6 | Fairness? | Document starvation risk |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- ConcurrentRateLimiter handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via TokenBucket interface at variation points
- Constructor injection for testability
- Correctness under concurrent access — no data races
- Avoid deadlock — consistent lock ordering where multiple locks

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `RateLimiter` | Facade |
| `TokenBucket` | Atomic tokens |
| `Clock` | Time source |
| `ClientKey` | Limiter key |

**Nouns → classes:** `RateLimiter`, `TokenBucket`, `Clock`, `ClientKey`  
**Verbs → methods:** `allowRequest()`, `reset()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ConcurrentRateLimiter│──────>│ Concurrency      │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteConcurrency│
│  RateLimiter        │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  TokenBucket        │────>│  Clock           │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ConcurrentRateLimiter {
        +boolean allowRequest(String clientKey)
        +void reset(String clientKey)
    }
    class RateLimiter {
        +allowRequest(String) boolean
    }
    class TokenBucket {
        -tokens: double
        +tryConsume() boolean
    }
    class Clock {
        +execute() void
    }
    class ClientKey {
        +execute() void
    }
    ConcurrentRateLimiter --> RateLimiter
```

---

## 6. Public API / Key Methods

```java
public class ConcurrentRateLimiter {
    public boolean allowRequest(String clientKey);
    public void reset(String clientKey);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Concurrency | Thread-safe design for Rate Limiter (Concurrent) |
| Synchronization | Locks, volatile, or concurrent collections |

**SOLID:**
- **S:** ConcurrentRateLimiter orchestrates; entities hold state
- **O:** New behavior via new TokenBucket impl
- **D:** Depend on TokenBucket interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ConcurrentRateLimiter
participant D as RateLimiter
U->>S: allowRequest()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ConcurrentRateLimiter
U->>S: allowRequest(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Concurrency` implementation plugs in at runtime — no change to `ConcurrentRateLimiter`."
>
> "Add new `RateLimiter` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Concurrency | Concurrency — 2+ behaviors |
| State | enum | State pattern | enum for simple lifecycles |
| Storage | in-memory | Repository | in-memory MVP |
| API return | primitive | domain object | domain object — type safety |

---

## 11. Concurrency & Edge Cases

- Identify shared mutable state across threads
- Use synchronized, Lock, or concurrent collections appropriately
- Avoid deadlock — consistent lock acquisition order
- Document happens-before relationships for interview clarity

---

## 12. Interview Answer Script (15 min)

> "I'll design Rate Limiter (Concurrent) — clarify in-memory scope and MVP flows first."
>
> "Entities: `RateLimiter`, `TokenBucket`, `Clock`, `ClientKey`. Domain structure separate from `ConcurrentRateLimiter` orchestration."
>
> "Problem: Design distributed-safe token bucket rate limiter with atomic updates."
>
> "`RateLimiter` — facade; owns its own invariants."
>
> "`TokenBucket` — atomic tokens; owns its own invariants."
>
> "`Clock` — time source; owns its own invariants."
>
> "`ConcurrentRateLimiter` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Concurrency` in isolation?
2. How would you extend Rate Limiter (Concurrent) without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Concurrency LLD track](../../04-concurrency-lld/README.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/concurrency/rate-limiter-concurrent/) (full)

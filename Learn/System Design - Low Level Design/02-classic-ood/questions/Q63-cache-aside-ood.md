# Cache-Aside Pattern (Object)

**Track:** Classic OOD  
**Companies:** Amazon, Redis Labs  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O63-cache-aside-ood.md](../../../Case Studies/lld/classic-ood/CS-LLD-O63-cache-aside-ood.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Redis cache-aside at object level. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design cache-aside loader: read-through, write-invalidate, stampede guard.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Cache-Aside Pattern (Object)? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design cache-aside loader? | Include in MVP — Design cache-aside loader |
| 5 | Requirement: read-through? | Include in MVP — read-through |
| 6 | Requirement: write-invalidate? | Include in MVP — write-invalidate |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- CacheAsideService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via CacheLoader interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Cache` | Fast store |
| `DataStore` | Authoritative DB |
| `CacheLoader` | Miss handler |
| `CacheKey` | Lookup id |
| `InvalidationPolicy` | TTL/event |

**Nouns → classes:** `Cache`, `DataStore`, `CacheLoader`, `CacheKey`, `InvalidationPolicy`  
**Verbs → methods:** `get()`, `put()`, `size()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  CacheAsideService  │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Cache              │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  DataStore          │────>│  CacheLoader     │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class CacheAsideService {
        +V get(K key)
        +void put(K key, V value)
        +int size()
    }
    class Cache {
        +execute() void
    }
    class DataStore {
        +execute() void
    }
    class CacheLoader {
        +execute() void
    }
    class CacheKey {
        +execute() void
    }
    class InvalidationPolicy {
        <<interface>>
        +apply() void
    }
    CacheAsideService --> Cache
```

---

## 6. Public API / Key Methods

```java
public class CacheAsideService {
    public V get(K key);
    public void put(K key, V value);
    public int size();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable algorithms |
| Repository | Persistence abstraction |

**SOLID:**
- **S:** CacheAsideService orchestrates; entities hold state
- **O:** New behavior via new CacheLoader impl
- **D:** Depend on CacheLoader interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CacheAsideService
participant D as Cache
U->>S: get()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CacheAsideService
U->>S: get(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `CacheAsideService`."
>
> "Add new `Cache` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Strategy | Strategy — 2+ behaviors |
| State | enum | State pattern | enum for simple lifecycles |
| Storage | in-memory | Repository | in-memory MVP |
| API return | primitive | domain object | domain object — type safety |

---

## 11. Concurrency & Edge Cases

- Single-threaded MVP unless clarifying assumes concurrent access
- If multi-user: synchronize on mutable aggregates or use concurrent collections
- Fail fast on invalid input with domain exceptions
- Idempotent retries where duplicate operations are possible

---

## 12. Interview Answer Script (15 min)

> "I'll design Cache-Aside Pattern (Object) — clarify in-memory scope and MVP flows first."
>
> "Entities: `Cache`, `DataStore`, `CacheLoader`, `CacheKey`, `InvalidationPolicy`. Domain structure separate from `CacheAsideService` orchestration."
>
> "Problem: Design cache-aside loader: read-through, write-invalidate, stampede guard."
>
> "`Cache` — fast store; owns its own invariants."
>
> "`DataStore` — authoritative db; owns its own invariants."
>
> "`CacheLoader` — miss handler; owns its own invariants."
>
> "`CacheAsideService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Cache-Aside Pattern (Object) without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/cache-aside-ood/README.md) (full)

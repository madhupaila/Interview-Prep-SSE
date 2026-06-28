# Concurrent LRU Cache

**Track:** Concurrency LLD  
**Companies:** Amazon, Meta  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-LLD-X06-concurrent-lru-cache.md](../../../Case Studies/lld/concurrency/CS-LLD-X06-concurrent-lru-cache.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Caffeine cache concurrent eviction. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design thread-safe LRU cache with fine-grained locking or ConcurrentHashMap.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Concurrent LRU Cache? | Core entities + 2 primary flows; extensions deferred |
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
- ConcurrentLRUCache handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ConcurrentLRUCache interface at variation points
- Constructor injection for testability
- Correctness under concurrent access — no data races
- Avoid deadlock — consistent lock ordering where multiple locks

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `ConcurrentLRUCache` | Facade |
| `Segment` | Lock shard |
| `Node` | DLL entry |
| `EvictionPolicy` | LRU order |

**Nouns → classes:** `ConcurrentLRUCache`, `Segment`, `Node`, `EvictionPolicy`  
**Verbs → methods:** `get()`, `put()`, `size()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ConcurrentLRUCache │──────>│ Concurrency      │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteConcurrency│
│  ConcurrentLRUCache │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Segment            │────>│  Node            │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ConcurrentLRUCache {
        +V get(K key)
        +void put(K key, V value)
        +int size()
    }
    class Segment {
        +execute() void
    }
    class Node {
        -key: K
        -value: V
        -prev, next: Node
    }
    class EvictionPolicy {
        <<interface>>
        +apply() void
    }
```

---

## 6. Public API / Key Methods

```java
public class ConcurrentLRUCache {
    public V get(K key);
    public void put(K key, V value);
    public int size();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Concurrency | Thread-safe design for Concurrent LRU Cache |
| Synchronization | Locks, volatile, or concurrent collections |

**SOLID:**
- **S:** ConcurrentLRUCache orchestrates; entities hold state
- **O:** New behavior via new ConcurrentLRUCache impl
- **D:** Depend on ConcurrentLRUCache interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ConcurrentLRUCache
participant D as ConcurrentLRUCache
U->>S: get()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ConcurrentLRUCache
U->>S: get(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Concurrency` implementation plugs in at runtime — no change to `ConcurrentLRUCache`."
>
> "Add new `ConcurrentLRUCache` subtypes or enum values for new categories — Open-Closed."

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

- Synchronize get/put or use read-write lock if read-heavy
- Eviction during get must be atomic with list reorder
- Alternative: ConcurrentHashMap + synchronized list head/tail
- Document lock granularity tradeoff: whole cache vs per-segment

---

## 12. Interview Answer Script (15 min)

> "I'll design Concurrent LRU Cache — clarify in-memory scope and MVP flows first."
>
> "Entities: `ConcurrentLRUCache`, `Segment`, `Node`, `EvictionPolicy`. Domain structure separate from `ConcurrentLRUCache` orchestration."
>
> "Problem: Design thread-safe LRU cache with fine-grained locking or ConcurrentHashMap."
>
> "`ConcurrentLRUCache` — facade; owns its own invariants."
>
> "`Segment` — lock shard; owns its own invariants."
>
> "`Node` — dll entry; owns its own invariants."
>
> "`ConcurrentLRUCache` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Concurrency` in isolation?
2. How would you extend Concurrent LRU Cache without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Concurrency LLD track](../../04-concurrency-lld/README.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/concurrency/concurrent-lru-cache/README.md) (full)

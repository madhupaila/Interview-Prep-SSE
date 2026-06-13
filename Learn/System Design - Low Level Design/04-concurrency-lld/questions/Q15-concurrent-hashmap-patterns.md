# ConcurrentHashMap Usage Patterns

**Track:** Concurrency LLD  
**Companies:** Amazon, Google  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-X15-concurrent-hashmap-patterns.md](../../../Case Studies/lld/concurrency/CS-LLD-X15-concurrent-hashmap-patterns.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the ConcurrentHashMap Usage Patterns domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design patterns using ConcurrentHashMap: computeIfAbsent, size, iteration safety.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for ConcurrentHashMap Usage Patterns? | Core entities + 2 primary flows; extensions deferred |
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
- ConcurrentMapPatterns handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ConcurrentHashMap interface at variation points
- Constructor injection for testability
- Correctness under concurrent access — no data races
- Avoid deadlock — consistent lock ordering where multiple locks

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `ConcurrentHashMap` | Map |
| `CacheLoader` | computeIfAbsent |
| `Counter` | Atomic increment |
| `StripedLock` | Segment sync |

**Nouns → classes:** `ConcurrentHashMap`, `CacheLoader`, `Counter`, `StripedLock`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ConcurrentMapPatterns│──────>│ Concurrency      │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteConcurrency│
│  ConcurrentHashMap  │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  CacheLoader        │────>│  Counter         │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ConcurrentMapPatterns {
        +void create(ConcurrentHashMap entity)
        +Optional<ConcurrentHashMap> getById(String id)
        +List<ConcurrentHashMap> listAll()
        +void delete(String id)
    }
    class ConcurrentHashMap {
        +execute() void
    }
    class CacheLoader {
        +execute() void
    }
    class Counter {
        +execute() void
    }
    class StripedLock {
        +execute() void
    }
    ConcurrentMapPatterns --> ConcurrentHashMap
```

---

## 6. Public API / Key Methods

```java
public class ConcurrentMapPatterns {
    public void create(ConcurrentHashMap entity);
    public Optional<ConcurrentHashMap> getById(String id);
    public List<ConcurrentHashMap> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Concurrency | Thread-safe design for ConcurrentHashMap Usage Patterns |
| Synchronization | Locks, volatile, or concurrent collections |

**SOLID:**
- **S:** ConcurrentMapPatterns orchestrates; entities hold state
- **O:** New behavior via new ConcurrentHashMap impl
- **D:** Depend on ConcurrentHashMap interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ConcurrentMapPatterns
participant D as ConcurrentHashMap
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ConcurrentMapPatterns
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Concurrency` implementation plugs in at runtime — no change to `ConcurrentMapPatterns`."
>
> "Add new `ConcurrentHashMap` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design ConcurrentHashMap Usage Patterns — clarify in-memory scope and MVP flows first."
>
> "Entities: `ConcurrentHashMap`, `CacheLoader`, `Counter`, `StripedLock`. Domain structure separate from `ConcurrentMapPatterns` orchestration."
>
> "Problem: Design patterns using ConcurrentHashMap: computeIfAbsent, size, iteration safety."
>
> "`ConcurrentHashMap` — map; owns its own invariants."
>
> "`CacheLoader` — computeifabsent; owns its own invariants."
>
> "`Counter` — atomic increment; owns its own invariants."
>
> "`ConcurrentMapPatterns` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Concurrency` in isolation?
2. How would you extend ConcurrentHashMap Usage Patterns without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Concurrency LLD track](../../04-concurrency-lld/README.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/concurrency/concurrent-hashmap-patterns/) (full)

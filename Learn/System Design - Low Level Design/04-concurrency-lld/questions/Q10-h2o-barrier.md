# H2O Barrier

**Track:** Concurrency LLD  
**Companies:** Google, Amazon  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-X10-h2o-barrier.md](../../../Case Studies/lld/concurrency/CS-LLD-X10-h2o-barrier.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the H2O Barrier domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design barrier synchronizing H, O threads to form H2O molecules.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for H2O Barrier? | Core entities + 2 primary flows; extensions deferred |
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
- H2OSynchronizer handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via H2O interface at variation points
- Constructor injection for testability
- Correctness under concurrent access — no data races
- Avoid deadlock — consistent lock ordering where multiple locks

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `H2O` | Barrier |
| `HydrogenThread` | H atom |
| `OxygenThread` | O atom |
| `Molecule` | Output unit |

**Nouns → classes:** `H2O`, `HydrogenThread`, `OxygenThread`, `Molecule`  
**Verbs → methods:** `addComment()`, `getThread()`, `upvote()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  H2OSynchronizer    │──────>│ Concurrency      │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteConcurrency│
│  H2O                │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  HydrogenThread     │────>│  OxygenThread    │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class H2OSynchronizer {
        +Comment addComment(String postId, String text, String parentId)
        +List<Comment> getThread(String postId)
        +void upvote(String commentId)
    }
    class H2O {
        +execute() void
    }
    class HydrogenThread {
        +execute() void
    }
    class OxygenThread {
        +execute() void
    }
    class Molecule {
        +execute() void
    }
    H2OSynchronizer --> H2O
```

---

## 6. Public API / Key Methods

```java
public class H2OSynchronizer {
    public Comment addComment(String postId, String text, String parentId);
    public List<Comment> getThread(String postId);
    public void upvote(String commentId);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Concurrency | Thread-safe design for H2O Barrier |
| Synchronization | Locks, volatile, or concurrent collections |

**SOLID:**
- **S:** H2OSynchronizer orchestrates; entities hold state
- **O:** New behavior via new H2O impl
- **D:** Depend on H2O interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as H2OSynchronizer
participant D as H2O
U->>S: addComment()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as H2OSynchronizer
U->>S: addComment(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Concurrency` implementation plugs in at runtime — no change to `H2OSynchronizer`."
>
> "Add new `H2O` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design H2O Barrier — clarify in-memory scope and MVP flows first."
>
> "Entities: `H2O`, `HydrogenThread`, `OxygenThread`, `Molecule`. Domain structure separate from `H2OSynchronizer` orchestration."
>
> "Problem: Design barrier synchronizing H, O threads to form H2O molecules."
>
> "`H2O` — barrier; owns its own invariants."
>
> "`HydrogenThread` — h atom; owns its own invariants."
>
> "`OxygenThread` — o atom; owns its own invariants."
>
> "`H2OSynchronizer` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Concurrency` in isolation?
2. How would you extend H2O Barrier without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Concurrency LLD track](../../04-concurrency-lld/README.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/concurrency/h2o-barrier/README.md) (full)

# Download Manager

**Track:** Concurrency LLD  
**Companies:** Microsoft, Apple  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-X12-download-manager.md](../../../Case Studies/lld/concurrency/CS-LLD-X12-download-manager.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Internet Download Manager parallel chunks. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design concurrent download manager with chunks, progress, pause/resume.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Download Manager? | Core entities + 2 primary flows; extensions deferred |
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
- DownloadManager handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via DownloadManager interface at variation points
- Constructor injection for testability
- Correctness under concurrent access — no data races
- Avoid deadlock — consistent lock ordering where multiple locks

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `DownloadTask` | File job |
| `Chunk` | Byte range |
| `WorkerPool` | Parallel fetch |
| `ProgressTracker` | Status |

**Nouns → classes:** `DownloadTask`, `Chunk`, `WorkerPool`, `ProgressTracker`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  DownloadManager    │──────>│ Concurrency      │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteConcurrency│
│  DownloadTask       │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Chunk              │────>│  WorkerPool      │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class DownloadManager {
        +void create(DownloadTask entity)
        +Optional<DownloadTask> getById(String id)
        +List<DownloadTask> listAll()
        +void delete(String id)
    }
    class DownloadTask {
        +execute() void
    }
    class Chunk {
        +execute() void
    }
    class WorkerPool {
        +execute() void
    }
    class ProgressTracker {
        <<enumeration>>
    }
    DownloadManager --> DownloadTask
```

---

## 6. Public API / Key Methods

```java
public class DownloadManager {
    public void create(DownloadTask entity);
    public Optional<DownloadTask> getById(String id);
    public List<DownloadTask> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Concurrency | Thread-safe design for Download Manager |
| Synchronization | Locks, volatile, or concurrent collections |

**SOLID:**
- **S:** DownloadManager orchestrates; entities hold state
- **O:** New behavior via new DownloadManager impl
- **D:** Depend on DownloadManager interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as DownloadManager
participant D as DownloadTask
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as DownloadManager
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Concurrency` implementation plugs in at runtime — no change to `DownloadManager`."
>
> "Add new `DownloadTask` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Download Manager — clarify in-memory scope and MVP flows first."
>
> "Entities: `DownloadTask`, `Chunk`, `WorkerPool`, `ProgressTracker`. Domain structure separate from `DownloadManager` orchestration."
>
> "Problem: Design concurrent download manager with chunks, progress, pause/resume."
>
> "`DownloadTask` — file job; owns its own invariants."
>
> "`Chunk` — byte range; owns its own invariants."
>
> "`WorkerPool` — parallel fetch; owns its own invariants."
>
> "`DownloadManager` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Concurrency` in isolation?
2. How would you extend Download Manager without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Concurrency LLD track](../../04-concurrency-lld/README.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/concurrency/download-manager/) (full)

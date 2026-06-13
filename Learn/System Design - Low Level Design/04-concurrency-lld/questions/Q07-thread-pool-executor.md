# Thread Pool Executor

**Track:** Concurrency LLD  
**Companies:** Amazon, Google  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-LLD-X07-thread-pool-executor.md](../../../Case Studies/lld/concurrency/CS-LLD-X07-thread-pool-executor.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Java ExecutorService and ForkJoinPool. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design fixed thread pool with task queue, worker threads, rejection policy.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Thread Pool Executor? | Core entities + 2 primary user flows |
| 2 | Persistence required? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded access? | Yes if multiple users/gates — else single-threaded |
| 4 | Pool size? | Fixed N worker threads |
| 5 | Queue type? | Bounded BlockingQueue |
| 6 | Rejection policy? | Abort, caller-runs, or block |
| 7 | Shutdown? | Graceful drain then interrupt |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- ThreadPoolExecutor handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ThreadPool interface at variation points
- Constructor injection for testability
- Correctness under concurrent access — no data races
- Avoid deadlock — consistent lock ordering where multiple locks

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `ThreadPool` | Worker set |
| `TaskQueue` | Pending work |
| `Worker` | Runnable loop |
| `RejectedExecutionHandler` | Overflow policy |

**Nouns → classes:** `ThreadPool`, `TaskQueue`, `Worker`, `RejectedExecutionHandler`  
**Verbs → methods:** `addComment()`, `getThread()`, `upvote()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ThreadPoolExecutor │──────>│ Concurrency      │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteConcurrency│
│  ThreadPool         │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  TaskQueue          │────>│  Worker          │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ThreadPoolExecutor {
        +Comment addComment(String postId, String text, String parentId)
        +List<Comment> getThread(String postId)
        +void upvote(String commentId)
    }
    class ThreadPool {
        +execute() void
    }
    class TaskQueue {
        +execute() void
    }
    class Worker {
        +execute() void
    }
    class RejectedExecutionHandler {
        +execute() void
    }
    ThreadPoolExecutor --> ThreadPool
```

---

## 6. Public API / Key Methods

```java
public class ThreadPoolExecutor {
    public Comment addComment(String postId, String text, String parentId);
    public List<Comment> getThread(String postId);
    public void upvote(String commentId);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Concurrency | Thread-safe design for Thread Pool Executor |
| Synchronization | Locks, volatile, or concurrent collections |

**SOLID:**
- **S:** ThreadPoolExecutor orchestrates; entities hold state
- **O:** New behavior via new ThreadPool impl
- **D:** Depend on ThreadPool interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ThreadPoolExecutor
participant D as ThreadPool
U->>S: addComment()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ThreadPoolExecutor
U->>S: addComment(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Concurrency` implementation plugs in at runtime — no change to `ThreadPoolExecutor`."
>
> "Add new `ThreadPool` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Thread Pool Executor — clarify in-memory scope and MVP flows first."
>
> "Entities: `ThreadPool`, `TaskQueue`, `Worker`, `RejectedExecutionHandler`. Domain structure separate from `ThreadPoolExecutor` orchestration."
>
> "Problem: Design fixed thread pool with task queue, worker threads, rejection policy."
>
> "`ThreadPool` — worker set; owns its own invariants."
>
> "`TaskQueue` — pending work; owns its own invariants."
>
> "`Worker` — runnable loop; owns its own invariants."
>
> "`ThreadPoolExecutor` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Concurrency` in isolation?
2. How would you extend Thread Pool Executor without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Concurrency LLD track](../../04-concurrency-lld/README.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/concurrency/thread-pool-executor/) (full)

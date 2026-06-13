# Job Scheduler with Worker Pool

**Track:** Concurrency LLD  
**Companies:** Amazon, Airbnb  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-LLD-X13-job-scheduler-pool.md](../../../Case Studies/lld/concurrency/CS-LLD-X13-job-scheduler-pool.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Sidekiq and Celery worker pools. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design scheduler dispatching cron jobs to worker pool with at-least-once semantics.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Job Scheduler with Worker Pool? | Core entities + 2 primary flows; extensions deferred |
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
- JobSchedulerPool handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via Scheduler interface at variation points
- Constructor injection for testability
- Correctness under concurrent access — no data races
- Avoid deadlock — consistent lock ordering where multiple locks

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Scheduler` | Cron trigger |
| `Job` | Unit of work |
| `WorkerPool` | Executors |
| `JobStore` | Persistence stub |

**Nouns → classes:** `Scheduler`, `Job`, `WorkerPool`, `JobStore`  
**Verbs → methods:** `schedule()`, `findAvailability()`, `cancelMeeting()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  JobSchedulerPool   │──────>│ Concurrency      │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteConcurrency│
│  Scheduler          │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Job                │────>│  WorkerPool      │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class JobSchedulerPool {
        +Meeting schedule(Meeting meeting)
        +List<TimeSlot> findAvailability(List<Participant> users)
        +void cancelMeeting(String meetingId)
    }
    class Scheduler {
        +execute() void
    }
    class Job {
        +execute() void
    }
    class WorkerPool {
        +execute() void
    }
    class JobStore {
        +execute() void
    }
    JobSchedulerPool --> Scheduler
```

---

## 6. Public API / Key Methods

```java
public class JobSchedulerPool {
    public Meeting schedule(Meeting meeting);
    public List<TimeSlot> findAvailability(List<Participant> users);
    public void cancelMeeting(String meetingId);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Concurrency | Thread-safe design for Job Scheduler with Worker Pool |
| Synchronization | Locks, volatile, or concurrent collections |

**SOLID:**
- **S:** JobSchedulerPool orchestrates; entities hold state
- **O:** New behavior via new Scheduler impl
- **D:** Depend on Scheduler interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as JobSchedulerPool
participant D as Scheduler
U->>S: schedule()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as JobSchedulerPool
U->>S: schedule(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Concurrency` implementation plugs in at runtime — no change to `JobSchedulerPool`."
>
> "Add new `Scheduler` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Job Scheduler with Worker Pool — clarify in-memory scope and MVP flows first."
>
> "Entities: `Scheduler`, `Job`, `WorkerPool`, `JobStore`. Domain structure separate from `JobSchedulerPool` orchestration."
>
> "Problem: Design scheduler dispatching cron jobs to worker pool with at-least-once semantics."
>
> "`Scheduler` — cron trigger; owns its own invariants."
>
> "`Job` — unit of work; owns its own invariants."
>
> "`WorkerPool` — executors; owns its own invariants."
>
> "`JobSchedulerPool` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Concurrency` in isolation?
2. How would you extend Job Scheduler with Worker Pool without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Concurrency LLD track](../../04-concurrency-lld/README.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/concurrency/job-scheduler-pool/) (full)

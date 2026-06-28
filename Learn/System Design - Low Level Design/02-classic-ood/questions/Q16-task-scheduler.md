# Task Scheduler

**Track:** Classic OOD  
**Companies:** Amazon, Google, Microsoft  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O16-task-scheduler.md](../../../Case Studies/lld/classic-ood/CS-LLD-O16-task-scheduler.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Task Scheduler domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design task scheduler executing jobs by priority or cron expression.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Task Scheduler? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design task scheduler executing jobs by ? | Include in MVP — Design task scheduler executing jobs by priority o |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- TaskScheduler handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via SchedulingPolicy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Scheduler` | Job runner |
| `Task` | Runnable unit |
| `JobQueue` | Priority queue |
| `Worker` | Execution thread |
| `CronExpression` | Schedule parser |

**Nouns → classes:** `Scheduler`, `Task`, `JobQueue`, `Worker`, `CronExpression`  
**Verbs → methods:** `schedule()`, `findAvailability()`, `cancelMeeting()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  TaskScheduler      │──────>│ Queue            │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteQueue    │
│  Scheduler          │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Task               │────>│  JobQueue        │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class TaskScheduler {
        +Meeting schedule(Meeting meeting)
        +List<TimeSlot> findAvailability(List<Participant> users)
        +void cancelMeeting(String meetingId)
    }
    class Scheduler {
        +execute() void
    }
    class Task {
        +execute() void
    }
    class JobQueue {
        +enqueue() void
        +dequeue() Object
    }
    class Worker {
        +execute() void
    }
    class CronExpression {
        +execute() void
    }
    TaskScheduler --> Scheduler
```

---

## 6. Public API / Key Methods

```java
public class TaskScheduler {
    public Meeting schedule(Meeting meeting);
    public List<TimeSlot> findAvailability(List<Participant> users);
    public void cancelMeeting(String meetingId);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Queue | FIFO ordering of work items |

**SOLID:**
- **S:** TaskScheduler orchestrates; entities hold state
- **O:** New behavior via new SchedulingPolicy impl
- **D:** Depend on SchedulingPolicy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as TaskScheduler
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
participant S as TaskScheduler
U->>S: schedule(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Queue` implementation plugs in at runtime — no change to `TaskScheduler`."
>
> "Add new `Scheduler` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Queue | Queue — 2+ behaviors |
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

> "I'll design Task Scheduler — clarify in-memory scope and MVP flows first."
>
> "Entities: `Scheduler`, `Task`, `JobQueue`, `Worker`, `CronExpression`. Domain structure separate from `TaskScheduler` orchestration."
>
> "Problem: Design task scheduler executing jobs by priority or cron expression."
>
> "`Scheduler` — job runner; owns its own invariants."
>
> "`Task` — runnable unit; owns its own invariants."
>
> "`JobQueue` — priority queue; owns its own invariants."
>
> "`TaskScheduler` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Queue` in isolation?
2. How would you extend Task Scheduler without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/task-scheduler/Demo.java) (full)

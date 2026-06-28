# Course Registration

**Track:** Classic OOD  
**Companies:** Coursera, Amazon  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O34-course-registration.md](../../../Case Studies/lld/classic-ood/CS-LLD-O34-course-registration.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Course Registration domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design university registration: courses, seats, waitlist, prerequisites.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Course Registration? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design university registration? | Include in MVP — Design university registration |
| 5 | Requirement: courses? | Include in MVP — courses |
| 6 | Requirement: waitlist? | Include in MVP — waitlist |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- RegistrationService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via PrerequisiteChecker interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Student` | Enrollee |
| `Course` | Offering |
| `Section` | Time slot |
| `Enrollment` | Seat record |
| `Waitlist` | FIFO queue |
| `PrerequisiteChecker` | Rules |

**Nouns → classes:** `Student`, `Course`, `Section`, `Enrollment`, `Waitlist`, `PrerequisiteChecker`  
**Verbs → methods:** `holdSeats()`, `confirm()`, `releaseHold()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  RegistrationService│──────>│ Queue            │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteQueue    │
│  Student            │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Course             │────>│  Section         │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class RegistrationService {
        +SeatLock holdSeats(Show show, List<Seat> seats)
        +Booking confirm(SeatLock lock)
        +void releaseHold(SeatLock lock)
    }
    class Student {
        +execute() void
    }
    class Course {
        +execute() void
    }
    class Section {
        +execute() void
    }
    class Enrollment {
        +execute() void
    }
    class Waitlist {
        +enqueue() void
        +dequeue() Object
    }
    class PrerequisiteChecker {
        +execute() void
    }
    RegistrationService --> Student
```

---

## 6. Public API / Key Methods

```java
public class RegistrationService {
    public SeatLock holdSeats(Show show, List<Seat> seats);
    public Booking confirm(SeatLock lock);
    public void releaseHold(SeatLock lock);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Queue | FIFO ordering of work items |

**SOLID:**
- **S:** RegistrationService orchestrates; entities hold state
- **O:** New behavior via new PrerequisiteChecker impl
- **D:** Depend on PrerequisiteChecker interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as RegistrationService
participant D as Student
U->>S: holdSeats()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as RegistrationService
U->>S: holdSeats(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Queue` implementation plugs in at runtime — no change to `RegistrationService`."
>
> "Add new `Student` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Course Registration — clarify in-memory scope and MVP flows first."
>
> "Entities: `Student`, `Course`, `Section`, `Enrollment`, `Waitlist`, `PrerequisiteChecker`. Domain structure separate from `RegistrationService` orchestration."
>
> "Problem: Design university registration: courses, seats, waitlist, prerequisites."
>
> "`Student` — enrollee; owns its own invariants."
>
> "`Course` — offering; owns its own invariants."
>
> "`Section` — time slot; owns its own invariants."
>
> "`RegistrationService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Queue` in isolation?
2. How would you extend Course Registration without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/course-registration/README.md) (full)

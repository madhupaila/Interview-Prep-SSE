# Bus Transit System

**Track:** Classic OOD  
**Companies:** City transit  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O54-bus-transit.md](../../../Case Studies/lld/classic-ood/CS-LLD-O54-bus-transit.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Bus Transit System domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design bus routes, stops, schedules, real-time ETA stub.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Bus Transit System? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design bus routes? | Include in MVP — Design bus routes |
| 5 | Requirement: schedules? | Include in MVP — schedules |
| 6 | Requirement: real-time ETA stub.? | Include in MVP — real-time ETA stub. |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- TransitService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ETAEstimator interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Route` | Line path |
| `Bus` | Vehicle |
| `Stop` | Station |
| `Schedule` | Timetable |
| `Trip` | Active run |
| `ETAEstimator` | Arrival calc |

**Nouns → classes:** `Route`, `Bus`, `Stop`, `Schedule`, `Trip`, `ETAEstimator`  
**Verbs → methods:** `schedule()`, `findAvailability()`, `cancelMeeting()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  TransitService     │──────>│ Mediator         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteMediator │
│  Route              │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Bus                │────>│  Stop            │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class TransitService {
        +Meeting schedule(Meeting meeting)
        +List<TimeSlot> findAvailability(List<Participant> users)
        +void cancelMeeting(String meetingId)
    }
    class Route {
        +execute() void
    }
    class Bus {
        +execute() void
    }
    class Stop {
        +execute() void
    }
    class Schedule {
        +execute() void
    }
    class Trip {
        -status: TripStatus
        +complete() void
    }
    class ETAEstimator {
        +execute() void
    }
    TransitService --> Route
```

---

## 6. Public API / Key Methods

```java
public class TransitService {
    public Meeting schedule(Meeting meeting);
    public List<TimeSlot> findAvailability(List<Participant> users);
    public void cancelMeeting(String meetingId);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Mediator | Decoupled communication |

**SOLID:**
- **S:** TransitService orchestrates; entities hold state
- **O:** New behavior via new ETAEstimator impl
- **D:** Depend on ETAEstimator interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as TransitService
participant D as Route
U->>S: schedule()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as TransitService
U->>S: schedule(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Mediator` implementation plugs in at runtime — no change to `TransitService`."
>
> "Add new `Route` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Mediator | Mediator — 2+ behaviors |
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

> "I'll design Bus Transit System — clarify in-memory scope and MVP flows first."
>
> "Entities: `Route`, `Bus`, `Stop`, `Schedule`, `Trip`, `ETAEstimator`. Domain structure separate from `TransitService` orchestration."
>
> "Problem: Design bus routes, stops, schedules, real-time ETA stub."
>
> "`Route` — line path; owns its own invariants."
>
> "`Bus` — vehicle; owns its own invariants."
>
> "`Stop` — station; owns its own invariants."
>
> "`TransitService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Mediator` in isolation?
2. How would you extend Bus Transit System without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/bus-transit/README.md) (skeleton)

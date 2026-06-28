# Meeting Scheduler

**Track:** Classic OOD  
**Companies:** Google, Microsoft, Zoom  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O26-meeting-scheduler.md](../../../Case Studies/lld/classic-ood/CS-LLD-O26-meeting-scheduler.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Meeting Scheduler domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design meeting scheduler: propose slots, check conflicts, book room.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Meeting Scheduler? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Overbooking? | No — reject overlapping dates |
| 5 | Cancellation? | Policy-based cancel window |
| 6 | Room types? | Enum RoomType |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- SchedulerService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ConflictChecker interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Meeting` | Event |
| `Participant` | Attendee |
| `Calendar` | Availability |
| `TimeSlot` | Start/end |
| `Room` | Physical resource |
| `ConflictChecker` | Overlap detection |

**Nouns → classes:** `Meeting`, `Participant`, `Calendar`, `TimeSlot`, `Room`, `ConflictChecker`  
**Verbs → methods:** `create()`, `cancel()`, `searchAvailable()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  SchedulerService   │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Meeting            │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Participant        │────>│  Calendar        │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class SchedulerService {
        +Booking create(Guest guest, Room room, LocalDateRange dates)
        +void cancel(String bookingId)
        +List<Room> searchAvailable(RoomType type, LocalDateRange dates)
    }
    class Meeting {
        +execute() void
    }
    class Participant {
        +execute() void
    }
    class Calendar {
        +execute() void
    }
    class TimeSlot {
        +execute() void
    }
    class Room {
        +execute() void
    }
    class ConflictChecker {
        +execute() void
    }
    SchedulerService --> Meeting
```

---

## 6. Public API / Key Methods

```java
public class SchedulerService {
    public Booking create(Guest guest, Room room, LocalDateRange dates);
    public void cancel(String bookingId);
    public List<Room> searchAvailable(RoomType type, LocalDateRange dates);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in Meeting Scheduler |

**SOLID:**
- **S:** SchedulerService orchestrates; entities hold state
- **O:** New behavior via new ConflictChecker impl
- **D:** Depend on ConflictChecker interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as SchedulerService
participant D as Meeting
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as SchedulerService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `SchedulerService`."
>
> "Add new `Meeting` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Meeting Scheduler — clarify in-memory scope and MVP flows first."
>
> "Entities: `Meeting`, `Participant`, `Calendar`, `TimeSlot`, `Room`, `ConflictChecker`. Domain structure separate from `SchedulerService` orchestration."
>
> "Problem: Design meeting scheduler: propose slots, check conflicts, book room."
>
> "`Meeting` — event; owns its own invariants."
>
> "`Participant` — attendee; owns its own invariants."
>
> "`Calendar` — availability; owns its own invariants."
>
> "`SchedulerService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Meeting Scheduler without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/meeting-scheduler/Demo.java) (full)

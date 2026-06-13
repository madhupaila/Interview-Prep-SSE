# Hotel Housekeeping

**Track:** Classic OOD  
**Companies:** Marriott, Hilton  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O57-hotel-housekeeping.md](../../../Case Studies/lld/classic-ood/CS-LLD-O57-hotel-housekeeping.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Hotel Housekeeping domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design housekeeping: room status, task assignment, inspect, DND.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Hotel Housekeeping? | Core entities + 2 primary flows; extensions deferred |
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
- HousekeepingService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via TaskAssigner interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Room` | Status dirty/clean |
| `Housekeeper` | Staff |
| `CleaningTask` | Assignment |
| `RoomStatus` | VACANT/OCCUPIED/DND |
| `Inspection` | QC check |

**Nouns → classes:** `Room`, `Housekeeper`, `CleaningTask`, `RoomStatus`, `Inspection`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  HousekeepingService│──────>│ State            │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteState    │
│  Room               │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Housekeeper        │────>│  CleaningTask    │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class HousekeepingService {
        +void create(Room entity)
        +Optional<Room> getById(String id)
        +List<Room> listAll()
        +void delete(String id)
    }
    class Room {
        <<enumeration>>
    }
    class Housekeeper {
        +execute() void
    }
    class CleaningTask {
        +execute() void
    }
    class RoomStatus {
        +execute() void
    }
    class Inspection {
        +execute() void
    }
    HousekeepingService --> Room
```

---

## 6. Public API / Key Methods

```java
public class HousekeepingService {
    public void create(Room entity);
    public Optional<Room> getById(String id);
    public List<Room> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| State | Lifecycle state transitions |

**SOLID:**
- **S:** HousekeepingService orchestrates; entities hold state
- **O:** New behavior via new TaskAssigner impl
- **D:** Depend on TaskAssigner interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as HousekeepingService
participant D as Room
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as HousekeepingService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `State` implementation plugs in at runtime — no change to `HousekeepingService`."
>
> "Add new `Room` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | State | State — 2+ behaviors |
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

> "I'll design Hotel Housekeeping — clarify in-memory scope and MVP flows first."
>
> "Entities: `Room`, `Housekeeper`, `CleaningTask`, `RoomStatus`, `Inspection`. Domain structure separate from `HousekeepingService` orchestration."
>
> "Problem: Design housekeeping: room status, task assignment, inspect, DND."
>
> "`Room` — status dirty/clean; owns its own invariants."
>
> "`Housekeeper` — staff; owns its own invariants."
>
> "`CleaningTask` — assignment; owns its own invariants."
>
> "`HousekeepingService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `State` in isolation?
2. How would you extend Hotel Housekeeping without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/hotel-housekeeping/) (skeleton)

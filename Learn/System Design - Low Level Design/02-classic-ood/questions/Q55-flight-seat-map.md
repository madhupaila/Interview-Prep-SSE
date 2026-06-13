# Flight Seat Map

**Track:** Classic OOD  
**Companies:** Airlines, Expedia  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O55-flight-seat-map.md](../../../Case Studies/lld/classic-ood/CS-LLD-O55-flight-seat-map.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Flight Seat Map domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design airline seat map: seat types, selection, hold, confirm.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Flight Seat Map? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design airline seat map? | Include in MVP — Design airline seat map |
| 5 | Requirement: seat types? | Include in MVP — seat types |
| 6 | Requirement: selection? | Include in MVP — selection |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- SeatMapService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via SeatPricing interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Flight` | Segment |
| `SeatMap` | Layout grid |
| `Seat` | Row/letter |
| `SeatType` | Economy/business |
| `SeatHold` | Temporary lock |
| `Passenger` | Traveler |

**Nouns → classes:** `Flight`, `SeatMap`, `Seat`, `SeatType`, `SeatHold`, `Passenger`  
**Verbs → methods:** `holdSeats()`, `confirm()`, `releaseHold()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  SeatMapService     │──────>│ Mediator         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteMediator │
│  Flight             │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  SeatMap            │────>│  Seat            │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class SeatMapService {
        +SeatLock holdSeats(Show show, List<Seat> seats)
        +Booking confirm(SeatLock lock)
        +void releaseHold(SeatLock lock)
    }
    class Flight {
        +execute() void
    }
    class SeatMap {
        +execute() void
    }
    class Seat {
        +execute() void
    }
    class SeatType {
        +execute() void
    }
    class SeatHold {
        +execute() void
    }
    class Passenger {
        +execute() void
    }
    SeatMapService --> Flight
```

---

## 6. Public API / Key Methods

```java
public class SeatMapService {
    public SeatLock holdSeats(Show show, List<Seat> seats);
    public Booking confirm(SeatLock lock);
    public void releaseHold(SeatLock lock);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Mediator | Decoupled communication |

**SOLID:**
- **S:** SeatMapService orchestrates; entities hold state
- **O:** New behavior via new SeatPricing impl
- **D:** Depend on SeatPricing interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as SeatMapService
participant D as Flight
U->>S: holdSeats()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as SeatMapService
U->>S: holdSeats(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Mediator` implementation plugs in at runtime — no change to `SeatMapService`."
>
> "Add new `Flight` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Flight Seat Map — clarify in-memory scope and MVP flows first."
>
> "Entities: `Flight`, `SeatMap`, `Seat`, `SeatType`, `SeatHold`, `Passenger`. Domain structure separate from `SeatMapService` orchestration."
>
> "Problem: Design airline seat map: seat types, selection, hold, confirm."
>
> "`Flight` — segment; owns its own invariants."
>
> "`SeatMap` — layout grid; owns its own invariants."
>
> "`Seat` — row/letter; owns its own invariants."
>
> "`SeatMapService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Mediator` in isolation?
2. How would you extend Flight Seat Map without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/flight-seat-map/) (full)

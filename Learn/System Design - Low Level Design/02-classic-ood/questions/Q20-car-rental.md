# Car Rental System

**Track:** Classic OOD  
**Companies:** Hertz, Amazon, Enterprise  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O20-car-rental.md](../../../Case Studies/lld/classic-ood/CS-LLD-O20-car-rental.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Car Rental System domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design car rental: fleet, reservations, pickup/return, pricing.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Car Rental System? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design car rental? | Include in MVP — Design car rental |
| 5 | Requirement: reservations? | Include in MVP — reservations |
| 6 | Requirement: pickup/return? | Include in MVP — pickup/return |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Create and cancel reservations with conflict checks

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via PricingStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `RentalAgency` | Fleet owner |
| `Vehicle` | Rentable car |
| `Reservation` | Date range booking |
| `Customer` | Renter |
| `Invoice` | Charges |

**Nouns → classes:** `RentalAgency`, `Vehicle`, `Reservation`, `Customer`, `Invoice`  
**Verbs → methods:** `create()`, `cancel()`, `searchAvailable()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  RentalService      │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  RentalAgency       │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Vehicle            │────>│  Reservation     │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class RentalService {
        +Booking create(Guest guest, Room room, LocalDateRange dates)
        +void cancel(String bookingId)
        +List<Room> searchAvailable(RoomType type, LocalDateRange dates)
    }
    class RentalAgency {
        +execute() void
    }
    class Vehicle {
        -type: VehicleType
        -licensePlate: String
    }
    class Reservation {
        +execute() void
    }
    class Customer {
        +execute() void
    }
    class Invoice {
        +execute() void
    }
    RentalService --> RentalAgency
```

---

## 6. Public API / Key Methods

```java
public class RentalService {
    public Booking create(Guest guest, Room room, LocalDateRange dates);
    public void cancel(String bookingId);
    public List<Room> searchAvailable(RoomType type, LocalDateRange dates);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in Car Rental System |

**SOLID:**
- **S:** RentalService orchestrates; entities hold state
- **O:** New behavior via new PricingStrategy impl
- **D:** Depend on PricingStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as RentalService
participant D as RentalAgency
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as RentalService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `RentalService`."
>
> "Add new `RentalAgency` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Car Rental System — clarify in-memory scope and MVP flows first."
>
> "Entities: `RentalAgency`, `Vehicle`, `Reservation`, `Customer`, `Invoice`. Domain structure separate from `RentalService` orchestration."
>
> "Problem: Design car rental: fleet, reservations, pickup/return, pricing."
>
> "`RentalAgency` — fleet owner; owns its own invariants."
>
> "`Vehicle` — rentable car; owns its own invariants."
>
> "`Reservation` — date range booking; owns its own invariants."
>
> "`RentalService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Car Rental System without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/car-rental/) (full)

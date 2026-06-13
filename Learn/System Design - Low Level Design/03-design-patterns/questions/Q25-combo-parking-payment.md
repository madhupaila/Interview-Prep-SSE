# Combo — Parking + Payment

**Track:** Design Patterns  
**Companies:** Amazon, Stripe  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-LLD-P25-combo-parking-payment.md](../../../Case Studies/lld/design-patterns/CS-LLD-P25-combo-parking-payment.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Combo — Parking + Payment domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Combine Strategy (allocation + payment) and Factory (vehicle) in parking lot.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Combo — Parking + Payment? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Combine Strategy (allocation + payment) ? | Include in MVP — Combine Strategy (allocation + payment) and Factor |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Park and unpark with spot assignment

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ParkingStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `ParkingLotService` | Orchestrator |
| `ParkingStrategy` | Spot pick |
| `PaymentProcessor` | Charge |
| `VehicleFactory` | Create vehicle |
| `Ticket` | Park token |

**Nouns → classes:** `ParkingLotService`, `ParkingStrategy`, `PaymentProcessor`, `VehicleFactory`, `Ticket`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ParkingPaymentFacade│──────>│ Combo            │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteCombo    │
│  ParkingLotService  │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  ParkingStrategy    │────>│  PaymentProcessor│
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ParkingPaymentFacade {
        +void create(ParkingLot entity)
        +Optional<ParkingLot> getById(String id)
        +List<ParkingLot> listAll()
        +void delete(String id)
    }
    class ParkingLotService {
        +execute() void
    }
    class ParkingStrategy {
        <<interface>>
        +findSpot(Vehicle, List) Optional
    }
    class PaymentProcessor {
        <<interface>>
        +pay(double) void
    }
    class VehicleFactory {
        +execute() void
    }
    class Ticket {
        -id: String
        -entryTime: Instant
        +getSpot() ParkingSpot
    }
    ParkingPaymentFacade --> ParkingLotService
```

---

## 6. Public API / Key Methods

```java
public class ParkingPaymentFacade {
    public void create(ParkingLot entity);
    public Optional<ParkingLot> getById(String id);
    public List<ParkingLot> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Combo | Demonstrate Combo pattern in combo-parking-payment |

**SOLID:**
- **S:** ParkingPaymentFacade orchestrates; entities hold state
- **O:** New behavior via new ParkingStrategy impl
- **D:** Depend on ParkingStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ParkingPaymentFacade
participant D as ParkingLotService
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ParkingPaymentFacade
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Combo` implementation plugs in at runtime — no change to `ParkingPaymentFacade`."
>
> "Add new `ParkingLotService` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Combo | Combo — 2+ behaviors |
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

> "I'll design Combo — Parking + Payment — clarify in-memory scope and MVP flows first."
>
> "Entities: `ParkingLotService`, `ParkingStrategy`, `PaymentProcessor`, `VehicleFactory`, `Ticket`. Domain structure separate from `ParkingPaymentFacade` orchestration."
>
> "Problem: Combine Strategy (allocation + payment) and Factory (vehicle) in parking lot."
>
> "`ParkingLotService` — orchestrator; owns its own invariants."
>
> "`ParkingStrategy` — spot pick; owns its own invariants."
>
> "`PaymentProcessor` — charge; owns its own invariants."
>
> "`ParkingPaymentFacade` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Combo` in isolation?
2. How would you extend Combo — Parking + Payment without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/combo-parking-payment/) (full)
- [HLD counterpart](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q30-parking-lot-elevator.md)

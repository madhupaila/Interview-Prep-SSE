# Parking Meter

**Track:** Classic OOD  
**Companies:** City apps, Amazon  
**Difficulty:** Easy  

---

## Case Study

> **Full case study:** [CS-LLD-O30-parking-meter.md](../../../Case Studies/lld/classic-ood/CS-LLD-O30-parking-meter.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Parking Meter domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design parking meter: pay for duration, expire, fine extension.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Parking Meter? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design parking meter? | Include in MVP — Design parking meter |
| 5 | Requirement: pay for duration? | Include in MVP — pay for duration |
| 6 | Requirement: expire? | Include in MVP — expire |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Park and unpark with spot assignment

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via RateTable interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Meter` | Street device |
| `Vehicle` | Plate id |
| `Payment` | Coins/card |
| `ParkingSession` | Active timer |
| `RateTable` | Price per hour |

**Nouns → classes:** `Meter`, `Vehicle`, `Payment`, `ParkingSession`, `RateTable`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ParkingMeter       │──────>│ Composite        │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteComposite│
│  Meter              │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Vehicle            │────>│  Payment         │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ParkingMeter {
        +void create(Meter entity)
        +Optional<Meter> getById(String id)
        +List<Meter> listAll()
        +void delete(String id)
    }
    class Meter {
        +execute() void
    }
    class Vehicle {
        -type: VehicleType
        -licensePlate: String
    }
    class Payment {
        +execute() void
    }
    class ParkingSession {
        +execute() void
    }
    class RateTable {
        +execute() void
    }
    ParkingMeter --> Meter
```

---

## 6. Public API / Key Methods

```java
public class ParkingMeter {
    public void create(Meter entity);
    public Optional<Meter> getById(String id);
    public List<Meter> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Composite | Tree structures |

**SOLID:**
- **S:** ParkingMeter orchestrates; entities hold state
- **O:** New behavior via new RateTable impl
- **D:** Depend on RateTable interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ParkingMeter
participant D as Meter
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ParkingMeter
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Composite` implementation plugs in at runtime — no change to `ParkingMeter`."
>
> "Add new `Meter` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Composite | Composite — 2+ behaviors |
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

> "I'll design Parking Meter — clarify in-memory scope and MVP flows first."
>
> "Entities: `Meter`, `Vehicle`, `Payment`, `ParkingSession`, `RateTable`. Domain structure separate from `ParkingMeter` orchestration."
>
> "Problem: Design parking meter: pay for duration, expire, fine extension."
>
> "`Meter` — street device; owns its own invariants."
>
> "`Vehicle` — plate id; owns its own invariants."
>
> "`Payment` — coins/card; owns its own invariants."
>
> "`ParkingMeter` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Composite` in isolation?
2. How would you extend Parking Meter without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/parking-meter/) (skeleton)

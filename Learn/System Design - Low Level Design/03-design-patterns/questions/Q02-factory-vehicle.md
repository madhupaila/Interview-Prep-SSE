# Factory — Vehicle Creator

**Track:** Design Patterns  
**Companies:** Tesla, Ford, Toyota  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P02-factory-vehicle.md](../../../Case Studies/lld/design-patterns/CS-LLD-P02-factory-vehicle.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Factory — Vehicle Creator domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design factory creating Car, Truck, Motorcycle from VehicleType enum.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Factory — Vehicle Creator? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design factory creating Car? | Include in MVP — Design factory creating Car |
| 5 | Requirement: Motorcycle from VehicleType enum.? | Include in MVP — Motorcycle from VehicleType enum. |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- VehicleFactory handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via VehicleFactory interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Vehicle` | Abstract product |
| `Car` | 4-wheel |
| `Truck` | Heavy |
| `Motorcycle` | 2-wheel |
| `VehicleFactory` | Creator |

**Nouns → classes:** `Vehicle`, `Car`, `Truck`, `Motorcycle`, `VehicleFactory`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  VehicleFactory     │──────>│ Factory          │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteFactory  │
│  Vehicle            │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Car                │────>│  Truck           │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class VehicleFactory {
        +void create(Vehicle entity)
        +Optional<Vehicle> getById(String id)
        +List<Vehicle> listAll()
        +void delete(String id)
    }
    class Vehicle {
        -type: VehicleType
        -licensePlate: String
    }
    class Car {
        +execute() void
    }
    class Truck {
        +execute() void
    }
    class Motorcycle {
        +execute() void
    }
    VehicleFactory --> Vehicle
```

---

## 6. Public API / Key Methods

```java
public class VehicleFactory {
    public void create(Vehicle entity);
    public Optional<Vehicle> getById(String id);
    public List<Vehicle> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Factory | Demonstrate Factory pattern in factory-vehicle |

**SOLID:**
- **S:** VehicleFactory orchestrates; entities hold state
- **O:** New behavior via new VehicleFactory impl
- **D:** Depend on VehicleFactory interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as VehicleFactory
participant D as Vehicle
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as VehicleFactory
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Factory` implementation plugs in at runtime — no change to `VehicleFactory`."
>
> "Add new `Vehicle` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Factory | Factory — 2+ behaviors |
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

> "I'll design Factory — Vehicle Creator — clarify in-memory scope and MVP flows first."
>
> "Entities: `Vehicle`, `Car`, `Truck`, `Motorcycle`, `VehicleFactory`. Domain structure separate from `VehicleFactory` orchestration."
>
> "Problem: Design factory creating Car, Truck, Motorcycle from VehicleType enum."
>
> "`Vehicle` — abstract product; owns its own invariants."
>
> "`Car` — 4-wheel; owns its own invariants."
>
> "`Truck` — heavy; owns its own invariants."
>
> "`VehicleFactory` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Factory` in isolation?
2. How would you extend Factory — Vehicle Creator without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/factory-vehicle/README.md) (full)

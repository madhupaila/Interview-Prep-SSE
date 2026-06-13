# Parking Garage Multi-Entry

**Track:** Classic OOD  
**Companies:** Amazon, Simon  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-LLD-O38-parking-garage.md](../../../Case Studies/lld/classic-ood/CS-LLD-O38-parking-garage.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Parking Garage Multi-Entry domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design multi-entry garage with per-entrance displays and central occupancy.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Parking Garage Multi-Entry? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design multi-entry garage with per-entra? | Include in MVP — Design multi-entry garage with per-entrance displa |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Execute game turns with rule validation

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ParkingStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Garage` | Multi-floor structure |
| `EntryGate` | Ingress point |
| `ExitGate` | Egress + payment |
| `OccupancyBoard` | Live counts |
| `CentralRegistry` | Cross-gate sync |

**Nouns → classes:** `Garage`, `EntryGate`, `ExitGate`, `OccupancyBoard`, `CentralRegistry`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  GarageService      │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Garage             │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  EntryGate          │────>│  ExitGate        │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class GarageService {
        +void create(Garage entity)
        +Optional<Garage> getById(String id)
        +List<Garage> listAll()
        +void delete(String id)
    }
    class Garage {
        +execute() void
    }
    class EntryGate {
        +execute() void
    }
    class ExitGate {
        +execute() void
    }
    class OccupancyBoard {
        +execute() void
    }
    class CentralRegistry {
        +execute() void
    }
    GarageService --> Garage
```

---

## 6. Public API / Key Methods

```java
public class GarageService {
    public void create(Garage entity);
    public Optional<Garage> getById(String id);
    public List<Garage> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in Parking Garage Multi-Entry |

**SOLID:**
- **S:** GarageService orchestrates; entities hold state
- **O:** New behavior via new ParkingStrategy impl
- **D:** Depend on ParkingStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as GarageService
participant D as Garage
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as GarageService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `GarageService`."
>
> "Add new `Garage` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Parking Garage Multi-Entry — clarify in-memory scope and MVP flows first."
>
> "Entities: `Garage`, `EntryGate`, `ExitGate`, `OccupancyBoard`, `CentralRegistry`. Domain structure separate from `GarageService` orchestration."
>
> "Problem: Design multi-entry garage with per-entrance displays and central occupancy."
>
> "`Garage` — multi-floor structure; owns its own invariants."
>
> "`EntryGate` — ingress point; owns its own invariants."
>
> "`ExitGate` — egress + payment; owns its own invariants."
>
> "`GarageService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Parking Garage Multi-Entry without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/parking-garage/) (skeleton)
- [HLD counterpart](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q30-parking-lot-elevator.md)

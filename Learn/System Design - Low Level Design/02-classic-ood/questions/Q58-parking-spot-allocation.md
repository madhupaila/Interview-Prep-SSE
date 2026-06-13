# Parking Spot Allocation

**Track:** Classic OOD  
**Companies:** Amazon, Google  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O58-parking-spot-allocation.md](../../../Case Studies/lld/classic-ood/CS-LLD-O58-parking-spot-allocation.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Parking Spot Allocation domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design optimal spot allocation service decoupled from payment and gates.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Parking Spot Allocation? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design optimal spot allocation service d? | Include in MVP — Design optimal spot allocation service decoupled f |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- AllocationService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via AllocationStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `SpotRegistry` | All spots |
| `AllocationRequest` | Vehicle type + prefs |
| `AllocationStrategy` | Algorithm |
| `SpotAssignment` | Result |
| `VehicleType` | Size enum |

**Nouns → classes:** `SpotRegistry`, `AllocationRequest`, `AllocationStrategy`, `SpotAssignment`, `VehicleType`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  AllocationService  │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  SpotRegistry       │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  AllocationRequest  │────>│  AllocationStrategy│
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class AllocationService {
        +void create(SpotRegistry entity)
        +Optional<SpotRegistry> getById(String id)
        +List<SpotRegistry> listAll()
        +void delete(String id)
    }
    class SpotRegistry {
        +execute() void
    }
    class AllocationRequest {
        +execute() void
    }
    class AllocationStrategy {
        <<interface>>
        +apply() void
    }
    class SpotAssignment {
        +execute() void
    }
    class VehicleType {
        <<enumeration>>
    }
    AllocationService --> SpotRegistry
```

---

## 6. Public API / Key Methods

```java
public class AllocationService {
    public void create(SpotRegistry entity);
    public Optional<SpotRegistry> getById(String id);
    public List<SpotRegistry> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable algorithms |

**SOLID:**
- **S:** AllocationService orchestrates; entities hold state
- **O:** New behavior via new AllocationStrategy impl
- **D:** Depend on AllocationStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as AllocationService
participant D as SpotRegistry
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as AllocationService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `AllocationService`."
>
> "Add new `SpotRegistry` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Parking Spot Allocation — clarify in-memory scope and MVP flows first."
>
> "Entities: `SpotRegistry`, `AllocationRequest`, `AllocationStrategy`, `SpotAssignment`, `VehicleType`. Domain structure separate from `AllocationService` orchestration."
>
> "Problem: Design optimal spot allocation service decoupled from payment and gates."
>
> "`SpotRegistry` — all spots; owns its own invariants."
>
> "`AllocationRequest` — vehicle type + prefs; owns its own invariants."
>
> "`AllocationStrategy` — algorithm; owns its own invariants."
>
> "`AllocationService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Parking Spot Allocation without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/parking-spot-allocation/) (skeleton)
- [HLD counterpart](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q30-parking-lot-elevator.md)

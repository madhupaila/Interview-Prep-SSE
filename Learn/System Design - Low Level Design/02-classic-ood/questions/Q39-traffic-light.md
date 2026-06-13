# Traffic Light System

**Track:** Classic OOD  
**Companies:** City systems, Siemens  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O39-traffic-light.md](../../../Case Studies/lld/classic-ood/CS-LLD-O39-traffic-light.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Traffic Light System domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design intersection traffic lights with timed phases and pedestrian crossing.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Traffic Light System? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design intersection traffic lights with ? | Include in MVP — Design intersection traffic lights with timed phas |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- TrafficController handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via PhaseSequence interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Intersection` | Road junction |
| `TrafficLight` | Red/yellow/green |
| `Phase` | Signal sequence |
| `Timer` | Phase duration |
| `PedestrianButton` | Walk request |

**Nouns → classes:** `Intersection`, `TrafficLight`, `Phase`, `Timer`, `PedestrianButton`  
**Verbs → methods:** `tick()`, `requestPedestrianCrossing()`, `getCurrentPhase()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  TrafficController  │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Intersection       │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  TrafficLight       │────>│  Phase           │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class TrafficController {
        +void tick()
        +void requestPedestrianCrossing()
        +Phase getCurrentPhase()
    }
    class Intersection {
        +execute() void
    }
    class TrafficLight {
        +execute() void
    }
    class Phase {
        +execute() void
    }
    class Timer {
        +execute() void
    }
    class PedestrianButton {
        +execute() void
    }
    TrafficController --> Intersection
```

---

## 6. Public API / Key Methods

```java
public class TrafficController {
    public void tick();
    public void requestPedestrianCrossing();
    public Phase getCurrentPhase();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in Traffic Light System |

**SOLID:**
- **S:** TrafficController orchestrates; entities hold state
- **O:** New behavior via new PhaseSequence impl
- **D:** Depend on PhaseSequence interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as TrafficController
participant D as Intersection
U->>S: tick()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as TrafficController
U->>S: tick(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `TrafficController`."
>
> "Add new `Intersection` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Traffic Light System — clarify in-memory scope and MVP flows first."
>
> "Entities: `Intersection`, `TrafficLight`, `Phase`, `Timer`, `PedestrianButton`. Domain structure separate from `TrafficController` orchestration."
>
> "Problem: Design intersection traffic lights with timed phases and pedestrian crossing."
>
> "`Intersection` — road junction; owns its own invariants."
>
> "`TrafficLight` — red/yellow/green; owns its own invariants."
>
> "`Phase` — signal sequence; owns its own invariants."
>
> "`TrafficController` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Traffic Light System without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/traffic-light/) (skeleton)

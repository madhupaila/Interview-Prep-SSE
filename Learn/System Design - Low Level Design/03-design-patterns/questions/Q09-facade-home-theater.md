# Facade — Home Theater

**Track:** Design Patterns  
**Companies:** Sony, Samsung  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P09-facade-home-theater.md](../../../Case Studies/lld/design-patterns/CS-LLD-P09-facade-home-theater.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Facade — Home Theater domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design facade orchestrating amp, projector, screen, lights for watchMovie().

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Facade — Home Theater? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design facade orchestrating amp? | Include in MVP — Design facade orchestrating amp |
| 5 | Requirement: projector? | Include in MVP — projector |
| 6 | Requirement: screen? | Include in MVP — screen |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- HomeTheaterFacade handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via HomeTheaterFacade interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `HomeTheaterFacade` | Simplified API |
| `Amplifier` | Device |
| `Projector` | Device |
| `Screen` | Device |
| `Lights` | Device |

**Nouns → classes:** `HomeTheaterFacade`, `Amplifier`, `Projector`, `Screen`, `Lights`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  HomeTheaterFacade  │──────>│ Facade           │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteFacade   │
│  HomeTheaterFacade  │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Amplifier          │────>│  Projector       │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class HomeTheaterFacade {
        +void create(HomeTheaterFacade entity)
        +Optional<HomeTheaterFacade> getById(String id)
        +List<HomeTheaterFacade> listAll()
        +void delete(String id)
    }
    class Amplifier {
        +execute() void
    }
    class Projector {
        +execute() void
    }
    class Screen {
        +execute() void
    }
    class Lights {
        +execute() void
    }
```

---

## 6. Public API / Key Methods

```java
public class HomeTheaterFacade {
    public void create(HomeTheaterFacade entity);
    public Optional<HomeTheaterFacade> getById(String id);
    public List<HomeTheaterFacade> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Facade | Demonstrate Facade pattern in facade-home-theater |

**SOLID:**
- **S:** HomeTheaterFacade orchestrates; entities hold state
- **O:** New behavior via new HomeTheaterFacade impl
- **D:** Depend on HomeTheaterFacade interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as HomeTheaterFacade
participant D as HomeTheaterFacade
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as HomeTheaterFacade
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Facade` implementation plugs in at runtime — no change to `HomeTheaterFacade`."
>
> "Add new `HomeTheaterFacade` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Facade | Facade — 2+ behaviors |
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

> "I'll design Facade — Home Theater — clarify in-memory scope and MVP flows first."
>
> "Entities: `HomeTheaterFacade`, `Amplifier`, `Projector`, `Screen`, `Lights`. Domain structure separate from `HomeTheaterFacade` orchestration."
>
> "Problem: Design facade orchestrating amp, projector, screen, lights for watchMovie()."
>
> "`HomeTheaterFacade` — simplified api; owns its own invariants."
>
> "`Amplifier` — device; owns its own invariants."
>
> "`Projector` — device; owns its own invariants."
>
> "`HomeTheaterFacade` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Facade` in isolation?
2. How would you extend Facade — Home Theater without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/facade-home-theater/README.md) (full)

# Baggage Carousel

**Track:** Classic OOD  
**Companies:** Airports  
**Difficulty:** Easy  

---

## Case Study

> **Full case study:** [CS-LLD-O56-baggage-carousel.md](../../../Case Studies/lld/classic-ood/CS-LLD-O56-baggage-carousel.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Baggage Carousel domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design baggage carousel: load bags, notify passenger, claim verification.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Baggage Carousel? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design baggage carousel? | Include in MVP — Design baggage carousel |
| 5 | Requirement: load bags? | Include in MVP — load bags |
| 6 | Requirement: notify passenger? | Include in MVP — notify passenger |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Deliver notifications via configured channels

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ClaimValidator interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Carousel` | Belt system |
| `Bag` | Tagged luggage |
| `Flight` | Arrival |
| `Passenger` | Owner |
| `BagTag` | Barcode id |

**Nouns → classes:** `Carousel`, `Bag`, `Flight`, `Passenger`, `BagTag`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  BaggageService     │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Carousel           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Bag                │────>│  Flight          │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class BaggageService {
        +void create(Carousel entity)
        +Optional<Carousel> getById(String id)
        +List<Carousel> listAll()
        +void delete(String id)
    }
    class Carousel {
        +execute() void
    }
    class Bag {
        +execute() void
    }
    class Flight {
        +execute() void
    }
    class Passenger {
        +execute() void
    }
    class BagTag {
        +execute() void
    }
    BaggageService --> Carousel
```

---

## 6. Public API / Key Methods

```java
public class BaggageService {
    public void create(Carousel entity);
    public Optional<Carousel> getById(String id);
    public List<Carousel> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in Baggage Carousel |

**SOLID:**
- **S:** BaggageService orchestrates; entities hold state
- **O:** New behavior via new ClaimValidator impl
- **D:** Depend on ClaimValidator interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as BaggageService
participant D as Carousel
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as BaggageService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `BaggageService`."
>
> "Add new `Carousel` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Baggage Carousel — clarify in-memory scope and MVP flows first."
>
> "Entities: `Carousel`, `Bag`, `Flight`, `Passenger`, `BagTag`. Domain structure separate from `BaggageService` orchestration."
>
> "Problem: Design baggage carousel: load bags, notify passenger, claim verification."
>
> "`Carousel` — belt system; owns its own invariants."
>
> "`Bag` — tagged luggage; owns its own invariants."
>
> "`Flight` — arrival; owns its own invariants."
>
> "`BaggageService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Baggage Carousel without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/baggage-carousel/README.md) (skeleton)

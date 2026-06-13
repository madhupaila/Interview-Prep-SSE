# Strategy — Shipping Calculator

**Track:** Design Patterns  
**Companies:** Amazon, FedEx  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P23-strategy-shipping.md](../../../Case Studies/lld/design-patterns/CS-LLD-P23-strategy-shipping.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Strategy — Shipping Calculator domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design shipping cost strategies: standard, express, overnight by weight/zone.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Strategy — Shipping Calculator? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design shipping cost strategies? | Include in MVP — Design shipping cost strategies |
| 5 | Requirement: standard? | Include in MVP — standard |
| 6 | Requirement: express? | Include in MVP — express |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- ShippingCalculator handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ShippingStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `ShippingStrategy` | Interface |
| `StandardShipping` | Impl |
| `ExpressShipping` | Impl |
| `Package` | Weight + zone |

**Nouns → classes:** `ShippingStrategy`, `StandardShipping`, `ExpressShipping`, `Package`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ShippingCalculator │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  ShippingStrategy   │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  StandardShipping   │────>│  ExpressShipping │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ShippingCalculator {
        +void create(ShippingStrategy entity)
        +Optional<ShippingStrategy> getById(String id)
        +List<ShippingStrategy> listAll()
        +void delete(String id)
    }
    class ShippingStrategy {
        <<interface>>
        +apply() void
    }
    class StandardShipping {
        +execute() void
    }
    class ExpressShipping {
        +execute() void
    }
    class Package {
        +execute() void
    }
    ShippingCalculator --> ShippingStrategy
```

---

## 6. Public API / Key Methods

```java
public class ShippingCalculator {
    public void create(ShippingStrategy entity);
    public Optional<ShippingStrategy> getById(String id);
    public List<ShippingStrategy> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Demonstrate Strategy pattern in strategy-shipping |

**SOLID:**
- **S:** ShippingCalculator orchestrates; entities hold state
- **O:** New behavior via new ShippingStrategy impl
- **D:** Depend on ShippingStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ShippingCalculator
participant D as ShippingStrategy
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ShippingCalculator
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `ShippingCalculator`."
>
> "Add new `ShippingStrategy` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Strategy — Shipping Calculator — clarify in-memory scope and MVP flows first."
>
> "Entities: `ShippingStrategy`, `StandardShipping`, `ExpressShipping`, `Package`. Domain structure separate from `ShippingCalculator` orchestration."
>
> "Problem: Design shipping cost strategies: standard, express, overnight by weight/zone."
>
> "`ShippingStrategy` — interface; owns its own invariants."
>
> "`StandardShipping` — impl; owns its own invariants."
>
> "`ExpressShipping` — impl; owns its own invariants."
>
> "`ShippingCalculator` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Strategy — Shipping Calculator without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/strategy-shipping/) (full)

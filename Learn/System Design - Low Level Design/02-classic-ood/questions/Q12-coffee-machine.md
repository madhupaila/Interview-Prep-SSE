# Coffee Machine

**Track:** Classic OOD  
**Companies:** Starbucks, Nestlé  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O12-coffee-machine.md](../../../Case Studies/lld/classic-ood/CS-LLD-O12-coffee-machine.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Coffee Machine domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design coffee machine with recipes, ingredients inventory, and brew states.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Coffee Machine? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design coffee machine with recipes? | Include in MVP — Design coffee machine with recipes |
| 5 | Requirement: ingredients inventory? | Include in MVP — ingredients inventory |
| 6 | Requirement: and brew states.? | Include in MVP — and brew states. |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- CoffeeMaker handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via Recipe interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Machine` | Hardware facade |
| `Recipe` | Espresso/latte steps |
| `Ingredient` | Beans/milk/water |
| `Beverage` | Output |
| `BrewState` | Idle/heating/brewing |

**Nouns → classes:** `Machine`, `Recipe`, `Ingredient`, `Beverage`, `BrewState`  
**Verbs → methods:** `reserve()`, `release()`, `getAvailable()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  CoffeeMaker        │──────>│ State            │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteState    │
│  Machine            │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Recipe             │────>│  Ingredient      │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class CoffeeMaker {
        +void reserve(String sku, int qty)
        +void release(String sku, int qty)
        +int getAvailable(String sku)
    }
    class Machine {
        +execute() void
    }
    class Recipe {
        +execute() void
    }
    class Ingredient {
        +execute() void
    }
    class Beverage {
        +execute() void
    }
    class BrewState {
        +execute() void
    }
    CoffeeMaker --> Machine
```

---

## 6. Public API / Key Methods

```java
public class CoffeeMaker {
    public void reserve(String sku, int qty);
    public void release(String sku, int qty);
    public int getAvailable(String sku);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| State | Lifecycle state transitions |

**SOLID:**
- **S:** CoffeeMaker orchestrates; entities hold state
- **O:** New behavior via new Recipe impl
- **D:** Depend on Recipe interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CoffeeMaker
participant D as Machine
U->>S: reserve()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CoffeeMaker
U->>S: reserve(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `State` implementation plugs in at runtime — no change to `CoffeeMaker`."
>
> "Add new `Machine` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | State | State — 2+ behaviors |
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

> "I'll design Coffee Machine — clarify in-memory scope and MVP flows first."
>
> "Entities: `Machine`, `Recipe`, `Ingredient`, `Beverage`, `BrewState`. Domain structure separate from `CoffeeMaker` orchestration."
>
> "Problem: Design coffee machine with recipes, ingredients inventory, and brew states."
>
> "`Machine` — hardware facade; owns its own invariants."
>
> "`Recipe` — espresso/latte steps; owns its own invariants."
>
> "`Ingredient` — beans/milk/water; owns its own invariants."
>
> "`CoffeeMaker` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `State` in isolation?
2. How would you extend Coffee Machine without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/coffee-machine/Demo.java) (skeleton)

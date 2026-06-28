# Builder — Meal Combo

**Track:** Design Patterns  
**Companies:** McDonald's, Starbucks  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P04-builder-meal.md](../../../Case Studies/lld/design-patterns/CS-LLD-P04-builder-meal.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Builder — Meal Combo domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design builder for meal combos: burger, drink, fries step-by-step.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Builder — Meal Combo? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design builder for meal combos? | Include in MVP — Design builder for meal combos |
| 5 | Requirement: burger? | Include in MVP — burger |
| 6 | Requirement: fries step-by-step.? | Include in MVP — fries step-by-step. |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- MealBuilder handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via MealBuilder interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Meal` | Product |
| `MealBuilder` | Fluent builder |
| `Burger` | Item |
| `Drink` | Item |
| `MealDirector` | Preset combos |

**Nouns → classes:** `Meal`, `MealBuilder`, `Burger`, `Drink`, `MealDirector`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  MealBuilder        │──────>│ Builder          │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteBuilder  │
│  Meal               │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  MealBuilder        │────>│  Burger          │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class MealBuilder {
        +void create(Meal entity)
        +Optional<Meal> getById(String id)
        +List<Meal> listAll()
        +void delete(String id)
    }
    class Meal {
        +execute() void
    }
    class Burger {
        +execute() void
    }
    class Drink {
        +execute() void
    }
    class MealDirector {
        +execute() void
    }
    MealBuilder --> Meal
```

---

## 6. Public API / Key Methods

```java
public class MealBuilder {
    public void create(Meal entity);
    public Optional<Meal> getById(String id);
    public List<Meal> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Builder | Demonstrate Builder pattern in builder-meal |

**SOLID:**
- **S:** MealBuilder orchestrates; entities hold state
- **O:** New behavior via new MealBuilder impl
- **D:** Depend on MealBuilder interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as MealBuilder
participant D as Meal
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as MealBuilder
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Builder` implementation plugs in at runtime — no change to `MealBuilder`."
>
> "Add new `Meal` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Builder | Builder — 2+ behaviors |
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

> "I'll design Builder — Meal Combo — clarify in-memory scope and MVP flows first."
>
> "Entities: `Meal`, `MealBuilder`, `Burger`, `Drink`, `MealDirector`. Domain structure separate from `MealBuilder` orchestration."
>
> "Problem: Design builder for meal combos: burger, drink, fries step-by-step."
>
> "`Meal` — product; owns its own invariants."
>
> "`MealBuilder` — fluent builder; owns its own invariants."
>
> "`Burger` — item; owns its own invariants."
>
> "`MealBuilder` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Builder` in isolation?
2. How would you extend Builder — Meal Combo without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/builder-meal/README.md) (full)

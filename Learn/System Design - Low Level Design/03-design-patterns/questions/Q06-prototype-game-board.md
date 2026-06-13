# Prototype — Game Board Clone

**Track:** Design Patterns  
**Companies:** EA, Unity  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P06-prototype-game-board.md](../../../Case Studies/lld/design-patterns/CS-LLD-P06-prototype-game-board.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Prototype — Game Board Clone domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design prototype pattern to clone complex game boards for save/replay.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Prototype — Game Board Clone? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design prototype pattern to clone comple? | Include in MVP — Design prototype pattern to clone complex game boa |
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
- Open-Closed via GameBoard interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `GameBoard` | Prototype |
| `Cell` | Board cell |
| `BoardRegistry` | Template cache |
| `Cloneable` | Copy interface |

**Nouns → classes:** `GameBoard`, `Cell`, `BoardRegistry`, `Cloneable`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  BoardPrototype     │──────>│ Prototype        │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcretePrototype│
│  GameBoard          │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Cell               │────>│  BoardRegistry   │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class BoardPrototype {
        +void create(GameBoard entity)
        +Optional<GameBoard> getById(String id)
        +List<GameBoard> listAll()
        +void delete(String id)
    }
    class GameBoard {
        +execute() void
    }
    class Cell {
        +execute() void
    }
    class BoardRegistry {
        +execute() void
    }
    class Cloneable {
        <<interface>>
        +apply() void
    }
    BoardPrototype --> GameBoard
```

---

## 6. Public API / Key Methods

```java
public class BoardPrototype {
    public void create(GameBoard entity);
    public Optional<GameBoard> getById(String id);
    public List<GameBoard> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Prototype | Demonstrate Prototype pattern in prototype-game-board |

**SOLID:**
- **S:** BoardPrototype orchestrates; entities hold state
- **O:** New behavior via new GameBoard impl
- **D:** Depend on GameBoard interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as BoardPrototype
participant D as GameBoard
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as BoardPrototype
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Prototype` implementation plugs in at runtime — no change to `BoardPrototype`."
>
> "Add new `GameBoard` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Prototype | Prototype — 2+ behaviors |
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

> "I'll design Prototype — Game Board Clone — clarify in-memory scope and MVP flows first."
>
> "Entities: `GameBoard`, `Cell`, `BoardRegistry`, `Cloneable`. Domain structure separate from `BoardPrototype` orchestration."
>
> "Problem: Design prototype pattern to clone complex game boards for save/replay."
>
> "`GameBoard` — prototype; owns its own invariants."
>
> "`Cell` — board cell; owns its own invariants."
>
> "`BoardRegistry` — template cache; owns its own invariants."
>
> "`BoardPrototype` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Prototype` in isolation?
2. How would you extend Prototype — Game Board Clone without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/prototype-game-board/) (full)

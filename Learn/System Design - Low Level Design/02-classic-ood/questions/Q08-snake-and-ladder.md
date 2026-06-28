# Snake and Ladder

**Track:** Classic OOD  
**Companies:** Amazon, Flipkart  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O08-snake-and-ladder.md](../../../Case Studies/lld/classic-ood/CS-LLD-O08-snake-and-ladder.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Snake and Ladder domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design snake-and-ladder board game with dice rolls, snakes, ladders, and win condition.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Snake and Ladder? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design snake-and-ladder board game with ? | Include in MVP — Design snake-and-ladder board game with dice rolls |
| 5 | Requirement: snakes? | Include in MVP — snakes |
| 6 | Requirement: ladders? | Include in MVP — ladders |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- GameEngine handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via Dice interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Board` | Cells with jumps |
| `Player` | Position |
| `Dice` | Random 1-6 |
| `Snake` | Down jump |
| `Ladder` | Up jump |

**Nouns → classes:** `Board`, `Player`, `Dice`, `Snake`, `Ladder`  
**Verbs → methods:** `playTurn()`, `isGameOver()`, `getCurrentPlayer()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  GameEngine         │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Board              │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Player             │────>│  Dice            │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class GameEngine {
        +void playTurn(GameAction action)
        +boolean isGameOver()
        +Player getCurrentPlayer()
    }
    class Board {
        -cells: Cell[][]
        +getPiece(int,int) Piece
        +movePiece(Move) void
    }
    class Player {
        +execute() void
    }
    class Dice {
        +execute() void
    }
    class Snake {
        +execute() void
    }
    class Ladder {
        +execute() void
    }
    GameEngine --> Board
```

---

## 6. Public API / Key Methods

```java
public class GameEngine {
    public void playTurn(GameAction action);
    public boolean isGameOver();
    public Player getCurrentPlayer();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in Snake and Ladder |

**SOLID:**
- **S:** GameEngine orchestrates; entities hold state
- **O:** New behavior via new Dice impl
- **D:** Depend on Dice interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as GameEngine
participant D as Board
U->>S: playTurn()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as GameEngine
U->>S: playTurn(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `GameEngine`."
>
> "Add new `Board` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Snake and Ladder — clarify in-memory scope and MVP flows first."
>
> "Entities: `Board`, `Player`, `Dice`, `Snake`, `Ladder`. Domain structure separate from `GameEngine` orchestration."
>
> "Problem: Design snake-and-ladder board game with dice rolls, snakes, ladders, and win condition."
>
> "`Board` — cells with jumps; owns its own invariants."
>
> "`Player` — position; owns its own invariants."
>
> "`Dice` — random 1-6; owns its own invariants."
>
> "`GameEngine` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Snake and Ladder without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/snake-and-ladder/Demo.java) (full)

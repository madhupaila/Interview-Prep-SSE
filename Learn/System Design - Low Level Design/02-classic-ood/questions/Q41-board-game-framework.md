# Board Game Framework

**Track:** Classic OOD  
**Companies:** EA, Hasbro  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O41-board-game-framework.md](../../../Case Studies/lld/classic-ood/CS-LLD-O41-board-game-framework.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Board Game Framework domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design extensible board game framework: board, players, turns, rules engine.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Board Game Framework? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design extensible board game framework? | Include in MVP — Design extensible board game framework |
| 5 | Requirement: players? | Include in MVP — players |
| 6 | Requirement: rules engine.? | Include in MVP — rules engine. |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Execute game turns with rule validation

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via RuleEngine interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Game` | Match coordinator |
| `Board` | Grid/graph |
| `Player` | Participant |
| `RuleEngine` | Move validation |
| `TurnManager` | Next player |
| `GameAction` | Command |

**Nouns → classes:** `Game`, `Board`, `Player`, `RuleEngine`, `TurnManager`, `GameAction`  
**Verbs → methods:** `playTurn()`, `isGameOver()`, `getCurrentPlayer()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  GameFramework      │──────>│ Command          │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteCommand  │
│  Game               │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Board              │────>│  Player          │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class GameFramework {
        +void playTurn(GameAction action)
        +boolean isGameOver()
        +Player getCurrentPlayer()
    }
    class Game {
        +execute() void
    }
    class Board {
        -cells: Cell[][]
        +getPiece(int,int) Piece
        +movePiece(Move) void
    }
    class Player {
        +execute() void
    }
    class RuleEngine {
        +execute() void
    }
    class TurnManager {
        +execute() void
    }
    class GameAction {
        +execute() void
    }
    GameFramework --> Game
```

---

## 6. Public API / Key Methods

```java
public class GameFramework {
    public void playTurn(GameAction action);
    public boolean isGameOver();
    public Player getCurrentPlayer();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Command | Encapsulated operations |

**SOLID:**
- **S:** GameFramework orchestrates; entities hold state
- **O:** New behavior via new RuleEngine impl
- **D:** Depend on RuleEngine interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as GameFramework
participant D as Game
U->>S: playTurn()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as GameFramework
U->>S: playTurn(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Command` implementation plugs in at runtime — no change to `GameFramework`."
>
> "Add new `Game` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Command | Command — 2+ behaviors |
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

> "I'll design Board Game Framework — clarify in-memory scope and MVP flows first."
>
> "Entities: `Game`, `Board`, `Player`, `RuleEngine`, `TurnManager`, `GameAction`. Domain structure separate from `GameFramework` orchestration."
>
> "Problem: Design extensible board game framework: board, players, turns, rules engine."
>
> "`Game` — match coordinator; owns its own invariants."
>
> "`Board` — grid/graph; owns its own invariants."
>
> "`Player` — participant; owns its own invariants."
>
> "`GameFramework` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Command` in isolation?
2. How would you extend Board Game Framework without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/board-game-framework/README.md) (full)

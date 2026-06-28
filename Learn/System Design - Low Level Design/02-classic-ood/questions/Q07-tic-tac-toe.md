# Tic-Tac-Toe

**Track:** Classic OOD  
**Companies:** Amazon, Google  
**Difficulty:** Easy  

---

## Case Study

> **Full case study:** [CS-LLD-O07-tic-tac-toe.md](../../../Case Studies/lld/classic-ood/CS-LLD-O07-tic-tac-toe.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Tic-Tac-Toe domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design tic-tac-toe for two players with win/draw detection on NxN board.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Tic-Tac-Toe? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design tic-tac-toe for two players with ? | Include in MVP — Design tic-tac-toe for two players with win/draw d |
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
- Open-Closed via WinChecker interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Board` | NxN grid |
| `Player` | X or O |
| `Game` | Match state |
| `WinChecker` | Row/col/diag scan |

**Nouns → classes:** `Board`, `Player`, `Game`, `WinChecker`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  GameService        │──────>│ Strategy         │<<interface>>
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
│  Player             │────>│  Game            │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class GameService {
        +void create(Board entity)
        +Optional<Board> getById(String id)
        +List<Board> listAll()
        +void delete(String id)
    }
    class Board {
        -cells: Cell[][]
        +getPiece(int,int) Piece
        +movePiece(Move) void
    }
    class Player {
        +execute() void
    }
    class Game {
        +execute() void
    }
    class WinChecker {
        +execute() void
    }
    GameService --> Board
```

---

## 6. Public API / Key Methods

```java
public class GameService {
    public void create(Board entity);
    public Optional<Board> getById(String id);
    public List<Board> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Win detection algorithm |

**SOLID:**
- **S:** GameService orchestrates; entities hold state
- **O:** New behavior via new WinChecker impl
- **D:** Depend on WinChecker interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as GameService
participant D as Board
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as GameService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `GameService`."
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

> "I'll design Tic-Tac-Toe — clarify in-memory scope and MVP flows first."
>
> "Entities: `Board`, `Player`, `Game`, `WinChecker`. Domain structure separate from `GameService` orchestration."
>
> "Problem: Design tic-tac-toe for two players with win/draw detection on NxN board."
>
> "`Board` — nxn grid; owns its own invariants."
>
> "`Player` — x or o; owns its own invariants."
>
> "`Game` — match state; owns its own invariants."
>
> "`GameService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Tic-Tac-Toe without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/tic-tac-toe/Demo.java) (full)

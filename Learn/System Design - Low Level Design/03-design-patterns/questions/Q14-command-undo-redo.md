# Command — Undo/Redo

**Track:** Design Patterns  
**Companies:** Adobe, Microsoft  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P14-command-undo-redo.md](../../../Case Studies/lld/design-patterns/CS-LLD-P14-command-undo-redo.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Photoshop and Google Docs undo stack. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design command pattern with undo/redo stack for text editor actions.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Command — Undo/Redo? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design command pattern with undo/redo st? | Include in MVP — Design command pattern with undo/redo stack for te |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- CommandManager handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via Command interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Command` | Execute/undo |
| `InsertCommand` | Concrete |
| `CommandHistory` | Undo stack |
| `Editor` | Receiver |

**Nouns → classes:** `Command`, `InsertCommand`, `CommandHistory`, `Editor`  
**Verbs → methods:** `execute()`, `undo()`, `redo()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  CommandManager     │──────>│ Command          │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteCommand  │
│  Command            │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  InsertCommand      │────>│  CommandHistory  │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class CommandManager {
        +void execute(Command command)
        +void undo()
        +void redo()
    }
    class Command {
        <<interface>>
        +execute() void
        +undo() void
    }
    class InsertCommand {
        +execute() void
        +undo() void
    }
    class CommandHistory {
        +push(Command) void
        +pop() Command
    }
    class Editor {
        +insert(String) void
        +delete(int) void
    }
    CommandManager --> Command
```

---

## 6. Public API / Key Methods

```java
public class CommandManager {
    public void execute(Command command);
    public void undo();
    public void redo();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Command | Encapsulate actions with undo |
| Memento | Optional state snapshots |

**SOLID:**
- **S:** CommandManager orchestrates; entities hold state
- **O:** New behavior via new Command impl
- **D:** Depend on Command interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CommandManager
participant D as Command
U->>S: execute()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CommandManager
U->>S: execute(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Command` implementation plugs in at runtime — no change to `CommandManager`."
>
> "Add new `Command` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Command — Undo/Redo — clarify in-memory scope and MVP flows first."
>
> "Entities: `Command`, `InsertCommand`, `CommandHistory`, `Editor`. Domain structure separate from `CommandManager` orchestration."
>
> "Problem: Design command pattern with undo/redo stack for text editor actions."
>
> "`Command` — execute/undo; owns its own invariants."
>
> "`InsertCommand` — concrete; owns its own invariants."
>
> "`CommandHistory` — undo stack; owns its own invariants."
>
> "`CommandManager` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Command` in isolation?
2. How would you extend Command — Undo/Redo without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/command-undo-redo/) (full)

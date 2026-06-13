# Memento — Text Editor

**Track:** Design Patterns  
**Companies:** Microsoft, Adobe  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P20-memento-text-editor.md](../../../Case Studies/lld/design-patterns/CS-LLD-P20-memento-text-editor.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Memento — Text Editor domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design memento for editor snapshots enabling undo to prior document state.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Memento — Text Editor? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design memento for editor snapshots enab? | Include in MVP — Design memento for editor snapshots enabling undo  |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- EditorMemento handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via Editor interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Editor` | Originator |
| `Memento` | Snapshot |
| `HistoryCaretaker` | Stack of mementos |
| `Document` | State |

**Nouns → classes:** `Editor`, `Memento`, `HistoryCaretaker`, `Document`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  EditorMemento      │──────>│ Memento          │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteMemento  │
│  Editor             │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Memento            │────>│  HistoryCaretaker│
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class EditorMemento {
        +void create(Editor entity)
        +Optional<Editor> getById(String id)
        +List<Editor> listAll()
        +void delete(String id)
    }
    class Editor {
        +insert(String) void
        +delete(int) void
    }
    class Memento {
        +execute() void
    }
    class HistoryCaretaker {
        +execute() void
    }
    class Document {
        +execute() void
    }
    EditorMemento --> Editor
```

---

## 6. Public API / Key Methods

```java
public class EditorMemento {
    public void create(Editor entity);
    public Optional<Editor> getById(String id);
    public List<Editor> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Memento | Demonstrate Memento pattern in memento-text-editor |

**SOLID:**
- **S:** EditorMemento orchestrates; entities hold state
- **O:** New behavior via new Editor impl
- **D:** Depend on Editor interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as EditorMemento
participant D as Editor
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as EditorMemento
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Memento` implementation plugs in at runtime — no change to `EditorMemento`."
>
> "Add new `Editor` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Memento | Memento — 2+ behaviors |
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

> "I'll design Memento — Text Editor — clarify in-memory scope and MVP flows first."
>
> "Entities: `Editor`, `Memento`, `HistoryCaretaker`, `Document`. Domain structure separate from `EditorMemento` orchestration."
>
> "Problem: Design memento for editor snapshots enabling undo to prior document state."
>
> "`Editor` — originator; owns its own invariants."
>
> "`Memento` — snapshot; owns its own invariants."
>
> "`HistoryCaretaker` — stack of mementos; owns its own invariants."
>
> "`EditorMemento` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Memento` in isolation?
2. How would you extend Memento — Text Editor without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/memento-text-editor/) (full)

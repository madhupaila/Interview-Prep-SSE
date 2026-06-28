# Template Method — Data Parser

**Track:** Design Patterns  
**Companies:** Apache, Elastic  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P16-template-method-parser.md](../../../Case Studies/lld/design-patterns/CS-LLD-P16-template-method-parser.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Template Method — Data Parser domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design template method for CSV/JSON parsers sharing open-read-parse-close skeleton.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Template Method — Data Parser? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design template method for CSV/JSON pars? | Include in MVP — Design template method for CSV/JSON parsers sharin |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- DataParser handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via DataParser interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `DataParser` | Abstract template |
| `CsvParser` | Concrete |
| `JsonParser` | Concrete |
| `ParseContext` | Input source |

**Nouns → classes:** `DataParser`, `CsvParser`, `JsonParser`, `ParseContext`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  DataParser         │──────>│ Template Method  │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteTemplate Method│
│  DataParser         │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  CsvParser          │────>│  JsonParser      │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class DataParser {
        +void create(DataParser entity)
        +Optional<DataParser> getById(String id)
        +List<DataParser> listAll()
        +void delete(String id)
    }
    class CsvParser {
        +execute() void
    }
    class JsonParser {
        +execute() void
    }
    class ParseContext {
        +execute() void
    }
```

---

## 6. Public API / Key Methods

```java
public class DataParser {
    public void create(DataParser entity);
    public Optional<DataParser> getById(String id);
    public List<DataParser> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Template Method | Demonstrate Template Method pattern in template-method-parser |

**SOLID:**
- **S:** DataParser orchestrates; entities hold state
- **O:** New behavior via new DataParser impl
- **D:** Depend on DataParser interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as DataParser
participant D as DataParser
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as DataParser
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Template Method` implementation plugs in at runtime — no change to `DataParser`."
>
> "Add new `DataParser` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Template Method | Template Method — 2+ behaviors |
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

> "I'll design Template Method — Data Parser — clarify in-memory scope and MVP flows first."
>
> "Entities: `DataParser`, `CsvParser`, `JsonParser`, `ParseContext`. Domain structure separate from `DataParser` orchestration."
>
> "Problem: Design template method for CSV/JSON parsers sharing open-read-parse-close skeleton."
>
> "`DataParser` — abstract template; owns its own invariants."
>
> "`CsvParser` — concrete; owns its own invariants."
>
> "`JsonParser` — concrete; owns its own invariants."
>
> "`DataParser` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Template Method` in isolation?
2. How would you extend Template Method — Data Parser without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/template-method-parser/README.md) (full)

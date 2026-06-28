# Factory — Document Creator

**Track:** Design Patterns  
**Companies:** Microsoft, Google  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P24-factory-document.md](../../../Case Studies/lld/design-patterns/CS-LLD-P24-factory-document.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Factory — Document Creator domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design factory method creating PDF, Word, Markdown documents.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Factory — Document Creator? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design factory method creating PDF? | Include in MVP — Design factory method creating PDF |
| 5 | Requirement: Markdown documents.? | Include in MVP — Markdown documents. |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- DocumentFactory handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via DocumentFactory interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Document` | Product |
| `PdfDocument` | Concrete |
| `WordDocument` | Concrete |
| `DocumentFactory` | Creator |

**Nouns → classes:** `Document`, `PdfDocument`, `WordDocument`, `DocumentFactory`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  DocumentFactory    │──────>│ Factory          │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteFactory  │
│  Document           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  PdfDocument        │────>│  WordDocument    │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class DocumentFactory {
        +void create(Document entity)
        +Optional<Document> getById(String id)
        +List<Document> listAll()
        +void delete(String id)
    }
    class Document {
        +execute() void
    }
    class PdfDocument {
        +execute() void
    }
    class WordDocument {
        +execute() void
    }
    DocumentFactory --> Document
```

---

## 6. Public API / Key Methods

```java
public class DocumentFactory {
    public void create(Document entity);
    public Optional<Document> getById(String id);
    public List<Document> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Factory | Demonstrate Factory pattern in factory-document |

**SOLID:**
- **S:** DocumentFactory orchestrates; entities hold state
- **O:** New behavior via new DocumentFactory impl
- **D:** Depend on DocumentFactory interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as DocumentFactory
participant D as Document
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as DocumentFactory
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Factory` implementation plugs in at runtime — no change to `DocumentFactory`."
>
> "Add new `Document` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Factory | Factory — 2+ behaviors |
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

> "I'll design Factory — Document Creator — clarify in-memory scope and MVP flows first."
>
> "Entities: `Document`, `PdfDocument`, `WordDocument`, `DocumentFactory`. Domain structure separate from `DocumentFactory` orchestration."
>
> "Problem: Design factory method creating PDF, Word, Markdown documents."
>
> "`Document` — product; owns its own invariants."
>
> "`PdfDocument` — concrete; owns its own invariants."
>
> "`WordDocument` — concrete; owns its own invariants."
>
> "`DocumentFactory` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Factory` in isolation?
2. How would you extend Factory — Document Creator without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/factory-document/README.md) (full)

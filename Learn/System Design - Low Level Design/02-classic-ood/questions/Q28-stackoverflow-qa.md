# Stack Overflow Q&A

**Track:** Classic OOD  
**Companies:** Stack Overflow, Google  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O28-stackoverflow-qa.md](../../../Case Studies/lld/classic-ood/CS-LLD-O28-stackoverflow-qa.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Stack Overflow Q&A domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design Q&A platform object model: questions, answers, votes, tags, reputation.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Stack Overflow Q&A? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design Q&A platform object model? | Include in MVP — Design Q&A platform object model |
| 5 | Requirement: questions? | Include in MVP — questions |
| 6 | Requirement: answers? | Include in MVP — answers |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- QAService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via VotePolicy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Question` | Post |
| `Answer` | Response |
| `User` | Reputation holder |
| `Vote` | Up/down |
| `Tag` | Topic label |
| `ReputationService` | Score updates |

**Nouns → classes:** `Question`, `Answer`, `User`, `Vote`, `Tag`, `ReputationService`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  QAService          │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Question           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Answer             │────>│  User            │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class QAService {
        +void create(Question entity)
        +Optional<Question> getById(String id)
        +List<Question> listAll()
        +void delete(String id)
    }
    class Question {
        +execute() void
    }
    class Answer {
        +execute() void
    }
    class User {
        -id: String
        -name: String
    }
    class Vote {
        +execute() void
    }
    class Tag {
        -label: String
    }
    class ReputationService {
        +execute() void
    }
    QAService --> Question
```

---

## 6. Public API / Key Methods

```java
public class QAService {
    public void create(Question entity);
    public Optional<Question> getById(String id);
    public List<Question> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in Stack Overflow Q&A |

**SOLID:**
- **S:** QAService orchestrates; entities hold state
- **O:** New behavior via new VotePolicy impl
- **D:** Depend on VotePolicy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as QAService
participant D as Question
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as QAService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `QAService`."
>
> "Add new `Question` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Stack Overflow Q&A — clarify in-memory scope and MVP flows first."
>
> "Entities: `Question`, `Answer`, `User`, `Vote`, `Tag`, `ReputationService`. Domain structure separate from `QAService` orchestration."
>
> "Problem: Design Q&A platform object model: questions, answers, votes, tags, reputation."
>
> "`Question` — post; owns its own invariants."
>
> "`Answer` — response; owns its own invariants."
>
> "`User` — reputation holder; owns its own invariants."
>
> "`QAService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Stack Overflow Q&A without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/stackoverflow-qa/README.md) (skeleton)

# Social Graph

**Track:** Classic OOD  
**Companies:** Meta, LinkedIn  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O44-social-graph.md](../../../Case Studies/lld/classic-ood/CS-LLD-O44-social-graph.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Social Graph domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design social graph: follow/friend edges, suggestions, BFS reach.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Social Graph? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design social graph? | Include in MVP — Design social graph |
| 5 | Requirement: follow/friend edges? | Include in MVP — follow/friend edges |
| 6 | Requirement: suggestions? | Include in MVP — suggestions |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- GraphService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via SuggestionEngine interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `User` | Node |
| `Relationship` | Edge type |
| `SocialGraph` | Adjacency store |
| `Follow` | Directed edge |
| `SuggestionEngine` | Friend-of-friend |

**Nouns → classes:** `User`, `Relationship`, `SocialGraph`, `Follow`, `SuggestionEngine`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  GraphService       │──────>│ Repository       │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteRepository│
│  User               │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Relationship       │────>│  SocialGraph     │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class GraphService {
        +void create(User entity)
        +Optional<User> getById(String id)
        +List<User> listAll()
        +void delete(String id)
    }
    class User {
        -id: String
        -name: String
    }
    class Relationship {
        +execute() void
    }
    class SocialGraph {
        +execute() void
    }
    class Follow {
        +execute() void
    }
    class SuggestionEngine {
        +execute() void
    }
    GraphService --> User
```

---

## 6. Public API / Key Methods

```java
public class GraphService {
    public void create(User entity);
    public Optional<User> getById(String id);
    public List<User> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Repository | Persistence abstraction |

**SOLID:**
- **S:** GraphService orchestrates; entities hold state
- **O:** New behavior via new SuggestionEngine impl
- **D:** Depend on SuggestionEngine interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as GraphService
participant D as User
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as GraphService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Repository` implementation plugs in at runtime — no change to `GraphService`."
>
> "Add new `User` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Repository | Repository — 2+ behaviors |
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

> "I'll design Social Graph — clarify in-memory scope and MVP flows first."
>
> "Entities: `User`, `Relationship`, `SocialGraph`, `Follow`, `SuggestionEngine`. Domain structure separate from `GraphService` orchestration."
>
> "Problem: Design social graph: follow/friend edges, suggestions, BFS reach."
>
> "`User` — node; owns its own invariants."
>
> "`Relationship` — edge type; owns its own invariants."
>
> "`SocialGraph` — adjacency store; owns its own invariants."
>
> "`GraphService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Repository` in isolation?
2. How would you extend Social Graph without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/social-graph/) (skeleton)

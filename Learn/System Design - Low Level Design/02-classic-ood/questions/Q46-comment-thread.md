# Comment Thread

**Track:** Classic OOD  
**Companies:** Reddit, YouTube  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O46-comment-thread.md](../../../Case Studies/lld/classic-ood/CS-LLD-O46-comment-thread.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Comment Thread domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design nested comments: post, reply, edit, delete, sort top/new.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Comment Thread? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design nested comments? | Include in MVP — Design nested comments |
| 5 | Requirement: delete? | Include in MVP — delete |
| 6 | Requirement: sort top/new.? | Include in MVP — sort top/new. |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- CommentService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via SortStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Post` | Parent content |
| `Comment` | Tree node |
| `CommentThread` | Root collection |
| `SortStrategy` | Top/new ordering |
| `ModerationFlag` | Report |

**Nouns → classes:** `Post`, `Comment`, `CommentThread`, `SortStrategy`, `ModerationFlag`  
**Verbs → methods:** `getFeed()`, `createPost()`, `addReaction()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  CommentService     │──────>│ Composite        │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteComposite│
│  Post               │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Comment            │────>│  CommentThread   │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class CommentService {
        +Feed getFeed(User user, Cursor cursor)
        +Post createPost(User author, String content)
        +void addReaction(String postId, Reaction reaction)
    }
    class Post {
        -content: String
        +addReaction(Reaction) void
    }
    class Comment {
        -text: String
        +reply(String) Comment
    }
    class CommentThread {
        +execute() void
    }
    class SortStrategy {
        <<interface>>
        +apply() void
    }
    class ModerationFlag {
        +execute() void
    }
    CommentService --> Post
```

---

## 6. Public API / Key Methods

```java
public class CommentService {
    public Feed getFeed(User user, Cursor cursor);
    public Post createPost(User author, String content);
    public void addReaction(String postId, Reaction reaction);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Composite | Nested comments tree |

**SOLID:**
- **S:** CommentService orchestrates; entities hold state
- **O:** New behavior via new SortStrategy impl
- **D:** Depend on SortStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CommentService
participant D as Post
U->>S: getFeed()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CommentService
U->>S: getFeed(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Composite` implementation plugs in at runtime — no change to `CommentService`."
>
> "Add new `Post` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Composite | Composite — 2+ behaviors |
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

> "I'll design Comment Thread — clarify in-memory scope and MVP flows first."
>
> "Entities: `Post`, `Comment`, `CommentThread`, `SortStrategy`, `ModerationFlag`. Domain structure separate from `CommentService` orchestration."
>
> "Problem: Design nested comments: post, reply, edit, delete, sort top/new."
>
> "`Post` — parent content; owns its own invariants."
>
> "`Comment` — tree node; owns its own invariants."
>
> "`CommentThread` — root collection; owns its own invariants."
>
> "`CommentService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Composite` in isolation?
2. How would you extend Comment Thread without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/comment-thread/README.md) (skeleton)

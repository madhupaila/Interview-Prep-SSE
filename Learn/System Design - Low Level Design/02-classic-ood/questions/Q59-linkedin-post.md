# LinkedIn Post

**Track:** Classic OOD  
**Companies:** LinkedIn, Meta  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O59-linkedin-post.md](../../../Case Studies/lld/classic-ood/CS-LLD-O59-linkedin-post.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the LinkedIn Post domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design professional post: text, mentions, visibility, engagement counts.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for LinkedIn Post? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design professional post? | Include in MVP — Design professional post |
| 5 | Requirement: mentions? | Include in MVP — mentions |
| 6 | Requirement: visibility? | Include in MVP — visibility |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- PostService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via VisibilityPolicy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Post` | Content |
| `Author` | User |
| `Mention` | @user ref |
| `Visibility` | PUBLIC/CONNECTIONS |
| `Engagement` | Like/comment counts |

**Nouns → classes:** `Post`, `Author`, `Mention`, `Visibility`, `Engagement`  
**Verbs → methods:** `getFeed()`, `createPost()`, `addReaction()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  PostService        │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Post               │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Author             │────>│  Mention         │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class PostService {
        +Feed getFeed(User user, Cursor cursor)
        +Post createPost(User author, String content)
        +void addReaction(String postId, Reaction reaction)
    }
    class Post {
        -content: String
        +addReaction(Reaction) void
    }
    class Author {
        +execute() void
    }
    class Mention {
        +execute() void
    }
    class Visibility {
        +execute() void
    }
    class Engagement {
        +execute() void
    }
    PostService --> Post
```

---

## 6. Public API / Key Methods

```java
public class PostService {
    public Feed getFeed(User user, Cursor cursor);
    public Post createPost(User author, String content);
    public void addReaction(String postId, Reaction reaction);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in LinkedIn Post |

**SOLID:**
- **S:** PostService orchestrates; entities hold state
- **O:** New behavior via new VisibilityPolicy impl
- **D:** Depend on VisibilityPolicy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as PostService
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
participant S as PostService
U->>S: getFeed(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `PostService`."
>
> "Add new `Post` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design LinkedIn Post — clarify in-memory scope and MVP flows first."
>
> "Entities: `Post`, `Author`, `Mention`, `Visibility`, `Engagement`. Domain structure separate from `PostService` orchestration."
>
> "Problem: Design professional post: text, mentions, visibility, engagement counts."
>
> "`Post` — content; owns its own invariants."
>
> "`Author` — user; owns its own invariants."
>
> "`Mention` — @user ref; owns its own invariants."
>
> "`PostService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend LinkedIn Post without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/linkedin-post/) (skeleton)

# Friend Request Flow

**Track:** Classic OOD  
**Companies:** Meta, LinkedIn  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O45-friend-request.md](../../../Case Studies/lld/classic-ood/CS-LLD-O45-friend-request.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Friend Request Flow domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design friend requests: send, accept, reject, block, pending state.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Friend Request Flow? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design friend requests? | Include in MVP — Design friend requests |
| 5 | Requirement: accept? | Include in MVP — accept |
| 6 | Requirement: reject? | Include in MVP — reject |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Send messages with delivery status tracking

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via RequestValidator interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `User` | Account |
| `FriendRequest` | Pending invite |
| `Friendship` | Mutual link |
| `BlockList` | Blocked users |
| `RequestStatus` | PENDING/ACCEPTED |

**Nouns → classes:** `User`, `FriendRequest`, `Friendship`, `BlockList`, `RequestStatus`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  FriendService      │──────>│ State            │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteState    │
│  User               │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  FriendRequest      │────>│  Friendship      │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class FriendService {
        +void create(User entity)
        +Optional<User> getById(String id)
        +List<User> listAll()
        +void delete(String id)
    }
    class User {
        -id: String
        -name: String
    }
    class FriendRequest {
        +execute() void
    }
    class Friendship {
        +execute() void
    }
    class BlockList {
        +execute() void
    }
    class RequestStatus {
        +execute() void
    }
    FriendService --> User
```

---

## 6. Public API / Key Methods

```java
public class FriendService {
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
| State | Lifecycle state transitions |

**SOLID:**
- **S:** FriendService orchestrates; entities hold state
- **O:** New behavior via new RequestValidator impl
- **D:** Depend on RequestValidator interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as FriendService
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
participant S as FriendService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `State` implementation plugs in at runtime — no change to `FriendService`."
>
> "Add new `User` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | State | State — 2+ behaviors |
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

> "I'll design Friend Request Flow — clarify in-memory scope and MVP flows first."
>
> "Entities: `User`, `FriendRequest`, `Friendship`, `BlockList`, `RequestStatus`. Domain structure separate from `FriendService` orchestration."
>
> "Problem: Design friend requests: send, accept, reject, block, pending state."
>
> "`User` — account; owns its own invariants."
>
> "`FriendRequest` — pending invite; owns its own invariants."
>
> "`Friendship` — mutual link; owns its own invariants."
>
> "`FriendService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `State` in isolation?
2. How would you extend Friend Request Flow without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/friend-request/README.md) (skeleton)

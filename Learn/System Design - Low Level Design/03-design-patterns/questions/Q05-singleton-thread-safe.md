# Singleton — Thread-Safe Config

**Track:** Design Patterns  
**Companies:** Amazon, Spring  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P05-singleton-thread-safe.md](../../../Case Studies/lld/design-patterns/CS-LLD-P05-singleton-thread-safe.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Singleton — Thread-Safe Config domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design thread-safe singleton config holder with lazy initialization.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Singleton — Thread-Safe Config? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design thread-safe singleton config hold? | Include in MVP — Design thread-safe singleton config holder with la |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- AppConfig handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via AppConfig interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `AppConfig` | Singleton |
| `ConfigProperty` | KV entry |
| `ConfigLoader` | Load from file |

**Nouns → classes:** `AppConfig`, `ConfigProperty`, `ConfigLoader`  
**Verbs → methods:** `addComment()`, `getThread()`, `upvote()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  AppConfig          │──────>│ Singleton        │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteSingleton│
│  AppConfig          │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  ConfigProperty     │────>│  ConfigLoader    │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class AppConfig {
        +Comment addComment(String postId, String text, String parentId)
        +List<Comment> getThread(String postId)
        +void upvote(String commentId)
    }
    class ConfigProperty {
        +execute() void
    }
    class ConfigLoader {
        +execute() void
    }
```

---

## 6. Public API / Key Methods

```java
public class AppConfig {
    public Comment addComment(String postId, String text, String parentId);
    public List<Comment> getThread(String postId);
    public void upvote(String commentId);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Singleton | Single JVM instance |

**SOLID:**
- **S:** AppConfig orchestrates; entities hold state
- **O:** New behavior via new AppConfig impl
- **D:** Depend on AppConfig interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as AppConfig
participant D as AppConfig
U->>S: addComment()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as AppConfig
U->>S: addComment(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Singleton` implementation plugs in at runtime — no change to `AppConfig`."
>
> "Add new `AppConfig` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Singleton | Singleton — 2+ behaviors |
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

> "I'll design Singleton — Thread-Safe Config — clarify in-memory scope and MVP flows first."
>
> "Entities: `AppConfig`, `ConfigProperty`, `ConfigLoader`. Domain structure separate from `AppConfig` orchestration."
>
> "Problem: Design thread-safe singleton config holder with lazy initialization."
>
> "`AppConfig` — singleton; owns its own invariants."
>
> "`ConfigProperty` — kv entry; owns its own invariants."
>
> "`ConfigLoader` — load from file; owns its own invariants."
>
> "`AppConfig` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Singleton` in isolation?
2. How would you extend Singleton — Thread-Safe Config without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/singleton-thread-safe/) (full)

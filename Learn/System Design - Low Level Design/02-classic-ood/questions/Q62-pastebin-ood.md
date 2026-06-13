# Pastebin (OOD)

**Track:** Classic OOD  
**Companies:** Pastebin, GitHub Gist  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O62-pastebin-ood.md](../../../Case Studies/lld/classic-ood/CS-LLD-O62-pastebin-ood.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Pastebin object model — paste, expiry, visibility. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design pastebin: create paste, short URL, expiry, privacy.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Pastebin (OOD)? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design pastebin? | Include in MVP — Design pastebin |
| 5 | Requirement: create paste? | Include in MVP — create paste |
| 6 | Requirement: short URL? | Include in MVP — short URL |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- PastebinService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ExpiryPolicy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Paste` | Content blob |
| `ShortUrl` | Key mapping |
| `Author` | Optional user |
| `ExpiryPolicy` | TTL |
| `AccessLevel` | PUBLIC/UNLISTED |

**Nouns → classes:** `Paste`, `ShortUrl`, `Author`, `ExpiryPolicy`, `AccessLevel`  
**Verbs → methods:** `create()`, `get()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  PastebinService    │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Paste              │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  ShortUrl           │────>│  Author          │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class PastebinService {
        +Paste create(String content, Duration ttl)
        +Optional<Paste> get(String id)
        +void delete(String id)
    }
    class Paste {
        +execute() void
    }
    class ShortUrl {
        +execute() void
    }
    class Author {
        +execute() void
    }
    class ExpiryPolicy {
        <<interface>>
        +apply() void
    }
    class AccessLevel {
        +execute() void
    }
    PastebinService --> Paste
```

---

## 6. Public API / Key Methods

```java
public class PastebinService {
    public Paste create(String content, Duration ttl);
    public Optional<Paste> get(String id);
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable algorithms |

**SOLID:**
- **S:** PastebinService orchestrates; entities hold state
- **O:** New behavior via new ExpiryPolicy impl
- **D:** Depend on ExpiryPolicy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as PastebinService
participant D as Paste
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as PastebinService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `PastebinService`."
>
> "Add new `Paste` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Pastebin (OOD) — clarify in-memory scope and MVP flows first."
>
> "Entities: `Paste`, `ShortUrl`, `Author`, `ExpiryPolicy`, `AccessLevel`. Domain structure separate from `PastebinService` orchestration."
>
> "Problem: Design pastebin: create paste, short URL, expiry, privacy."
>
> "`Paste` — content blob; owns its own invariants."
>
> "`ShortUrl` — key mapping; owns its own invariants."
>
> "`Author` — optional user; owns its own invariants."
>
> "`PastebinService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Pastebin (OOD) without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/pastebin-ood/) (skeleton)

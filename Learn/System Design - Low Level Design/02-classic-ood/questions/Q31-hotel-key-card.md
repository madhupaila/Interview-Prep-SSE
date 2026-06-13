# Hotel Key Card System

**Track:** Classic OOD  
**Companies:** Marriott, Hilton  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O31-hotel-key-card.md](../../../Case Studies/lld/classic-ood/CS-LLD-O31-hotel-key-card.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Hotel Key Card System domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design hotel key card: encode room access, expiry, revoke on checkout.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Hotel Key Card System? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Overbooking? | No — reject overlapping dates |
| 5 | Cancellation? | Policy-based cancel window |
| 6 | Room types? | Enum RoomType |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Checkout and return items with business rules

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via AccessPolicy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `KeyCard` | RFID token |
| `Room` | Access target |
| `Guest` | Holder |
| `AccessPolicy` | Time-bound rules |
| `Encoder` | Write card |

**Nouns → classes:** `KeyCard`, `Room`, `Guest`, `AccessPolicy`, `Encoder`  
**Verbs → methods:** `checkout()`, `returnItem()`, `reserve()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  KeyCardService     │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  KeyCard            │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Room               │────>│  Guest           │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class KeyCardService {
        +Loan checkout(Member member, String id)
        +void returnItem(String id)
        +void reserve(String isbn)
    }
    class KeyCard {
        +execute() void
    }
    class Room {
        +execute() void
    }
    class Guest {
        +execute() void
    }
    class AccessPolicy {
        <<interface>>
        +apply() void
    }
    class Encoder {
        +execute() void
    }
    KeyCardService --> KeyCard
```

---

## 6. Public API / Key Methods

```java
public class KeyCardService {
    public Loan checkout(Member member, String id);
    public void returnItem(String id);
    public void reserve(String isbn);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable algorithms |

**SOLID:**
- **S:** KeyCardService orchestrates; entities hold state
- **O:** New behavior via new AccessPolicy impl
- **D:** Depend on AccessPolicy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as KeyCardService
participant D as KeyCard
U->>S: checkout()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as KeyCardService
U->>S: checkout(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `KeyCardService`."
>
> "Add new `KeyCard` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Hotel Key Card System — clarify in-memory scope and MVP flows first."
>
> "Entities: `KeyCard`, `Room`, `Guest`, `AccessPolicy`, `Encoder`. Domain structure separate from `KeyCardService` orchestration."
>
> "Problem: Design hotel key card: encode room access, expiry, revoke on checkout."
>
> "`KeyCard` — rfid token; owns its own invariants."
>
> "`Room` — access target; owns its own invariants."
>
> "`Guest` — holder; owns its own invariants."
>
> "`KeyCardService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Hotel Key Card System without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/hotel-key-card/) (skeleton)

# Wishlist

**Track:** Classic OOD  
**Companies:** Amazon, Etsy  
**Difficulty:** Easy  

---

## Case Study

> **Full case study:** [CS-LLD-O48-wishlist.md](../../../Case Studies/lld/classic-ood/CS-LLD-O48-wishlist.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Wishlist domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design product wishlist: add, remove, share, price drop notify.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Wishlist? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Share wishlist? | Read-only link to friends |
| 5 | Price alerts? | Observer on price drop |
| 6 | Multiple lists? | One per user MVP |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Deliver notifications via configured channels

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via PriceAlert interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Wishlist` | Item collection |
| `WishlistItem` | Product ref |
| `User` | Owner |
| `Product` | Catalog ref |
| `PriceAlert` | Notification rule |

**Nouns → classes:** `Wishlist`, `WishlistItem`, `User`, `Product`, `PriceAlert`  
**Verbs → methods:** `makeMove()`, `getState()`, `getLegalMoves()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  WishlistService    │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Wishlist           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  WishlistItem       │────>│  User            │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class WishlistService {
        +boolean makeMove(Move move)
        +GameState getState()
        +List<Move> getLegalMoves()
    }
    class Wishlist {
        +addItem(String productId) void
        +removeItem(String productId) void
    }
    class WishlistItem {
        +execute() void
    }
    class User {
        -id: String
        -name: String
    }
    class Product {
        +execute() void
    }
    class PriceAlert {
        +execute() void
    }
    WishlistService --> Wishlist
```

---

## 6. Public API / Key Methods

```java
public class WishlistService {
    public boolean makeMove(Move move);
    public GameState getState();
    public List<Move> getLegalMoves();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in Wishlist |

**SOLID:**
- **S:** WishlistService orchestrates; entities hold state
- **O:** New behavior via new PriceAlert impl
- **D:** Depend on PriceAlert interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as WishlistService
participant D as Wishlist
U->>S: makeMove()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as WishlistService
U->>S: makeMove(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `WishlistService`."
>
> "Add new `Wishlist` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Wishlist — clarify in-memory scope and MVP flows first."
>
> "Entities: `Wishlist`, `WishlistItem`, `User`, `Product`, `PriceAlert`. Domain structure separate from `WishlistService` orchestration."
>
> "Problem: Design product wishlist: add, remove, share, price drop notify."
>
> "`Wishlist` — item collection; owns its own invariants."
>
> "`WishlistItem` — product ref; owns its own invariants."
>
> "`User` — owner; owns its own invariants."
>
> "`WishlistService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Wishlist without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/wishlist/) (skeleton)

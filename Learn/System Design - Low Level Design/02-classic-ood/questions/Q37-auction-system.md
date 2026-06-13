# Auction System

**Track:** Classic OOD  
**Companies:** eBay, Amazon  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O37-auction-system.md](../../../Case Studies/lld/classic-ood/CS-LLD-O37-auction-system.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Auction System domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design auction: place bid, anti-sniping, highest bidder wins.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Auction System? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Bid increment? | Minimum raise rule |
| 5 | Anti-sniping? | Extend end time on late bid |
| 6 | Reserve price? | Optional hidden minimum |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Place bids with validation and winner selection

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via BidValidator interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Auction` | Listing + end time |
| `Bid` | Amount + bidder |
| `Bidder` | User |
| `AuctionStatus` | OPEN/CLOSED |
| `BidValidator` | Min increment |

**Nouns → classes:** `Auction`, `Bid`, `Bidder`, `AuctionStatus`, `BidValidator`  
**Verbs → methods:** `placeBid()`, `getHighestBid()`, `closeAuction()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  AuctionService     │──────>│ State            │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteState    │
│  Auction            │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Bid                │────>│  Bidder          │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class AuctionService {
        +void placeBid(String lotId, BigDecimal amount)
        +Bid getHighestBid(String lotId)
        +void closeAuction(String lotId)
    }
    class Auction {
        +placeBid(Bid) void
        +getWinner() Bidder
    }
    class Bid {
        +execute() void
    }
    class Bidder {
        +execute() void
    }
    class AuctionStatus {
        +execute() void
    }
    class BidValidator {
        +execute() void
    }
    AuctionService --> Auction
```

---

## 6. Public API / Key Methods

```java
public class AuctionService {
    public void placeBid(String lotId, BigDecimal amount);
    public Bid getHighestBid(String lotId);
    public void closeAuction(String lotId);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| State | Lifecycle state transitions |

**SOLID:**
- **S:** AuctionService orchestrates; entities hold state
- **O:** New behavior via new BidValidator impl
- **D:** Depend on BidValidator interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as AuctionService
participant D as Auction
U->>S: placeBid()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as AuctionService
U->>S: placeBid(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `State` implementation plugs in at runtime — no change to `AuctionService`."
>
> "Add new `Auction` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Auction System — clarify in-memory scope and MVP flows first."
>
> "Entities: `Auction`, `Bid`, `Bidder`, `AuctionStatus`, `BidValidator`. Domain structure separate from `AuctionService` orchestration."
>
> "Problem: Design auction: place bid, anti-sniping, highest bidder wins."
>
> "`Auction` — listing + end time; owns its own invariants."
>
> "`Bid` — amount + bidder; owns its own invariants."
>
> "`Bidder` — user; owns its own invariants."
>
> "`AuctionService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `State` in isolation?
2. How would you extend Auction System without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/auction-system/) (full)

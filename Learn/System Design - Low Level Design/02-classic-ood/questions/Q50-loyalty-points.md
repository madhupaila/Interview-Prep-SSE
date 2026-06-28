# Loyalty Points

**Track:** Classic OOD  
**Companies:** Airlines, Starbucks  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O50-loyalty-points.md](../../../Case Studies/lld/classic-ood/CS-LLD-O50-loyalty-points.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Loyalty Points domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design loyalty program: earn on purchase, redeem, tier levels.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Loyalty Points? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design loyalty program? | Include in MVP — Design loyalty program |
| 5 | Requirement: earn on purchase? | Include in MVP — earn on purchase |
| 6 | Requirement: redeem? | Include in MVP — redeem |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- LoyaltyService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via EarningRule interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Member` | Account |
| `PointsLedger` | Earn/burn log |
| `Transaction` | Purchase event |
| `RewardTier` | Silver/gold |
| `Redemption` | Points to discount |

**Nouns → classes:** `Member`, `PointsLedger`, `Transaction`, `RewardTier`, `Redemption`  
**Verbs → methods:** `earnPoints()`, `redeemPoints()`, `getTier()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  LoyaltyService     │──────>│ Command          │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteCommand  │
│  Member             │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  PointsLedger       │────>│  Transaction     │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class LoyaltyService {
        +void earnPoints(String memberId, int points)
        +void redeemPoints(String memberId, int points)
        +RewardTier getTier(String memberId)
    }
    class Member {
        -id: String
        +getActiveLoans() List
    }
    class PointsLedger {
        +execute() void
    }
    class Transaction {
        +execute() void
    }
    class RewardTier {
        +execute() void
    }
    class Redemption {
        +execute() void
    }
    LoyaltyService --> Member
```

---

## 6. Public API / Key Methods

```java
public class LoyaltyService {
    public void earnPoints(String memberId, int points);
    public void redeemPoints(String memberId, int points);
    public RewardTier getTier(String memberId);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Command | Encapsulated operations |

**SOLID:**
- **S:** LoyaltyService orchestrates; entities hold state
- **O:** New behavior via new EarningRule impl
- **D:** Depend on EarningRule interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as LoyaltyService
participant D as Member
U->>S: earnPoints()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as LoyaltyService
U->>S: earnPoints(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Command` implementation plugs in at runtime — no change to `LoyaltyService`."
>
> "Add new `Member` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Command | Command — 2+ behaviors |
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

> "I'll design Loyalty Points — clarify in-memory scope and MVP flows first."
>
> "Entities: `Member`, `PointsLedger`, `Transaction`, `RewardTier`, `Redemption`. Domain structure separate from `LoyaltyService` orchestration."
>
> "Problem: Design loyalty program: earn on purchase, redeem, tier levels."
>
> "`Member` — account; owns its own invariants."
>
> "`PointsLedger` — earn/burn log; owns its own invariants."
>
> "`Transaction` — purchase event; owns its own invariants."
>
> "`LoyaltyService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Command` in isolation?
2. How would you extend Loyalty Points without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/loyalty-points/README.md) (skeleton)

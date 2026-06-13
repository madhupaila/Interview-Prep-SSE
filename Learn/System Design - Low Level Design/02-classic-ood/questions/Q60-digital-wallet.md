# Digital Wallet

**Track:** Classic OOD  
**Companies:** PayPal, Apple Pay  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O60-digital-wallet.md](../../../Case Studies/lld/classic-ood/CS-LLD-O60-digital-wallet.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after PayPal wallet and ledger. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design wallet: balance, P2P transfer, transaction history, KYC stub.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Digital Wallet? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design wallet? | Include in MVP — Design wallet |
| 5 | Requirement: balance? | Include in MVP — balance |
| 6 | Requirement: P2P transfer? | Include in MVP — P2P transfer |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- WalletService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via FraudChecker interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Wallet` | Balance holder |
| `User` | Owner |
| `Transaction` | Ledger entry |
| `Transfer` | P2P move |
| `PaymentMethod` | Linked bank/card |

**Nouns → classes:** `Wallet`, `User`, `Transaction`, `Transfer`, `PaymentMethod`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  WalletService      │──────>│ Command          │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteCommand  │
│  Wallet             │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  User               │────>│  Transaction     │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class WalletService {
        +void create(Wallet entity)
        +Optional<Wallet> getById(String id)
        +List<Wallet> listAll()
        +void delete(String id)
    }
    class Wallet {
        +execute() void
    }
    class User {
        -id: String
        -name: String
    }
    class Transaction {
        +execute() void
    }
    class Transfer {
        +execute() void
    }
    class PaymentMethod {
        +execute() void
    }
    WalletService --> Wallet
```

---

## 6. Public API / Key Methods

```java
public class WalletService {
    public void create(Wallet entity);
    public Optional<Wallet> getById(String id);
    public List<Wallet> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Command | Encapsulated operations |

**SOLID:**
- **S:** WalletService orchestrates; entities hold state
- **O:** New behavior via new FraudChecker impl
- **D:** Depend on FraudChecker interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as WalletService
participant D as Wallet
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as WalletService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Command` implementation plugs in at runtime — no change to `WalletService`."
>
> "Add new `Wallet` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Digital Wallet — clarify in-memory scope and MVP flows first."
>
> "Entities: `Wallet`, `User`, `Transaction`, `Transfer`, `PaymentMethod`. Domain structure separate from `WalletService` orchestration."
>
> "Problem: Design wallet: balance, P2P transfer, transaction history, KYC stub."
>
> "`Wallet` — balance holder; owns its own invariants."
>
> "`User` — owner; owns its own invariants."
>
> "`Transaction` — ledger entry; owns its own invariants."
>
> "`WalletService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Command` in isolation?
2. How would you extend Digital Wallet without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/digital-wallet/) (full)

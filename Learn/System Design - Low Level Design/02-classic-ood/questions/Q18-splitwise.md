# Splitwise Expense Sharing

**Track:** Classic OOD  
**Companies:** Splitwise, Amazon  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O18-splitwise.md](../../../Case Studies/lld/classic-ood/CS-LLD-O18-splitwise.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Splitwise balance simplification graph. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design expense sharing: add bill, split equally/percent, settle balances.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Splitwise Expense Sharing? | Core entities + 2 primary user flows |
| 2 | Persistence required? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded access? | Yes if multiple users/gates — else single-threaded |
| 4 | Split types? | Equal, exact amounts, percentage |
| 5 | Simplify debts? | Optional balance simplification graph |
| 6 | Multi-currency? | Extension |
| 7 | Groups? | Group contains multiple users |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Split expenses and track balances

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via SplitStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `User` | Member |
| `Group` | Expense group |
| `Expense` | Bill record |
| `Split` | Per-user share |
| `BalanceSheet` | Who owes whom |

**Nouns → classes:** `User`, `Group`, `Expense`, `Split`, `BalanceSheet`  
**Verbs → methods:** `addExpense()`, `getBalances()`, `settle()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ExpenseService     │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  User               │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Group              │────>│  Expense         │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ExpenseService {
        +void addExpense(Expense expense)
        +Map<User, BigDecimal> getBalances(Group group)
        +void settle(User from, User to, BigDecimal amount)
    }
    class User {
        -id: String
        -name: String
    }
    class Group {
        +execute() void
    }
    class Expense {
        +execute() void
    }
    class Split {
        +execute() void
    }
    class BalanceSheet {
        +execute() void
    }
    ExpenseService --> User
```

---

## 6. Public API / Key Methods

```java
public class ExpenseService {
    public void addExpense(Expense expense);
    public Map<User, BigDecimal> getBalances(Group group);
    public void settle(User from, User to, BigDecimal amount);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Equal / percent / exact split |

**SOLID:**
- **S:** ExpenseService orchestrates; entities hold state
- **O:** New behavior via new SplitStrategy impl
- **D:** Depend on SplitStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ExpenseService
participant E as Expense
U->>S: addExpense(expense)
S->>E: validateSplit()
S->>S: updateBalances()
S-->>U: ok
```

**Failure path:**

```mermaid
sequenceDiagram
U->>S: addExpense(invalid)
S-->>U: InvalidSplitException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `ExpenseService`."
>
> "Add new `User` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Splitwise Expense Sharing — clarify in-memory scope and MVP flows first."
>
> "Entities: `User`, `Group`, `Expense`, `Split`, `BalanceSheet`. Domain structure separate from `ExpenseService` orchestration."
>
> "Problem: Design expense sharing: add bill, split equally/percent, settle balances."
>
> "`User` — member; owns its own invariants."
>
> "`Group` — expense group; owns its own invariants."
>
> "`Expense` — bill record; owns its own invariants."
>
> "`ExpenseService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Splitwise Expense Sharing without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/splitwise/) (full)

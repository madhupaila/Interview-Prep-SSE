# State — Vending Machine

**Track:** Design Patterns  
**Companies:** Amazon, Coca-Cola  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P15-state-vending-machine.md](../../../Case Studies/lld/design-patterns/CS-LLD-P15-state-vending-machine.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Automated retail state machines. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design state pattern for vending machine phases: idle, coin, dispense.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for State — Vending Machine? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design state pattern for vending machine? | Include in MVP — Design state pattern for vending machine phases |
| 5 | Requirement: dispense.? | Include in MVP — dispense. |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- VendingStateMachine handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via VendingState interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `VendingContext` | Context |
| `VendingState` | State interface |
| `IdleState` | No coin |
| `HasCoinState` | Selection |
| `DispenseState` | Release item |

**Nouns → classes:** `VendingContext`, `VendingState`, `IdleState`, `HasCoinState`, `DispenseState`  
**Verbs → methods:** `insertCoin()`, `selectItem()`, `dispense()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  VendingStateMachine│──────>│ State            │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteState    │
│  VendingContext     │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  VendingState       │────>│  IdleState       │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class VendingStateMachine {
        +void insertCoin(Coin coin)
        +Product selectItem(String code)
        +void dispense()
    }
    class VendingContext {
        +execute() void
    }
    class VendingState {
        <<interface>>
        +insertCoin()
        +selectProduct()
    }
    class IdleState {
        +execute() void
    }
    class HasCoinState {
        +execute() void
    }
    class DispenseState {
        +execute() void
    }
    VendingStateMachine --> VendingContext
```

---

## 6. Public API / Key Methods

```java
public class VendingStateMachine {
    public void insertCoin(Coin coin);
    public Product selectItem(String code);
    public void dispense();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| State | Vending machine lifecycle states |

**SOLID:**
- **S:** VendingStateMachine orchestrates; entities hold state
- **O:** New behavior via new VendingState impl
- **D:** Depend on VendingState interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as VendingStateMachine
participant D as VendingContext
U->>S: insertCoin()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as VendingStateMachine
U->>S: insertCoin(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `State` implementation plugs in at runtime — no change to `VendingStateMachine`."
>
> "Add new `VendingContext` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design State — Vending Machine — clarify in-memory scope and MVP flows first."
>
> "Entities: `VendingContext`, `VendingState`, `IdleState`, `HasCoinState`, `DispenseState`. Domain structure separate from `VendingStateMachine` orchestration."
>
> "Problem: Design state pattern for vending machine phases: idle, coin, dispense."
>
> "`VendingContext` — context; owns its own invariants."
>
> "`VendingState` — state interface; owns its own invariants."
>
> "`IdleState` — no coin; owns its own invariants."
>
> "`VendingStateMachine` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `State` in isolation?
2. How would you extend State — Vending Machine without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/state-vending-machine/VendingMachine.java) (full)

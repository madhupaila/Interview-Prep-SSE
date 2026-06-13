# Chain of Responsibility — Support

**Track:** Design Patterns  
**Companies:** Amazon, Zendesk  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P18-chain-support-tickets.md](../../../Case Studies/lld/design-patterns/CS-LLD-P18-chain-support-tickets.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Chain of Responsibility — Support domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design support ticket escalation: L1 → L2 → L3 handler chain.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Chain of Responsibility — Support? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design support ticket escalation? | Include in MVP — Design support ticket escalation |
| 5 | Requirement: L1 → L2 → L3 handler chain.? | Include in MVP — L1 → L2 → L3 handler chain. |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- SupportChain handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via SupportHandler interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `SupportHandler` | Abstract handler |
| `L1Handler` | Tier 1 |
| `L2Handler` | Tier 2 |
| `Ticket` | Request |
| `EscalationPolicy` | Routing rules |

**Nouns → classes:** `SupportHandler`, `L1Handler`, `L2Handler`, `Ticket`, `EscalationPolicy`  
**Verbs → methods:** `holdSeats()`, `confirm()`, `releaseHold()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  SupportChain       │──────>│ Chain of Responsibility │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteChain of Responsibility│
│  SupportHandler     │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  L1Handler          │────>│  L2Handler       │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class SupportChain {
        +SeatLock holdSeats(Show show, List<Seat> seats)
        +Booking confirm(SeatLock lock)
        +void releaseHold(SeatLock lock)
    }
    class SupportHandler {
        +execute() void
    }
    class L1Handler {
        +execute() void
    }
    class L2Handler {
        +execute() void
    }
    class Ticket {
        -id: String
        -entryTime: Instant
        +getSpot() ParkingSpot
    }
    class EscalationPolicy {
        <<interface>>
        +apply() void
    }
    SupportChain --> SupportHandler
```

---

## 6. Public API / Key Methods

```java
public class SupportChain {
    public SeatLock holdSeats(Show show, List<Seat> seats);
    public Booking confirm(SeatLock lock);
    public void releaseHold(SeatLock lock);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Chain of Responsibility | Demonstrate Chain of Responsibility pattern in chain-support-tickets |

**SOLID:**
- **S:** SupportChain orchestrates; entities hold state
- **O:** New behavior via new SupportHandler impl
- **D:** Depend on SupportHandler interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as SupportChain
participant D as SupportHandler
U->>S: holdSeats()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as SupportChain
U->>S: holdSeats(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Chain of Responsibility` implementation plugs in at runtime — no change to `SupportChain`."
>
> "Add new `SupportHandler` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Chain of Responsibility | Chain of Responsibility — 2+ behaviors |
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

> "I'll design Chain of Responsibility — Support — clarify in-memory scope and MVP flows first."
>
> "Entities: `SupportHandler`, `L1Handler`, `L2Handler`, `Ticket`, `EscalationPolicy`. Domain structure separate from `SupportChain` orchestration."
>
> "Problem: Design support ticket escalation: L1 → L2 → L3 handler chain."
>
> "`SupportHandler` — abstract handler; owns its own invariants."
>
> "`L1Handler` — tier 1; owns its own invariants."
>
> "`L2Handler` — tier 2; owns its own invariants."
>
> "`SupportChain` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Chain of Responsibility` in isolation?
2. How would you extend Chain of Responsibility — Support without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/chain-support-tickets/) (full)

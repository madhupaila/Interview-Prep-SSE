# Kitchen Order Queue

**Track:** Classic OOD  
**Companies:** Restaurant POS  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O52-kitchen-order-queue.md](../../../Case Studies/lld/classic-ood/CS-LLD-O52-kitchen-order-queue.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Kitchen Order Queue domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design kitchen display queue: order priority, prep stations, bump bar.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Kitchen Order Queue? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design kitchen display queue? | Include in MVP — Design kitchen display queue |
| 5 | Requirement: order priority? | Include in MVP — order priority |
| 6 | Requirement: prep stations? | Include in MVP — prep stations |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Execute game turns with rule validation

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via PriorityStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `KitchenQueue` | Order pipeline |
| `OrderTicket` | Kitchen card |
| `Station` | Grill/salad |
| `PriorityStrategy` | Rush first |
| `OrderStatus` | PREP/DONE |

**Nouns → classes:** `KitchenQueue`, `OrderTicket`, `Station`, `PriorityStrategy`, `OrderStatus`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  KitchenService     │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  KitchenQueue       │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  OrderTicket        │────>│  Station         │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class KitchenService {
        +void create(KitchenQueue entity)
        +Optional<KitchenQueue> getById(String id)
        +List<KitchenQueue> listAll()
        +void delete(String id)
    }
    class KitchenQueue {
        +execute() void
    }
    class OrderTicket {
        +execute() void
    }
    class Station {
        +execute() void
    }
    class PriorityStrategy {
        <<interface>>
        +apply() void
    }
    class OrderStatus {
        +execute() void
    }
    KitchenService --> KitchenQueue
```

---

## 6. Public API / Key Methods

```java
public class KitchenService {
    public void create(KitchenQueue entity);
    public Optional<KitchenQueue> getById(String id);
    public List<KitchenQueue> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable algorithms |
| State | Lifecycle state transitions |
| Queue | FIFO ordering of work items |

**SOLID:**
- **S:** KitchenService orchestrates; entities hold state
- **O:** New behavior via new PriorityStrategy impl
- **D:** Depend on PriorityStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as KitchenService
participant D as KitchenQueue
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as KitchenService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `KitchenService`."
>
> "Add new `KitchenQueue` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Kitchen Order Queue — clarify in-memory scope and MVP flows first."
>
> "Entities: `KitchenQueue`, `OrderTicket`, `Station`, `PriorityStrategy`, `OrderStatus`. Domain structure separate from `KitchenService` orchestration."
>
> "Problem: Design kitchen display queue: order priority, prep stations, bump bar."
>
> "`KitchenQueue` — order pipeline; owns its own invariants."
>
> "`OrderTicket` — kitchen card; owns its own invariants."
>
> "`Station` — grill/salad; owns its own invariants."
>
> "`KitchenService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Kitchen Order Queue without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/kitchen-order-queue/) (skeleton)

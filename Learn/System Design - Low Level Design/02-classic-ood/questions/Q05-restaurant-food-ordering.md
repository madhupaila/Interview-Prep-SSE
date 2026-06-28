# Restaurant / Food Ordering

**Track:** Classic OOD  
**Companies:** DoorDash, Uber, Swiggy  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O05-restaurant-food-ordering.md](../../../Case Studies/lld/classic-ood/CS-LLD-O05-restaurant-food-ordering.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Toast POS kitchen display. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design in-restaurant ordering: menu, cart, kitchen queue, order status.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Restaurant / Food Ordering? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design in-restaurant ordering? | Include in MVP — Design in-restaurant ordering |
| 5 | Requirement: kitchen queue? | Include in MVP — kitchen queue |
| 6 | Requirement: order status.? | Include in MVP — order status. |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- OrderService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via OrderState interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Restaurant` | Venue |
| `Menu` | Items |
| `Order` | Customer order |
| `OrderItem` | Line item |
| `KitchenQueue` | Prep queue |
| `OrderStatus` | State enum |

**Nouns → classes:** `Restaurant`, `Menu`, `Order`, `OrderItem`, `KitchenQueue`, `OrderStatus`  
**Verbs → methods:** `addItem()`, `removeItem()`, `checkout()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  OrderService       │──────>│ State            │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteState    │
│  Restaurant         │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Menu               │────>│  Order           │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class OrderService {
        +void addItem(String sku, int qty)
        +void removeItem(String sku)
        +CheckoutResult checkout()
    }
    class Restaurant {
        +execute() void
    }
    class Menu {
        +execute() void
    }
    class Order {
        -items: List
        -status: OrderStatus
        +addItem(Item) void
    }
    class OrderItem {
        +execute() void
    }
    class KitchenQueue {
        +enqueue() void
        +dequeue() Object
    }
    class OrderStatus {
        <<enumeration>>
    }
    OrderService --> Restaurant
```

---

## 6. Public API / Key Methods

```java
public class OrderService {
    public void addItem(String sku, int qty);
    public void removeItem(String sku);
    public CheckoutResult checkout();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| State | Lifecycle state transitions |
| Queue | FIFO ordering of work items |

**SOLID:**
- **S:** OrderService orchestrates; entities hold state
- **O:** New behavior via new OrderState impl
- **D:** Depend on OrderState interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as OrderService
participant D as Restaurant
U->>S: addItem()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as OrderService
U->>S: addItem(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `State` implementation plugs in at runtime — no change to `OrderService`."
>
> "Add new `Restaurant` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Restaurant / Food Ordering — clarify in-memory scope and MVP flows first."
>
> "Entities: `Restaurant`, `Menu`, `Order`, `OrderItem`, `KitchenQueue`, `OrderStatus`. Domain structure separate from `OrderService` orchestration."
>
> "Problem: Design in-restaurant ordering: menu, cart, kitchen queue, order status."
>
> "`Restaurant` — venue; owns its own invariants."
>
> "`Menu` — items; owns its own invariants."
>
> "`Order` — customer order; owns its own invariants."
>
> "`OrderService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `State` in isolation?
2. How would you extend Restaurant / Food Ordering without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/restaurant-food-ordering/README.md) (full)

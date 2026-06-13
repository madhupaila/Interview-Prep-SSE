# Delivery Dispatch

**Track:** Classic OOD  
**Companies:** DoorDash, Amazon, FedEx  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O33-delivery-dispatch.md](../../../Case Studies/lld/classic-ood/CS-LLD-O33-delivery-dispatch.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Delivery Dispatch domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design last-mile dispatch: assign orders to drivers by proximity.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Delivery Dispatch? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design last-mile dispatch? | Include in MVP — Design last-mile dispatch |
| 5 | Requirement: assign orders to drivers by proximity.? | Include in MVP — assign orders to drivers by proximity. |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- DispatchService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via DispatchStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Order` | Delivery request |
| `Driver` | Courier |
| `Route` | Stop sequence |
| `DispatchStrategy` | Assignment algo |
| `DeliveryStatus` | Lifecycle enum |

**Nouns → classes:** `Order`, `Driver`, `Route`, `DispatchStrategy`, `DeliveryStatus`  
**Verbs → methods:** `assignOrder()`, `findNearestDriver()`, `updateStatus()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  DispatchService    │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Order              │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Driver             │────>│  Route           │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class DispatchService {
        +void assignOrder(Order order)
        +Driver findNearestDriver(Location loc)
        +void updateStatus(String orderId, DeliveryStatus status)
    }
    class Order {
        -items: List
        -status: OrderStatus
        +addItem(Item) void
    }
    class Driver {
        -location: Location
        +setAvailable(boolean) void
    }
    class Route {
        +execute() void
    }
    class DispatchStrategy {
        <<interface>>
        +apply() void
    }
    class DeliveryStatus {
        <<enumeration>>
    }
    DispatchService --> Order
```

---

## 6. Public API / Key Methods

```java
public class DispatchService {
    public void assignOrder(Order order);
    public Driver findNearestDriver(Location loc);
    public void updateStatus(String orderId, DeliveryStatus status);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable algorithms |
| State | Lifecycle state transitions |

**SOLID:**
- **S:** DispatchService orchestrates; entities hold state
- **O:** New behavior via new DispatchStrategy impl
- **D:** Depend on DispatchStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as DispatchService
participant D as Order
U->>S: assignOrder()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as DispatchService
U->>S: assignOrder(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `DispatchService`."
>
> "Add new `Order` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Delivery Dispatch — clarify in-memory scope and MVP flows first."
>
> "Entities: `Order`, `Driver`, `Route`, `DispatchStrategy`, `DeliveryStatus`. Domain structure separate from `DispatchService` orchestration."
>
> "Problem: Design last-mile dispatch: assign orders to drivers by proximity."
>
> "`Order` — delivery request; owns its own invariants."
>
> "`Driver` — courier; owns its own invariants."
>
> "`Route` — stop sequence; owns its own invariants."
>
> "`DispatchService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Delivery Dispatch without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/delivery-dispatch/) (full)

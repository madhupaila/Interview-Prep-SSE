# Inventory Management

**Track:** Classic OOD  
**Companies:** Amazon, Walmart  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O23-inventory-management.md](../../../Case Studies/lld/classic-ood/CS-LLD-O23-inventory-management.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Inventory Management domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design warehouse inventory: SKUs, stock levels, reserve, reorder alerts.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Inventory Management? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design warehouse inventory? | Include in MVP — Design warehouse inventory |
| 5 | Requirement: stock levels? | Include in MVP — stock levels |
| 6 | Requirement: reserve? | Include in MVP — reserve |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Create and cancel reservations with conflict checks

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ReorderPolicy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Warehouse` | Storage site |
| `SKU` | Product id |
| `StockLevel` | Quantity on hand |
| `Reservation` | Allocated stock |
| `ReorderPolicy` | Low stock alert |

**Nouns → classes:** `Warehouse`, `SKU`, `StockLevel`, `Reservation`, `ReorderPolicy`  
**Verbs → methods:** `create()`, `cancel()`, `searchAvailable()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  InventoryService   │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Warehouse          │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  SKU                │────>│  StockLevel      │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class InventoryService {
        +Booking create(Guest guest, Room room, LocalDateRange dates)
        +void cancel(String bookingId)
        +List<Room> searchAvailable(RoomType type, LocalDateRange dates)
    }
    class Warehouse {
        +execute() void
    }
    class SKU {
        +execute() void
    }
    class StockLevel {
        +execute() void
    }
    class Reservation {
        +execute() void
    }
    class ReorderPolicy {
        <<interface>>
        +apply() void
    }
    InventoryService --> Warehouse
```

---

## 6. Public API / Key Methods

```java
public class InventoryService {
    public Booking create(Guest guest, Room room, LocalDateRange dates);
    public void cancel(String bookingId);
    public List<Room> searchAvailable(RoomType type, LocalDateRange dates);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable algorithms |

**SOLID:**
- **S:** InventoryService orchestrates; entities hold state
- **O:** New behavior via new ReorderPolicy impl
- **D:** Depend on ReorderPolicy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as InventoryService
participant D as Warehouse
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as InventoryService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `InventoryService`."
>
> "Add new `Warehouse` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Inventory Management — clarify in-memory scope and MVP flows first."
>
> "Entities: `Warehouse`, `SKU`, `StockLevel`, `Reservation`, `ReorderPolicy`. Domain structure separate from `InventoryService` orchestration."
>
> "Problem: Design warehouse inventory: SKUs, stock levels, reserve, reorder alerts."
>
> "`Warehouse` — storage site; owns its own invariants."
>
> "`SKU` — product id; owns its own invariants."
>
> "`StockLevel` — quantity on hand; owns its own invariants."
>
> "`InventoryService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Inventory Management without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/inventory-management/) (full)

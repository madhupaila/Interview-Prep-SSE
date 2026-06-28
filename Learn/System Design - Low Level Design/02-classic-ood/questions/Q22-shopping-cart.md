# Shopping Cart

**Track:** Classic OOD  
**Companies:** Amazon, Walmart, Shopify  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O22-shopping-cart.md](../../../Case Studies/lld/classic-ood/CS-LLD-O22-shopping-cart.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Amazon cart and checkout session. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design e-commerce cart: add/remove items, quantity, apply coupon, checkout.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Shopping Cart? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design e-commerce cart? | Include in MVP — Design e-commerce cart |
| 5 | Requirement: add/remove items? | Include in MVP — add/remove items |
| 6 | Requirement: quantity? | Include in MVP — quantity |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Checkout and return items with business rules

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via DiscountStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `ShoppingCart` | Session cart |
| `CartItem` | SKU + qty |
| `Product` | Catalog item |
| `Customer` | Shopper |
| `Coupon` | Discount rule |

**Nouns → classes:** `ShoppingCart`, `CartItem`, `Product`, `Customer`, `Coupon`  
**Verbs → methods:** `checkout()`, `returnItem()`, `reserve()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  CartService        │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  ShoppingCart       │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  CartItem           │────>│  Product         │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class CartService {
        +Loan checkout(Member member, String id)
        +void returnItem(String id)
        +void reserve(String isbn)
    }
    class ShoppingCart {
        +addItem(SKU, int) void
        +removeItem(SKU) void
        +total() Money
    }
    class CartItem {
        +execute() void
    }
    class Product {
        +execute() void
    }
    class Customer {
        +execute() void
    }
    class Coupon {
        -code: String
        +isValid(Cart) boolean
    }
    CartService --> ShoppingCart
```

---

## 6. Public API / Key Methods

```java
public class CartService {
    public Loan checkout(Member member, String id);
    public void returnItem(String id);
    public void reserve(String isbn);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in Shopping Cart |

**SOLID:**
- **S:** CartService orchestrates; entities hold state
- **O:** New behavior via new DiscountStrategy impl
- **D:** Depend on DiscountStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CartService
participant D as ShoppingCart
U->>S: checkout()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CartService
U->>S: checkout(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `CartService`."
>
> "Add new `ShoppingCart` subtypes or enum values for new categories — Open-Closed."

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

- Per-session cart — ConcurrentHashMap by sessionId if multi-thread
- addItem validates inventory via InventoryService
- checkout is single-use — clear cart after order
- Coupon apply validates expiry and usage limits

---

## 12. Interview Answer Script (15 min)

> "I'll design Shopping Cart — clarify in-memory scope and MVP flows first."
>
> "Entities: `ShoppingCart`, `CartItem`, `Product`, `Customer`, `Coupon`. Domain structure separate from `CartService` orchestration."
>
> "Problem: Design e-commerce cart: add/remove items, quantity, apply coupon, checkout."
>
> "`ShoppingCart` — session cart; owns its own invariants."
>
> "`CartItem` — sku + qty; owns its own invariants."
>
> "`Product` — catalog item; owns its own invariants."
>
> "`CartService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Shopping Cart without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/shopping-cart/README.md) (full)

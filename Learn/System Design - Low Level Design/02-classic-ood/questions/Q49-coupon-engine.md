# Coupon Engine

**Track:** Classic OOD  
**Companies:** Amazon, Shopify  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O49-coupon-engine.md](../../../Case Studies/lld/classic-ood/CS-LLD-O49-coupon-engine.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Coupon Engine domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design coupon engine: percent/fixed off, min cart, expiry, stack rules.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Coupon Engine? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design coupon engine? | Include in MVP — Design coupon engine |
| 5 | Requirement: percent/fixed off? | Include in MVP — percent/fixed off |
| 6 | Requirement: min cart? | Include in MVP — min cart |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- CouponService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via PromotionRule interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Coupon` | Code + rules |
| `Cart` | Order context |
| `Discount` | Applied amount |
| `CouponValidator` | Eligibility |
| `PromotionRule` | Business logic |

**Nouns → classes:** `Coupon`, `Cart`, `Discount`, `CouponValidator`, `PromotionRule`  
**Verbs → methods:** `addItem()`, `removeItem()`, `checkout()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  CouponService      │──────>│ Mediator         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteMediator │
│  Coupon             │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Cart               │────>│  Discount        │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class CouponService {
        +void addItem(String sku, int qty)
        +void removeItem(String sku)
        +CheckoutResult checkout()
    }
    class Coupon {
        -code: String
        +isValid(Cart) boolean
    }
    class Cart {
        +execute() void
    }
    class Discount {
        +execute() void
    }
    class CouponValidator {
        +execute() void
    }
    class PromotionRule {
        +execute() void
    }
    CouponService --> Coupon
```

---

## 6. Public API / Key Methods

```java
public class CouponService {
    public void addItem(String sku, int qty);
    public void removeItem(String sku);
    public CheckoutResult checkout();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Mediator | Decoupled communication |

**SOLID:**
- **S:** CouponService orchestrates; entities hold state
- **O:** New behavior via new PromotionRule impl
- **D:** Depend on PromotionRule interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CouponService
participant D as Coupon
U->>S: addItem()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CouponService
U->>S: addItem(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Mediator` implementation plugs in at runtime — no change to `CouponService`."
>
> "Add new `Coupon` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Mediator | Mediator — 2+ behaviors |
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

> "I'll design Coupon Engine — clarify in-memory scope and MVP flows first."
>
> "Entities: `Coupon`, `Cart`, `Discount`, `CouponValidator`, `PromotionRule`. Domain structure separate from `CouponService` orchestration."
>
> "Problem: Design coupon engine: percent/fixed off, min cart, expiry, stack rules."
>
> "`Coupon` — code + rules; owns its own invariants."
>
> "`Cart` — order context; owns its own invariants."
>
> "`Discount` — applied amount; owns its own invariants."
>
> "`CouponService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Mediator` in isolation?
2. How would you extend Coupon Engine without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/coupon-engine/) (full)

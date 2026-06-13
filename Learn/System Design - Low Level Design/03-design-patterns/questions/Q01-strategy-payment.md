# Strategy — Payment Gateways

**Track:** Design Patterns  
**Companies:** Stripe, Amazon, PayPal  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P01-strategy-payment.md](../../../Case Studies/lld/design-patterns/CS-LLD-P01-strategy-payment.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Stripe multi-gateway payment routing. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design payment processing with swappable gateways (Stripe, PayPal, Apple Pay).

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Strategy — Payment Gateways? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design payment processing with swappable? | Include in MVP — Design payment processing with swappable gateways  |
| 5 | Requirement: PayPal? | Include in MVP — PayPal |
| 6 | Requirement: Apple Pay).? | Include in MVP — Apple Pay). |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- PaymentProcessor handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via PaymentProcessor interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `PaymentProcessor` | Strategy interface |
| `StripeProcessor` | Stripe impl |
| `PayPalProcessor` | PayPal impl |
| `PaymentRequest` | Amount + method |
| `PaymentResult` | Success/fail |

**Nouns → classes:** `PaymentProcessor`, `StripeProcessor`, `PayPalProcessor`, `PaymentRequest`, `PaymentResult`  
**Verbs → methods:** `process()`, `setProcessor()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  PaymentProcessor   │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  PaymentProcessor   │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  StripeProcessor    │────>│  PayPalProcessor │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class PaymentProcessor {
        +PaymentResult process(PaymentRequest request)
        +void setProcessor(PaymentProcessor processor)
    }
    class StripeProcessor {
        +execute() void
    }
    class PayPalProcessor {
        +execute() void
    }
    class PaymentRequest {
        +execute() void
    }
    class PaymentResult {
        +execute() void
    }
```

---

## 6. Public API / Key Methods

```java
public class PaymentProcessor {
    public PaymentResult process(PaymentRequest request);
    public void setProcessor(PaymentProcessor processor);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable payment gateways |

**SOLID:**
- **S:** PaymentProcessor orchestrates; entities hold state
- **O:** New behavior via new PaymentProcessor impl
- **D:** Depend on PaymentProcessor interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as PaymentProcessor
participant D as PaymentProcessor
U->>S: process()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as PaymentProcessor
U->>S: process(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `PaymentProcessor`."
>
> "Add new `PaymentProcessor` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Strategy — Payment Gateways — clarify in-memory scope and MVP flows first."
>
> "Entities: `PaymentProcessor`, `StripeProcessor`, `PayPalProcessor`, `PaymentRequest`, `PaymentResult`. Domain structure separate from `PaymentProcessor` orchestration."
>
> "Problem: Design payment processing with swappable gateways (Stripe, PayPal, Apple Pay)."
>
> "`PaymentProcessor` — strategy interface; owns its own invariants."
>
> "`StripeProcessor` — stripe impl; owns its own invariants."
>
> "`PayPalProcessor` — paypal impl; owns its own invariants."
>
> "`PaymentProcessor` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. Add Apple Pay gateway?
2. Handle idempotent retries?
3. PCI compliance at HLD?
4. Refund flow design?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/strategy-payment/) (full)

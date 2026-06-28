# Adapter — Legacy Payment API

**Track:** Design Patterns  
**Companies:** Banks, Stripe  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P07-adapter-legacy-payment.md](../../../Case Studies/lld/design-patterns/CS-LLD-P07-adapter-legacy-payment.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Adapter — Legacy Payment API domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design adapter wrapping legacy XML payment API behind modern interface.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Adapter — Legacy Payment API? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design adapter wrapping legacy XML payme? | Include in MVP — Design adapter wrapping legacy XML payment API beh |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- PaymentAdapter handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ModernPaymentGateway interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `ModernPaymentGateway` | Target interface |
| `LegacyPaymentAPI` | Adaptee |
| `LegacyPaymentAdapter` | Adapter |
| `PaymentRequest` | DTO |

**Nouns → classes:** `ModernPaymentGateway`, `LegacyPaymentAPI`, `LegacyPaymentAdapter`, `PaymentRequest`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  PaymentAdapter     │──────>│ Adapter          │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteAdapter  │
│  ModernPaymentGateway│       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  LegacyPaymentAPI   │────>│  LegacyPaymentAdapter│
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class PaymentAdapter {
        +void create(ModernPaymentGateway entity)
        +Optional<ModernPaymentGateway> getById(String id)
        +List<ModernPaymentGateway> listAll()
        +void delete(String id)
    }
    class ModernPaymentGateway {
        <<interface>>
        +apply() void
    }
    class LegacyPaymentAPI {
        +execute() void
    }
    class LegacyPaymentAdapter {
        +execute() void
    }
    class PaymentRequest {
        +execute() void
    }
    PaymentAdapter --> ModernPaymentGateway
```

---

## 6. Public API / Key Methods

```java
public class PaymentAdapter {
    public void create(ModernPaymentGateway entity);
    public Optional<ModernPaymentGateway> getById(String id);
    public List<ModernPaymentGateway> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Adapter | Demonstrate Adapter pattern in adapter-legacy-payment |

**SOLID:**
- **S:** PaymentAdapter orchestrates; entities hold state
- **O:** New behavior via new ModernPaymentGateway impl
- **D:** Depend on ModernPaymentGateway interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as PaymentAdapter
participant D as ModernPaymentGateway
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as PaymentAdapter
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Adapter` implementation plugs in at runtime — no change to `PaymentAdapter`."
>
> "Add new `ModernPaymentGateway` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Adapter | Adapter — 2+ behaviors |
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

> "I'll design Adapter — Legacy Payment API — clarify in-memory scope and MVP flows first."
>
> "Entities: `ModernPaymentGateway`, `LegacyPaymentAPI`, `LegacyPaymentAdapter`, `PaymentRequest`. Domain structure separate from `PaymentAdapter` orchestration."
>
> "Problem: Design adapter wrapping legacy XML payment API behind modern interface."
>
> "`ModernPaymentGateway` — target interface; owns its own invariants."
>
> "`LegacyPaymentAPI` — adaptee; owns its own invariants."
>
> "`LegacyPaymentAdapter` — adapter; owns its own invariants."
>
> "`PaymentAdapter` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Adapter` in isolation?
2. How would you extend Adapter — Legacy Payment API without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/adapter-legacy-payment/README.md) (full)

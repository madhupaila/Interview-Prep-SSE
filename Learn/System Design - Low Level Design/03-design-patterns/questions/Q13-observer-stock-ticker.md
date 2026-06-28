# Observer — Stock Price Feed

**Track:** Design Patterns  
**Companies:** Bloomberg, Robinhood  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P13-observer-stock-ticker.md](../../../Case Studies/lld/design-patterns/CS-LLD-P13-observer-stock-ticker.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Bloomberg real-time price feeds. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design observer for stock price updates to multiple display widgets.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Observer — Stock Price Feed? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design observer for stock price updates ? | Include in MVP — Design observer for stock price updates to multipl |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Execute game turns with rule validation

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via Observer interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `StockTicker` | Subject |
| `Observer` | Listener |
| `PriceDisplay` | Concrete observer |
| `Stock` | Symbol + price |

**Nouns → classes:** `StockTicker`, `Observer`, `PriceDisplay`, `Stock`  
**Verbs → methods:** `reserve()`, `release()`, `getAvailable()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  StockTicker        │──────>│ Observer         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteObserver │
│  StockTicker        │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Observer           │────>│  PriceDisplay    │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class StockTicker {
        +void reserve(String sku, int qty)
        +void release(String sku, int qty)
        +int getAvailable(String sku)
    }
    class Observer {
        +execute() void
    }
    class PriceDisplay {
        +execute() void
    }
    class Stock {
        +execute() void
    }
```

---

## 6. Public API / Key Methods

```java
public class StockTicker {
    public void reserve(String sku, int qty);
    public void release(String sku, int qty);
    public int getAvailable(String sku);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Observer | Price change notifies investors |

**SOLID:**
- **S:** StockTicker orchestrates; entities hold state
- **O:** New behavior via new Observer impl
- **D:** Depend on Observer interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as StockTicker
participant D as StockTicker
U->>S: reserve()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as StockTicker
U->>S: reserve(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Observer` implementation plugs in at runtime — no change to `StockTicker`."
>
> "Add new `StockTicker` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Observer | Observer — 2+ behaviors |
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

> "I'll design Observer — Stock Price Feed — clarify in-memory scope and MVP flows first."
>
> "Entities: `StockTicker`, `Observer`, `PriceDisplay`, `Stock`. Domain structure separate from `StockTicker` orchestration."
>
> "Problem: Design observer for stock price updates to multiple display widgets."
>
> "`StockTicker` — subject; owns its own invariants."
>
> "`Observer` — listener; owns its own invariants."
>
> "`PriceDisplay` — concrete observer; owns its own invariants."
>
> "`StockTicker` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Observer` in isolation?
2. How would you extend Observer — Stock Price Feed without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/observer-stock-ticker/Stock.java) (full)

# Token Budget Manager

**Track:** Gen AI LLD  
**Companies:** OpenAI, Anthropic  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-A05-token-budget-manager.md](../../../Case Studies/lld/genai/CS-LLD-A05-token-budget-manager.md)
> **End-to-end pair:** [Token Budget & Cost Control](../../../Case Studies/paired/CS-PAIR-20-token-budget-cost.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after OpenAI token counting and context window limits. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design token budget allocator across system, history, retrieval, response.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Token Budget Manager? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Vector DB? | HLD — stub interface in LLD |
| 5 | Streaming? | Extension |
| 6 | Token limits? | Budget manager or truncate |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- TokenBudgetManager handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via TruncationStrategy interface at variation points
- Constructor injection for testability
- Swappable pipeline stages behind interfaces
- Explicit boundary to HLD for vector DB, model serving, queues

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `TokenBudget` | Limits |
| `BudgetAllocator` | Split tokens |
| `TokenCounter` | Estimate |
| `TruncationStrategy` | Trim policy |

**Nouns → classes:** `TokenBudget`, `BudgetAllocator`, `TokenCounter`, `TruncationStrategy`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  TokenBudgetManager │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  TokenBudget        │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  BudgetAllocator    │────>│  TokenCounter    │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class TokenBudgetManager {
        +void create(TokenBudget entity)
        +Optional<TokenBudget> getById(String id)
        +List<TokenBudget> listAll()
        +void delete(String id)
    }
    class TokenBudget {
        +execute() void
    }
    class BudgetAllocator {
        +execute() void
    }
    class TokenCounter {
        +execute() void
    }
    class TruncationStrategy {
        <<interface>>
        +apply() void
    }
    TokenBudgetManager --> TokenBudget
```

---

## 6. Public API / Key Methods

```java
public class TokenBudgetManager {
    public void create(TokenBudget entity);
    public Optional<TokenBudget> getById(String id);
    public List<TokenBudget> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable pipeline components |
| Chain of Responsibility | Sequential processing stages |

**SOLID:**
- **S:** TokenBudgetManager orchestrates; entities hold state
- **O:** New behavior via new TruncationStrategy impl
- **D:** Depend on TruncationStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as TokenBudgetManager
participant D as TokenBudget
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as TokenBudgetManager
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `TokenBudgetManager`."
>
> "Add new `TokenBudget` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Token Budget Manager — clarify in-memory scope and MVP flows first."
>
> "Entities: `TokenBudget`, `BudgetAllocator`, `TokenCounter`, `TruncationStrategy`. Domain structure separate from `TokenBudgetManager` orchestration."
>
> "Problem: Design token budget allocator across system, history, retrieval, response."
>
> "`TokenBudget` — limits; owns its own invariants."
>
> "`BudgetAllocator` — split tokens; owns its own invariants."
>
> "`TokenCounter` — estimate; owns its own invariants."
>
> "`TokenBudgetManager` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Token Budget Manager without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Gen AI LLD memory map](../../05-genai-llm-lld/memory-map-genai-lld.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/genai/token-budget-manager/README.md) (skeleton)

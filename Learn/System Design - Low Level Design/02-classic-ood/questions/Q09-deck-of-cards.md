# Deck of Cards

**Track:** Classic OOD  
**Companies:** Amazon, Microsoft  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O09-deck-of-cards.md](../../../Case Studies/lld/classic-ood/CS-LLD-O09-deck-of-cards.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Deck of Cards domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design a deck of cards supporting shuffle, deal, and card games (blackjack MVP).

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Deck of Cards? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design a deck of cards supporting shuffl? | Include in MVP — Design a deck of cards supporting shuffle |
| 5 | Requirement: and card games (blackjack MVP).? | Include in MVP — and card games (blackjack MVP). |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- DeckService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ShuffleStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Card` | Suit + rank |
| `Deck` | 52 cards |
| `Hand` | Player cards |
| `ShuffleStrategy` | Randomize order |
| `Game` | Blackjack rules |

**Nouns → classes:** `Card`, `Deck`, `Hand`, `ShuffleStrategy`, `Game`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  DeckService        │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Card               │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Deck               │────>│  Hand            │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class DeckService {
        +void create(Card entity)
        +Optional<Card> getById(String id)
        +List<Card> listAll()
        +void delete(String id)
    }
    class Card {
        +execute() void
    }
    class Deck {
        +execute() void
    }
    class Hand {
        +execute() void
    }
    class ShuffleStrategy {
        <<interface>>
        +apply() void
    }
    class Game {
        +execute() void
    }
    DeckService --> Card
```

---

## 6. Public API / Key Methods

```java
public class DeckService {
    public void create(Card entity);
    public Optional<Card> getById(String id);
    public List<Card> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable algorithms |

**SOLID:**
- **S:** DeckService orchestrates; entities hold state
- **O:** New behavior via new ShuffleStrategy impl
- **D:** Depend on ShuffleStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as DeckService
participant D as Card
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as DeckService
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `DeckService`."
>
> "Add new `Card` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Deck of Cards — clarify in-memory scope and MVP flows first."
>
> "Entities: `Card`, `Deck`, `Hand`, `ShuffleStrategy`, `Game`. Domain structure separate from `DeckService` orchestration."
>
> "Problem: Design a deck of cards supporting shuffle, deal, and card games (blackjack MVP)."
>
> "`Card` — suit + rank; owns its own invariants."
>
> "`Deck` — 52 cards; owns its own invariants."
>
> "`Hand` — player cards; owns its own invariants."
>
> "`DeckService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Deck of Cards without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/deck-of-cards/Demo.java) (full)

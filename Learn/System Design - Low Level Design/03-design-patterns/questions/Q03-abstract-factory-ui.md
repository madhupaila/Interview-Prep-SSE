# Abstract Factory — UI Themes

**Track:** Design Patterns  
**Companies:** Adobe, Microsoft  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-LLD-P03-abstract-factory-ui.md](../../../Case Studies/lld/design-patterns/CS-LLD-P03-abstract-factory-ui.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Abstract Factory — UI Themes domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design abstract factory for Light/Dark UI component families (Button, Checkbox).

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Abstract Factory — UI Themes? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design abstract factory for Light/Dark U? | Include in MVP — Design abstract factory for Light/Dark UI componen |
| 5 | Requirement: Checkbox).? | Include in MVP — Checkbox). |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- UIFactory handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via UIFactory interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `UIFactory` | Abstract factory |
| `LightThemeFactory` | Light widgets |
| `DarkThemeFactory` | Dark widgets |
| `Button` | Widget |
| `Checkbox` | Widget |

**Nouns → classes:** `UIFactory`, `LightThemeFactory`, `DarkThemeFactory`, `Button`, `Checkbox`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  UIFactory          │──────>│ Abstract Factory │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteAbstract Factory│
│  UIFactory          │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  LightThemeFactory  │────>│  DarkThemeFactory│
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class UIFactory {
        +void create(UIFactory entity)
        +Optional<UIFactory> getById(String id)
        +List<UIFactory> listAll()
        +void delete(String id)
    }
    class LightThemeFactory {
        +execute() void
    }
    class DarkThemeFactory {
        +execute() void
    }
    class Button {
        +execute() void
    }
    class Checkbox {
        +execute() void
    }
```

---

## 6. Public API / Key Methods

```java
public class UIFactory {
    public void create(UIFactory entity);
    public Optional<UIFactory> getById(String id);
    public List<UIFactory> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Abstract Factory | Demonstrate Abstract Factory pattern in abstract-factory-ui |

**SOLID:**
- **S:** UIFactory orchestrates; entities hold state
- **O:** New behavior via new UIFactory impl
- **D:** Depend on UIFactory interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as UIFactory
participant D as UIFactory
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as UIFactory
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Abstract Factory` implementation plugs in at runtime — no change to `UIFactory`."
>
> "Add new `UIFactory` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Abstract Factory | Abstract Factory — 2+ behaviors |
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

> "I'll design Abstract Factory — UI Themes — clarify in-memory scope and MVP flows first."
>
> "Entities: `UIFactory`, `LightThemeFactory`, `DarkThemeFactory`, `Button`, `Checkbox`. Domain structure separate from `UIFactory` orchestration."
>
> "Problem: Design abstract factory for Light/Dark UI component families (Button, Checkbox)."
>
> "`UIFactory` — abstract factory; owns its own invariants."
>
> "`LightThemeFactory` — light widgets; owns its own invariants."
>
> "`DarkThemeFactory` — dark widgets; owns its own invariants."
>
> "`UIFactory` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Abstract Factory` in isolation?
2. How would you extend Abstract Factory — UI Themes without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/abstract-factory-ui/README.md) (full)

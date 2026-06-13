# Config Manager

**Track:** Classic OOD  
**Companies:** Netflix, Spring  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O64-config-manager.md](../../../Case Studies/lld/classic-ood/CS-LLD-O64-config-manager.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Netflix Archaius dynamic config. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design dynamic config: key-value, environment overrides, change listeners.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Config Manager? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design dynamic config? | Include in MVP — Design dynamic config |
| 5 | Requirement: key-value? | Include in MVP — key-value |
| 6 | Requirement: environment overrides? | Include in MVP — environment overrides |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- ConfigManager handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ConfigSource interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `ConfigStore` | KV source |
| `ConfigKey` | Namespaced key |
| `ConfigSnapshot` | Immutable view |
| `ConfigListener` | Change callback |
| `Environment` | dev/prod overlay |

**Nouns → classes:** `ConfigStore`, `ConfigKey`, `ConfigSnapshot`, `ConfigListener`, `Environment`  
**Verbs → methods:** `requestRide()`, `acceptTrip()`, `completeTrip()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ConfigManager      │──────>│ Observer         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteObserver │
│  ConfigStore        │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  ConfigKey          │────>│  ConfigSnapshot  │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ConfigManager {
        +Trip requestRide(Rider rider, Location pickup, Location dropoff)
        +void acceptTrip(Driver driver, String tripId)
        +void completeTrip(String tripId)
    }
    class ConfigStore {
        +execute() void
    }
    class ConfigKey {
        +execute() void
    }
    class ConfigSnapshot {
        +execute() void
    }
    class ConfigListener {
        +execute() void
    }
    class Environment {
        +execute() void
    }
    ConfigManager --> ConfigStore
```

---

## 6. Public API / Key Methods

```java
public class ConfigManager {
    public Trip requestRide(Rider rider, Location pickup, Location dropoff);
    public void acceptTrip(Driver driver, String tripId);
    public void completeTrip(String tripId);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Observer | Event notification |
| Repository | Persistence abstraction |

**SOLID:**
- **S:** ConfigManager orchestrates; entities hold state
- **O:** New behavior via new ConfigSource impl
- **D:** Depend on ConfigSource interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ConfigManager
participant D as ConfigStore
U->>S: requestRide()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ConfigManager
U->>S: requestRide(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Observer` implementation plugs in at runtime — no change to `ConfigManager`."
>
> "Add new `ConfigStore` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Config Manager — clarify in-memory scope and MVP flows first."
>
> "Entities: `ConfigStore`, `ConfigKey`, `ConfigSnapshot`, `ConfigListener`, `Environment`. Domain structure separate from `ConfigManager` orchestration."
>
> "Problem: Design dynamic config: key-value, environment overrides, change listeners."
>
> "`ConfigStore` — kv source; owns its own invariants."
>
> "`ConfigKey` — namespaced key; owns its own invariants."
>
> "`ConfigSnapshot` — immutable view; owns its own invariants."
>
> "`ConfigManager` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Observer` in isolation?
2. How would you extend Config Manager without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/config-manager/) (full)

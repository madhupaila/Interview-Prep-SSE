# Flyweight — Forest Scene

**Track:** Design Patterns  
**Companies:** Unity, EA  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P21-flyweight-forest.md](../../../Case Studies/lld/design-patterns/CS-LLD-P21-flyweight-forest.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Flyweight — Forest Scene domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design flyweight sharing tree intrinsic state (type) across thousands of instances.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Flyweight — Forest Scene? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design flyweight sharing tree intrinsic ? | Include in MVP — Design flyweight sharing tree intrinsic state (typ |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- TreeFlyweight handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via TreeType interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `TreeType` | Flyweight |
| `Tree` | Extrinsic position |
| `Forest` | Object pool |
| `TreeFactory` | Cache flyweights |

**Nouns → classes:** `TreeType`, `Tree`, `Forest`, `TreeFactory`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  TreeFlyweight      │──────>│ Flyweight        │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteFlyweight│
│  TreeType           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Tree               │────>│  Forest          │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class TreeFlyweight {
        +void create(TreeType entity)
        +Optional<TreeType> getById(String id)
        +List<TreeType> listAll()
        +void delete(String id)
    }
    class TreeType {
        +execute() void
    }
    class Tree {
        +execute() void
    }
    class Forest {
        +execute() void
    }
    class TreeFactory {
        +execute() void
    }
    TreeFlyweight --> TreeType
```

---

## 6. Public API / Key Methods

```java
public class TreeFlyweight {
    public void create(TreeType entity);
    public Optional<TreeType> getById(String id);
    public List<TreeType> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Flyweight | Shared tree mesh per type |

**SOLID:**
- **S:** TreeFlyweight orchestrates; entities hold state
- **O:** New behavior via new TreeType impl
- **D:** Depend on TreeType interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as TreeFlyweight
participant D as TreeType
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as TreeFlyweight
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Flyweight` implementation plugs in at runtime — no change to `TreeFlyweight`."
>
> "Add new `TreeType` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Flyweight | Flyweight — 2+ behaviors |
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

> "I'll design Flyweight — Forest Scene — clarify in-memory scope and MVP flows first."
>
> "Entities: `TreeType`, `Tree`, `Forest`, `TreeFactory`. Domain structure separate from `TreeFlyweight` orchestration."
>
> "Problem: Design flyweight sharing tree intrinsic state (type) across thousands of instances."
>
> "`TreeType` — flyweight; owns its own invariants."
>
> "`Tree` — extrinsic position; owns its own invariants."
>
> "`Forest` — object pool; owns its own invariants."
>
> "`TreeFlyweight` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Flyweight` in isolation?
2. How would you extend Flyweight — Forest Scene without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/flyweight-forest/README.md) (full)

# Bridge — Remote Control

**Track:** Design Patterns  
**Companies:** Samsung, LG  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P12-bridge-remote-control.md](../../../Case Studies/lld/design-patterns/CS-LLD-P12-bridge-remote-control.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Bridge — Remote Control domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design bridge separating remote abstraction from device implementation.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Bridge — Remote Control? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design bridge separating remote abstract? | Include in MVP — Design bridge separating remote abstraction from d |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- RemoteBridge handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via Device interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Remote` | Abstraction |
| `Device` | Implementor |
| `TV` | Device impl |
| `Radio` | Device impl |
| `AdvancedRemote` | Extended abstraction |

**Nouns → classes:** `Remote`, `Device`, `TV`, `Radio`, `AdvancedRemote`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  RemoteBridge       │──────>│ Bridge           │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteBridge   │
│  Remote             │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Device             │────>│  TV              │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class RemoteBridge {
        +void create(Remote entity)
        +Optional<Remote> getById(String id)
        +List<Remote> listAll()
        +void delete(String id)
    }
    class Remote {
        +execute() void
    }
    class Device {
        +execute() void
    }
    class TV {
        +execute() void
    }
    class Radio {
        +execute() void
    }
    class AdvancedRemote {
        +execute() void
    }
    RemoteBridge --> Remote
```

---

## 6. Public API / Key Methods

```java
public class RemoteBridge {
    public void create(Remote entity);
    public Optional<Remote> getById(String id);
    public List<Remote> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Bridge | Demonstrate Bridge pattern in bridge-remote-control |

**SOLID:**
- **S:** RemoteBridge orchestrates; entities hold state
- **O:** New behavior via new Device impl
- **D:** Depend on Device interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as RemoteBridge
participant D as Remote
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as RemoteBridge
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Bridge` implementation plugs in at runtime — no change to `RemoteBridge`."
>
> "Add new `Remote` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Bridge | Bridge — 2+ behaviors |
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

> "I'll design Bridge — Remote Control — clarify in-memory scope and MVP flows first."
>
> "Entities: `Remote`, `Device`, `TV`, `Radio`, `AdvancedRemote`. Domain structure separate from `RemoteBridge` orchestration."
>
> "Problem: Design bridge separating remote abstraction from device implementation."
>
> "`Remote` — abstraction; owns its own invariants."
>
> "`Device` — implementor; owns its own invariants."
>
> "`TV` — device impl; owns its own invariants."
>
> "`RemoteBridge` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Bridge` in isolation?
2. How would you extend Bridge — Remote Control without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/bridge-remote-control/) (full)

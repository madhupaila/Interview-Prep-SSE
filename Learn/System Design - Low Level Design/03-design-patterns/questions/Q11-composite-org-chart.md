# Composite — Org Chart

**Track:** Design Patterns  
**Companies:** Workday, SAP  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P11-composite-org-chart.md](../../../Case Studies/lld/design-patterns/CS-LLD-P11-composite-org-chart.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Composite — Org Chart domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design composite for org chart: Employee leaf and Department composite.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Composite — Org Chart? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design composite for org chart? | Include in MVP — Design composite for org chart |
| 5 | Requirement: Employee leaf and Department composite.? | Include in MVP — Employee leaf and Department composite. |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- OrgComposite handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via OrgComponent interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `OrgComponent` | Component |
| `Employee` | Leaf |
| `Department` | Composite |
| `OrgChart` | Root tree |

**Nouns → classes:** `OrgComponent`, `Employee`, `Department`, `OrgChart`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  OrgComposite       │──────>│ Composite        │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteComposite│
│  OrgComponent       │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Employee           │────>│  Department      │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class OrgComposite {
        +void create(OrgComponent entity)
        +Optional<OrgComponent> getById(String id)
        +List<OrgComponent> listAll()
        +void delete(String id)
    }
    class OrgComponent {
        +execute() void
    }
    class Employee {
        +execute() void
    }
    class Department {
        +execute() void
    }
    class OrgChart {
        +execute() void
    }
    OrgComposite --> OrgComponent
```

---

## 6. Public API / Key Methods

```java
public class OrgComposite {
    public void create(OrgComponent entity);
    public Optional<OrgComponent> getById(String id);
    public List<OrgComponent> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Composite | Manager contains employees |

**SOLID:**
- **S:** OrgComposite orchestrates; entities hold state
- **O:** New behavior via new OrgComponent impl
- **D:** Depend on OrgComponent interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as OrgComposite
participant D as OrgComponent
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as OrgComposite
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Composite` implementation plugs in at runtime — no change to `OrgComposite`."
>
> "Add new `OrgComponent` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Composite | Composite — 2+ behaviors |
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

> "I'll design Composite — Org Chart — clarify in-memory scope and MVP flows first."
>
> "Entities: `OrgComponent`, `Employee`, `Department`, `OrgChart`. Domain structure separate from `OrgComposite` orchestration."
>
> "Problem: Design composite for org chart: Employee leaf and Department composite."
>
> "`OrgComponent` — component; owns its own invariants."
>
> "`Employee` — leaf; owns its own invariants."
>
> "`Department` — composite; owns its own invariants."
>
> "`OrgComposite` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Composite` in isolation?
2. How would you extend Composite — Org Chart without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/composite-org-chart/) (full)

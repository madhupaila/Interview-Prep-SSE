# Multi-Agent Coordinator

**Track:** Gen AI LLD  
**Companies:** OpenAI, Microsoft  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-LLD-A10-multi-agent-coordinator.md](../../../Case Studies/lld/genai/CS-LLD-A10-multi-agent-coordinator.md)
> **End-to-end pair:** [Multi-Agent Workflow Platform](../../../Case Studies/paired/CS-PAIR-08-multi-agent-workflow.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after CrewAI task delegation between agents. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design coordinator routing tasks between specialist agents with shared state.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Multi-Agent Coordinator? | Core entities + 2 primary flows; extensions deferred |
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
- AgentCoordinator handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via RoutingPolicy interface at variation points
- Constructor injection for testability
- Swappable pipeline stages behind interfaces
- Explicit boundary to HLD for vector DB, model serving, queues

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Coordinator` | Orchestrator |
| `Agent` | Specialist |
| `Task` | Work unit |
| `SharedState` | Blackboard |
| `RoutingPolicy` | Agent pick |

**Nouns → classes:** `Coordinator`, `Agent`, `Task`, `SharedState`, `RoutingPolicy`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  AgentCoordinator   │──────>│ Mediator         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteMediator │
│  Coordinator        │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Agent              │────>│  Task            │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class AgentCoordinator {
        +void create(Coordinator entity)
        +Optional<Coordinator> getById(String id)
        +List<Coordinator> listAll()
        +void delete(String id)
    }
    class Coordinator {
        +execute() void
    }
    class Agent {
        +execute() void
    }
    class Task {
        +execute() void
    }
    class SharedState {
        +execute() void
    }
    class RoutingPolicy {
        <<interface>>
        +apply() void
    }
    AgentCoordinator --> Coordinator
```

---

## 6. Public API / Key Methods

```java
public class AgentCoordinator {
    public void create(Coordinator entity);
    public Optional<Coordinator> getById(String id);
    public List<Coordinator> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Mediator | Supervisor routes to workers |
| Strategy | Task routing |

**SOLID:**
- **S:** AgentCoordinator orchestrates; entities hold state
- **O:** New behavior via new RoutingPolicy impl
- **D:** Depend on RoutingPolicy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as AgentCoordinator
participant D as Coordinator
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as AgentCoordinator
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Mediator` implementation plugs in at runtime — no change to `AgentCoordinator`."
>
> "Add new `Coordinator` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Mediator | Mediator — 2+ behaviors |
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

> "I'll design Multi-Agent Coordinator — clarify in-memory scope and MVP flows first."
>
> "Entities: `Coordinator`, `Agent`, `Task`, `SharedState`, `RoutingPolicy`. Domain structure separate from `AgentCoordinator` orchestration."
>
> "Problem: Design coordinator routing tasks between specialist agents with shared state."
>
> "`Coordinator` — orchestrator; owns its own invariants."
>
> "`Agent` — specialist; owns its own invariants."
>
> "`Task` — work unit; owns its own invariants."
>
> "`AgentCoordinator` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Mediator` in isolation?
2. How would you extend Multi-Agent Coordinator without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Gen AI LLD memory map](../../05-genai-llm-lld/memory-map-genai-lld.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/genai/multi-agent-coordinator/) (skeleton)
- [HLD counterpart](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q08-multi-agent-workflow.md)

# Streaming Response Aggregator

**Track:** Gen AI LLD  
**Companies:** OpenAI, Google  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-A09-streaming-response-aggregator.md](../../../Case Studies/lld/genai/CS-LLD-A09-streaming-response-aggregator.md)
> **End-to-end pair:** [Streaming LLM Responses](../../../Case Studies/paired/CS-PAIR-17-streaming-llm.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after ChatGPT SSE streaming and token aggregation. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design aggregator collecting streamed LLM tokens into final response + callbacks.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Streaming Response Aggregator? | Core entities + 2 primary flows; extensions deferred |
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
- StreamAggregator handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via StreamCallback interface at variation points
- Constructor injection for testability
- Swappable pipeline stages behind interfaces
- Explicit boundary to HLD for vector DB, model serving, queues

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `StreamAggregator` | Collector |
| `TokenChunk` | Delta |
| `StreamCallback` | Listener |
| `CompletionBuffer` | Assembly |

**Nouns → classes:** `StreamAggregator`, `TokenChunk`, `StreamCallback`, `CompletionBuffer`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  StreamAggregator   │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  StreamAggregator   │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  TokenChunk         │────>│  StreamCallback  │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class StreamAggregator {
        +void create(StreamAggregator entity)
        +Optional<StreamAggregator> getById(String id)
        +List<StreamAggregator> listAll()
        +void delete(String id)
    }
    class TokenChunk {
        +execute() void
    }
    class StreamCallback {
        +execute() void
    }
    class CompletionBuffer {
        +execute() void
    }
```

---

## 6. Public API / Key Methods

```java
public class StreamAggregator {
    public void create(StreamAggregator entity);
    public Optional<StreamAggregator> getById(String id);
    public List<StreamAggregator> listAll();
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
- **S:** StreamAggregator orchestrates; entities hold state
- **O:** New behavior via new StreamCallback impl
- **D:** Depend on StreamCallback interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as StreamAggregator
participant D as StreamAggregator
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as StreamAggregator
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `StreamAggregator`."
>
> "Add new `StreamAggregator` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Streaming Response Aggregator — clarify in-memory scope and MVP flows first."
>
> "Entities: `StreamAggregator`, `TokenChunk`, `StreamCallback`, `CompletionBuffer`. Domain structure separate from `StreamAggregator` orchestration."
>
> "Problem: Design aggregator collecting streamed LLM tokens into final response + callbacks."
>
> "`StreamAggregator` — collector; owns its own invariants."
>
> "`TokenChunk` — delta; owns its own invariants."
>
> "`StreamCallback` — listener; owns its own invariants."
>
> "`StreamAggregator` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Streaming Response Aggregator without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Gen AI LLD memory map](../../05-genai-llm-lld/memory-map-genai-lld.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/genai/streaming-response-aggregator/) (skeleton)

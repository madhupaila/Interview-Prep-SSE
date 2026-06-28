# LLM Provider Abstraction

**Track:** Gen AI LLD  
**Companies:** Anthropic, OpenAI  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-A06-llm-provider-abstraction.md](../../../Case Studies/lld/genai/CS-LLD-A06-llm-provider-abstraction.md)
> **End-to-end pair:** [LLM API Gateway / Model Router](../../../Case Studies/paired/CS-PAIR-10-llm-api-gateway.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after LiteLLM — unified provider interface. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design provider interface swapping OpenAI, Anthropic, local models.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for LLM Provider Abstraction? | Core entities + 2 primary flows; extensions deferred |
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
- LLMProvider handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via LLMProvider interface at variation points
- Constructor injection for testability
- Swappable pipeline stages behind interfaces
- Explicit boundary to HLD for vector DB, model serving, queues

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `LLMProvider` | Interface |
| `OpenAIProvider` | Impl |
| `AnthropicProvider` | Impl |
| `CompletionRequest` | Prompt |
| `CompletionResponse` | Text |

**Nouns → classes:** `LLMProvider`, `OpenAIProvider`, `AnthropicProvider`, `CompletionRequest`, `CompletionResponse`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  LLMProvider        │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  LLMProvider        │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  OpenAIProvider     │────>│  AnthropicProvider│
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class LLMProvider {
        +void create(LLMProvider entity)
        +Optional<LLMProvider> getById(String id)
        +List<LLMProvider> listAll()
        +void delete(String id)
    }
    class OpenAIProvider {
        +execute() void
    }
    class AnthropicProvider {
        +execute() void
    }
    class CompletionRequest {
        +execute() void
    }
    class CompletionResponse {
        +execute() void
    }
```

---

## 6. Public API / Key Methods

```java
public class LLMProvider {
    public void create(LLMProvider entity);
    public Optional<LLMProvider> getById(String id);
    public List<LLMProvider> listAll();
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
- **S:** LLMProvider orchestrates; entities hold state
- **O:** New behavior via new LLMProvider impl
- **D:** Depend on LLMProvider interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as LLMProvider
participant D as LLMProvider
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as LLMProvider
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `LLMProvider`."
>
> "Add new `LLMProvider` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design LLM Provider Abstraction — clarify in-memory scope and MVP flows first."
>
> "Entities: `LLMProvider`, `OpenAIProvider`, `AnthropicProvider`, `CompletionRequest`, `CompletionResponse`. Domain structure separate from `LLMProvider` orchestration."
>
> "Problem: Design provider interface swapping OpenAI, Anthropic, local models."
>
> "`LLMProvider` — interface; owns its own invariants."
>
> "`OpenAIProvider` — impl; owns its own invariants."
>
> "`AnthropicProvider` — impl; owns its own invariants."
>
> "`LLMProvider` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend LLM Provider Abstraction without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Gen AI LLD memory map](../../05-genai-llm-lld/memory-map-genai-lld.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/genai/llm-provider-abstraction/README.md) (full)
- [HLD counterpart](../../../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q05-llm-api-gateway.md)

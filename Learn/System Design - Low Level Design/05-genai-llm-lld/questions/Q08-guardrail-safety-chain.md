# Guardrail / Safety Filter Chain

**Track:** Gen AI LLD  
**Companies:** Anthropic, OpenAI  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-LLD-A08-guardrail-safety-chain.md](../../../Case Studies/lld/genai/CS-LLD-A08-guardrail-safety-chain.md)
> **End-to-end pair:** [Content Moderation for LLM Apps](../../../Case Studies/paired/CS-PAIR-16-content-moderation-llm.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Anthropic Constitutional AI and OpenAI moderation. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design chain of input/output guardrails: PII, toxicity, policy filters.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Guardrail / Safety Filter Chain? | Core entities + 2 primary flows; extensions deferred |
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
- GuardrailChain handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via Guardrail interface at variation points
- Constructor injection for testability
- Swappable pipeline stages behind interfaces
- Explicit boundary to HLD for vector DB, model serving, queues

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Guardrail` | Filter interface |
| `PIIGuardrail` | Redact |
| `ToxicityGuardrail` | Block |
| `GuardrailChain` | Pipeline |
| `SafetyResult` | Pass/fail |

**Nouns → classes:** `Guardrail`, `PIIGuardrail`, `ToxicityGuardrail`, `GuardrailChain`, `SafetyResult`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  GuardrailChain     │──────>│ Chain of Responsibility │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteChain of Responsibility│
│  Guardrail          │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  PIIGuardrail       │────>│  ToxicityGuardrail│
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class GuardrailChain {
        +void create(Guardrail entity)
        +Optional<Guardrail> getById(String id)
        +List<Guardrail> listAll()
        +void delete(String id)
    }
    class Guardrail {
        <<interface>>
        +filter(String) SafetyResult
    }
    class PIIGuardrail {
        +execute() void
    }
    class ToxicityGuardrail {
        +execute() void
    }
    class SafetyResult {
        +execute() void
    }
    GuardrailChain --> Guardrail
```

---

## 6. Public API / Key Methods

```java
public class GuardrailChain {
    public void create(Guardrail entity);
    public Optional<Guardrail> getById(String id);
    public List<Guardrail> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Chain of Responsibility | PII → toxicity → injection filters |

**SOLID:**
- **S:** GuardrailChain orchestrates; entities hold state
- **O:** New behavior via new Guardrail impl
- **D:** Depend on Guardrail interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as GuardrailChain
participant D as Guardrail
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as GuardrailChain
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Chain of Responsibility` implementation plugs in at runtime — no change to `GuardrailChain`."
>
> "Add new `Guardrail` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Chain of Responsibility | Chain of Responsibility — 2+ behaviors |
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

> "I'll design Guardrail / Safety Filter Chain — clarify in-memory scope and MVP flows first."
>
> "Entities: `Guardrail`, `PIIGuardrail`, `ToxicityGuardrail`, `GuardrailChain`, `SafetyResult`. Domain structure separate from `GuardrailChain` orchestration."
>
> "Problem: Design chain of input/output guardrails: PII, toxicity, policy filters."
>
> "`Guardrail` — filter interface; owns its own invariants."
>
> "`PIIGuardrail` — redact; owns its own invariants."
>
> "`ToxicityGuardrail` — block; owns its own invariants."
>
> "`GuardrailChain` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Chain of Responsibility` in isolation?
2. How would you extend Guardrail / Safety Filter Chain without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Gen AI LLD memory map](../../05-genai-llm-lld/memory-map-genai-lld.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/genai/guardrail-safety-chain/README.md) (full)
- [HLD counterpart](../../../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q15-content-moderation-llm.md)

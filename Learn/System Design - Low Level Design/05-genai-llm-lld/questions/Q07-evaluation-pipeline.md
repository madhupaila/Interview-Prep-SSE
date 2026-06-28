# Evaluation Pipeline

**Track:** Gen AI LLD  
**Companies:** OpenAI, HuggingFace  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-LLD-A07-evaluation-pipeline.md](../../../Case Studies/lld/genai/CS-LLD-A07-evaluation-pipeline.md)
> **End-to-end pair:** [LLM Evaluation Platform](../../../Case Studies/paired/CS-PAIR-15-llm-evaluation.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after OpenAI evals and HuggingFace Evaluate. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design LLM eval pipeline: dataset, metrics, judge model, report.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Evaluation Pipeline? | Core entities + 2 primary flows; extensions deferred |
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
- EvalPipeline handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via Metric interface at variation points
- Constructor injection for testability
- Swappable pipeline stages behind interfaces
- Explicit boundary to HLD for vector DB, model serving, queues

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `EvalPipeline` | Runner |
| `EvalCase` | Input/expected |
| `Metric` | Score |
| `JudgeModel` | LLM grader |
| `EvalReport` | Results |

**Nouns → classes:** `EvalPipeline`, `EvalCase`, `Metric`, `JudgeModel`, `EvalReport`  
**Verbs → methods:** `submit()`, `runTests()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  EvalPipeline       │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  EvalPipeline       │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  EvalCase           │────>│  Metric          │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class EvalPipeline {
        +Verdict submit(Submission submission)
        +List<TestResult> runTests(Submission submission)
    }
    class EvalCase {
        +execute() void
    }
    class Metric {
        +execute() void
    }
    class JudgeModel {
        +execute() void
    }
    class EvalReport {
        +execute() void
    }
```

---

## 6. Public API / Key Methods

```java
public class EvalPipeline {
    public Verdict submit(Submission submission);
    public List<TestResult> runTests(Submission submission);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable pipeline components |
| Chain of Responsibility | Sequential processing stages |

**SOLID:**
- **S:** EvalPipeline orchestrates; entities hold state
- **O:** New behavior via new Metric impl
- **D:** Depend on Metric interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as EvalPipeline
participant D as EvalPipeline
U->>S: submit()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as EvalPipeline
U->>S: submit(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `EvalPipeline`."
>
> "Add new `EvalPipeline` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Evaluation Pipeline — clarify in-memory scope and MVP flows first."
>
> "Entities: `EvalPipeline`, `EvalCase`, `Metric`, `JudgeModel`, `EvalReport`. Domain structure separate from `EvalPipeline` orchestration."
>
> "Problem: Design LLM eval pipeline: dataset, metrics, judge model, report."
>
> "`EvalPipeline` — runner; owns its own invariants."
>
> "`EvalCase` — input/expected; owns its own invariants."
>
> "`Metric` — score; owns its own invariants."
>
> "`EvalPipeline` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Evaluation Pipeline without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Gen AI LLD memory map](../../05-genai-llm-lld/memory-map-genai-lld.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/genai/evaluation-pipeline/README.md) (skeleton)
- [HLD counterpart](../../../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q14-llm-evaluation-platform.md)

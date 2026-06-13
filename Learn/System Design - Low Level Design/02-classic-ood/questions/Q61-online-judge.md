# Online Judge

**Track:** Classic OOD  
**Companies:** LeetCode, HackerRank  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-LLD-O61-online-judge.md](../../../Case Studies/lld/classic-ood/CS-LLD-O61-online-judge.md)
> **End-to-end pair:** [Online Judge (LeetCode)](../../../Case Studies/paired/CS-PAIR-14-online-judge.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after LeetCode — submit, compile, run, verdict. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design code judge: submit solution, compile, run tests, verdict.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Online Judge? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design code judge? | Include in MVP — Design code judge |
| 5 | Requirement: submit solution? | Include in MVP — submit solution |
| 6 | Requirement: compile? | Include in MVP — compile |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- JudgeService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via TestRunner interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Submission` | Code + problem |
| `Problem` | Test cases |
| `TestCase` | Input/expected |
| `Verdict` | AC/WA/TLE |
| `Sandbox` | Isolated runner |

**Nouns → classes:** `Submission`, `Problem`, `TestCase`, `Verdict`, `Sandbox`  
**Verbs → methods:** `submit()`, `runTests()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  JudgeService       │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Submission         │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Problem            │────>│  TestCase        │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class JudgeService {
        +Verdict submit(Submission submission)
        +List<TestResult> runTests(Submission submission)
    }
    class Submission {
        +execute() void
    }
    class Problem {
        +execute() void
    }
    class TestCase {
        +execute() void
    }
    class Verdict {
        +execute() void
    }
    class Sandbox {
        +execute() void
    }
    JudgeService --> Submission
```

---

## 6. Public API / Key Methods

```java
public class JudgeService {
    public Verdict submit(Submission submission);
    public List<TestResult> runTests(Submission submission);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in Online Judge |

**SOLID:**
- **S:** JudgeService orchestrates; entities hold state
- **O:** New behavior via new TestRunner impl
- **D:** Depend on TestRunner interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as JudgeService
participant D as Submission
U->>S: submit()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as JudgeService
U->>S: submit(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `JudgeService`."
>
> "Add new `Submission` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Online Judge — clarify in-memory scope and MVP flows first."
>
> "Entities: `Submission`, `Problem`, `TestCase`, `Verdict`, `Sandbox`. Domain structure separate from `JudgeService` orchestration."
>
> "Problem: Design code judge: submit solution, compile, run tests, verdict."
>
> "`Submission` — code + problem; owns its own invariants."
>
> "`Problem` — test cases; owns its own invariants."
>
> "`TestCase` — input/expected; owns its own invariants."
>
> "`JudgeService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Online Judge without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/online-judge/) (skeleton)

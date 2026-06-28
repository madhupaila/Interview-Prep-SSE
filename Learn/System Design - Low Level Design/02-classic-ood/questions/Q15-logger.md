# Logger / Log Aggregator

**Track:** Classic OOD  
**Companies:** Splunk, Datadog, Amazon  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O15-logger.md](../../../Case Studies/lld/classic-ood/CS-LLD-O15-logger.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Logger / Log Aggregator domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design leveled logger with multiple appenders (console, file) and formatting.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Logger / Log Aggregator? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design leveled logger with multiple appe? | Include in MVP — Design leveled logger with multiple appenders (con |
| 5 | Requirement: file) and formatting.? | Include in MVP — file) and formatting. |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Logger handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via LogAppender interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Logger` | Facade |
| `LogLevel` | DEBUG..ERROR |
| `LogAppender` | Output sink |
| `ConsoleAppender` | Stdout |
| `FileAppender` | Disk |
| `Formatter` | Pattern layout |

**Nouns → classes:** `Logger`, `LogLevel`, `LogAppender`, `ConsoleAppender`, `FileAppender`, `Formatter`  
**Verbs → methods:** `log()`, `addAppender()`, `setLevel()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  Logger             │──────>│ Chain of Responsibility │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteChain of Responsibility│
│  Logger             │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  LogLevel           │────>│  LogAppender     │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class Logger {
        +void log(LogLevel level, String message)
        +void addAppender(LogAppender appender)
        +void setLevel(LogLevel minLevel)
    }
    class LogLevel {
        +execute() void
    }
    class LogAppender {
        <<interface>>
        +append(LogMessage) void
    }
    class ConsoleAppender {
        +execute() void
    }
    class FileAppender {
        +execute() void
    }
    class Formatter {
        +execute() void
    }
```

---

## 6. Public API / Key Methods

```java
public class Logger {
    public void log(LogLevel level, String message);
    public void addAppender(LogAppender appender);
    public void setLevel(LogLevel minLevel);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Chain of Responsibility | Log level filtering |
| Observer | Multiple appenders |

**SOLID:**
- **S:** Logger orchestrates; entities hold state
- **O:** New behavior via new LogAppender impl
- **D:** Depend on LogAppender interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as Logger
participant D as Logger
U->>S: log()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as Logger
U->>S: log(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New appender: implement LogAppender — file, syslog, remote without changing Logger."
>
> "Custom formatter: pluggable Formatter per appender."

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

> "I'll design Logger / Log Aggregator — clarify in-memory scope and MVP flows first."
>
> "Entities: `Logger`, `LogLevel`, `LogAppender`, `ConsoleAppender`, `FileAppender`, `Formatter`. Domain structure separate from `Logger` orchestration."
>
> "Problem: Design leveled logger with multiple appenders (console, file) and formatting."
>
> "`Logger` — facade; owns its own invariants."
>
> "`LogLevel` — debug..error; owns its own invariants."
>
> "`LogAppender` — output sink; owns its own invariants."
>
> "`Logger` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Chain of Responsibility` in isolation?
2. How would you extend Logger / Log Aggregator without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/logger/Demo.java) (full)

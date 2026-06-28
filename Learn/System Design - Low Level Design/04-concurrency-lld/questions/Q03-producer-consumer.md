# Producer-Consumer

**Track:** Concurrency LLD  
**Companies:** Amazon, Oracle  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-X03-producer-consumer.md](../../../Case Studies/lld/concurrency/CS-LLD-X03-producer-consumer.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Kafka consumer groups pattern. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design producer-consumer with shared bounded buffer and wait/notify.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Producer-Consumer? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Lock vs synchronized? | Justify choice |
| 5 | Deadlock prevention? | Ordering or timeout |
| 6 | Fairness? | Document starvation risk |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Deliver notifications via configured channels

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via SharedBuffer interface at variation points
- Constructor injection for testability
- Correctness under concurrent access — no data races
- Avoid deadlock — consistent lock ordering where multiple locks

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Producer` | Adds items |
| `Consumer` | Removes items |
| `SharedBuffer` | Bounded queue |
| `Coordinator` | Start/stop |

**Nouns → classes:** `Producer`, `Consumer`, `SharedBuffer`, `Coordinator`  
**Verbs → methods:** `produce()`, `consume()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ProducerConsumer   │──────>│ Producer-Consumer │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteProducer-Consumer│
│  Producer           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Consumer           │────>│  SharedBuffer    │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ProducerConsumer {
        +void produce(T item)
        +T consume()
    }
    class Producer {
        +execute() void
    }
    class Consumer {
        +execute() void
    }
    class SharedBuffer {
        +enqueue() void
        +dequeue() Object
    }
    class Coordinator {
        +execute() void
    }
    ProducerConsumer --> Producer
```

---

## 6. Public API / Key Methods

```java
public class ProducerConsumer {
    public void produce(T item);
    public T consume();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Producer-Consumer | BlockingQueue between threads |

**SOLID:**
- **S:** ProducerConsumer orchestrates; entities hold state
- **O:** New behavior via new SharedBuffer impl
- **D:** Depend on SharedBuffer interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant Prod as Producer
participant Q as BlockingQueue
participant Cons as Consumer
Prod->>Q: put(item)
Q->>Cons: take()
Cons-->>Cons: process(item)
```

**Failure path:**

```mermaid
sequenceDiagram
Prod->>Q: put(item)
Note over Q: queue full — producer blocks
Cons->>Q: take()
Q-->>Prod: notify
```

---

## 9. Extensibility

> "New `Producer-Consumer` implementation plugs in at runtime — no change to `ProducerConsumer`."
>
> "Add new `Producer` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Producer-Consumer | Producer-Consumer — 2+ behaviors |
| State | enum | State pattern | enum for simple lifecycles |
| Storage | in-memory | Repository | in-memory MVP |
| API return | primitive | domain object | domain object — type safety |

---

## 11. Concurrency & Edge Cases

- BlockingQueue: wait/notify when full or empty
- Multiple producers/consumers — queue is shared synchronized structure
- Poison pill pattern to shut down consumers gracefully
- Spurious wakeup handled by while loop on condition

---

## 12. Interview Answer Script (15 min)

> "I'll design Producer-Consumer — clarify in-memory scope and MVP flows first."
>
> "Entities: `Producer`, `Consumer`, `SharedBuffer`, `Coordinator`. Domain structure separate from `ProducerConsumer` orchestration."
>
> "Problem: Design producer-consumer with shared bounded buffer and wait/notify."
>
> "`Producer` — adds items; owns its own invariants."
>
> "`Consumer` — removes items; owns its own invariants."
>
> "`SharedBuffer` — bounded queue; owns its own invariants."
>
> "`ProducerConsumer` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Producer-Consumer` in isolation?
2. How would you extend Producer-Consumer without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Concurrency LLD track](../../04-concurrency-lld/README.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/concurrency/producer-consumer/BoundedBlockingQueue.java) (full)

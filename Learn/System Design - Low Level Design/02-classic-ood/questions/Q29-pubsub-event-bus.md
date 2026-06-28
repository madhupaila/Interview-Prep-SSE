# Pub/Sub Event Bus

**Track:** Classic OOD  
**Companies:** Amazon, Google, Kafka  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O29-pubsub-event-bus.md](../../../Case Studies/lld/classic-ood/CS-LLD-O29-pubsub-event-bus.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Pub/Sub Event Bus domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design in-process pub/sub: topics, subscribers, async delivery.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Pub/Sub Event Bus? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design in-process pub/sub? | Include in MVP — Design in-process pub/sub |
| 5 | Requirement: topics? | Include in MVP — topics |
| 6 | Requirement: subscribers? | Include in MVP — subscribers |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- EventBus handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via EventHandler interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `EventBus` | Broker |
| `Topic` | Channel name |
| `Event` | Payload |
| `Subscriber` | Listener |
| `Subscription` | Topic binding |

**Nouns → classes:** `EventBus`, `Topic`, `Event`, `Subscriber`, `Subscription`  
**Verbs → methods:** `subscribe()`, `unsubscribe()`, `publish()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  EventBus           │──────>│ Observer         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteObserver │
│  EventBus           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Topic              │────>│  Event           │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class EventBus {
        +void subscribe(String topic, Subscriber subscriber)
        +void unsubscribe(String topic, Subscriber subscriber)
        +void publish(String topic, Event event)
    }
    class Topic {
        +execute() void
    }
    class Event {
        +execute() void
    }
    class Subscriber {
        +execute() void
    }
    class Subscription {
        +execute() void
    }
```

---

## 6. Public API / Key Methods

```java
public class EventBus {
    public void subscribe(String topic, Subscriber subscriber);
    public void unsubscribe(String topic, Subscriber subscriber);
    public void publish(String topic, Event event);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Observer | Topic subscribers |
| Mediator | EventBus decoupling |

**SOLID:**
- **S:** EventBus orchestrates; entities hold state
- **O:** New behavior via new EventHandler impl
- **D:** Depend on EventHandler interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant P as Publisher
participant B as EventBus
participant Sub as Subscriber
P->>B: publish(order.created, event)
B->>Sub: onEvent(event)
Sub-->>B: ack
```

**Failure path:**

```mermaid
sequenceDiagram
P->>B: publish(unknown, event)
B-->>P: no subscribers — optional log
```

---

## 9. Extensibility

> "New `Observer` implementation plugs in at runtime — no change to `EventBus`."
>
> "Add new `EventBus` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Observer | Observer — 2+ behaviors |
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

> "I'll design Pub/Sub Event Bus — clarify in-memory scope and MVP flows first."
>
> "Entities: `EventBus`, `Topic`, `Event`, `Subscriber`, `Subscription`. Domain structure separate from `EventBus` orchestration."
>
> "Problem: Design in-process pub/sub: topics, subscribers, async delivery."
>
> "`EventBus` — broker; owns its own invariants."
>
> "`Topic` — channel name; owns its own invariants."
>
> "`Event` — payload; owns its own invariants."
>
> "`EventBus` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Observer` in isolation?
2. How would you extend Pub/Sub Event Bus without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/pubsub-event-bus/README.md) (full)

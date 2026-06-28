# Conversation Memory Manager

**Track:** Gen AI LLD  
**Companies:** Character.AI, OpenAI  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-A04-conversation-memory-manager.md](../../../Case Studies/lld/genai/CS-LLD-A04-conversation-memory-manager.md)
> **End-to-end pair:** [ChatGPT-like Conversational AI](../../../Case Studies/paired/CS-PAIR-03-chatgpt-conversational-ai.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after ChatGPT conversation history and summarization. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design sliding-window + summary memory for multi-turn chat context.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Conversation Memory Manager? | Core entities + 2 primary flows; extensions deferred |
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
- MemoryManager handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via MemoryBuffer interface at variation points
- Constructor injection for testability
- Swappable pipeline stages behind interfaces
- Explicit boundary to HLD for vector DB, model serving, queues

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Conversation` | Session |
| `Message` | Turn |
| `MemoryBuffer` | Window |
| `SummaryCompressor` | Long context |
| `TokenCounter` | Budget |

**Nouns → classes:** `Conversation`, `Message`, `MemoryBuffer`, `SummaryCompressor`, `TokenCounter`  
**Verbs → methods:** `sendMessage()`, `getOrCreate()`, `markRead()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  MemoryManager      │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Conversation       │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Message            │────>│  MemoryBuffer    │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class MemoryManager {
        +Message sendMessage(String conversationId, String text)
        +Conversation getOrCreate(User a, User b)
        +void markRead(String messageId)
    }
    class Conversation {
        -participants: Pair<User>
        -messages: List
    }
    class Message {
        -text: String
        -status: DeliveryStatus
        +markRead() void
    }
    class MemoryBuffer {
        +execute() void
    }
    class SummaryCompressor {
        +execute() void
    }
    class TokenCounter {
        +execute() void
    }
    MemoryManager --> Conversation
```

---

## 6. Public API / Key Methods

```java
public class MemoryManager {
    public Message sendMessage(String conversationId, String text);
    public Conversation getOrCreate(User a, User b);
    public void markRead(String messageId);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable pipeline components |
| Chain of Responsibility | Sequential processing stages |

**SOLID:**
- **S:** MemoryManager orchestrates; entities hold state
- **O:** New behavior via new MemoryBuffer impl
- **D:** Depend on MemoryBuffer interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as MemoryManager
participant D as Conversation
U->>S: sendMessage()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as MemoryManager
U->>S: sendMessage(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `MemoryManager`."
>
> "Add new `Conversation` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Conversation Memory Manager — clarify in-memory scope and MVP flows first."
>
> "Entities: `Conversation`, `Message`, `MemoryBuffer`, `SummaryCompressor`, `TokenCounter`. Domain structure separate from `MemoryManager` orchestration."
>
> "Problem: Design sliding-window + summary memory for multi-turn chat context."
>
> "`Conversation` — session; owns its own invariants."
>
> "`Message` — turn; owns its own invariants."
>
> "`MemoryBuffer` — window; owns its own invariants."
>
> "`MemoryManager` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Conversation Memory Manager without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Gen AI LLD memory map](../../05-genai-llm-lld/memory-map-genai-lld.md)
- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/genai/conversation-memory-manager/README.md) (full)

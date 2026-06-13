# Mediator — Chat Room

**Track:** Design Patterns  
**Companies:** Discord, Slack  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P19-mediator-chat-room.md](../../../Case Studies/lld/design-patterns/CS-LLD-P19-mediator-chat-room.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Mediator — Chat Room domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design mediator so users send messages through chat room, not peer-to-peer.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Mediator — Chat Room? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Overbooking? | No — reject overlapping dates |
| 5 | Cancellation? | Policy-based cancel window |
| 6 | Room types? | Enum RoomType |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Send messages with delivery status tracking

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ChatRoom interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `ChatRoom` | Mediator |
| `User` | Colleague |
| `Message` | Payload |
| `ChatRoomMediator` | Routes messages |

**Nouns → classes:** `ChatRoom`, `User`, `Message`, `ChatRoomMediator`  
**Verbs → methods:** `sendMessage()`, `getOrCreate()`, `markRead()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ChatMediator       │──────>│ Mediator         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteMediator │
│  ChatRoom           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  User               │────>│  Message         │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ChatMediator {
        +Message sendMessage(String conversationId, String text)
        +Conversation getOrCreate(User a, User b)
        +void markRead(String messageId)
    }
    class ChatRoom {
        +execute() void
    }
    class User {
        -id: String
        -name: String
    }
    class Message {
        -text: String
        -status: DeliveryStatus
        +markRead() void
    }
    class ChatRoomMediator {
        +execute() void
    }
    ChatMediator --> ChatRoom
```

---

## 6. Public API / Key Methods

```java
public class ChatMediator {
    public Message sendMessage(String conversationId, String text);
    public Conversation getOrCreate(User a, User b);
    public void markRead(String messageId);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Mediator | Demonstrate Mediator pattern in mediator-chat-room |

**SOLID:**
- **S:** ChatMediator orchestrates; entities hold state
- **O:** New behavior via new ChatRoom impl
- **D:** Depend on ChatRoom interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ChatMediator
participant D as ChatRoom
U->>S: sendMessage()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ChatMediator
U->>S: sendMessage(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Mediator` implementation plugs in at runtime — no change to `ChatMediator`."
>
> "Add new `ChatRoom` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Mediator — Chat Room — clarify in-memory scope and MVP flows first."
>
> "Entities: `ChatRoom`, `User`, `Message`, `ChatRoomMediator`. Domain structure separate from `ChatMediator` orchestration."
>
> "Problem: Design mediator so users send messages through chat room, not peer-to-peer."
>
> "`ChatRoom` — mediator; owns its own invariants."
>
> "`User` — colleague; owns its own invariants."
>
> "`Message` — payload; owns its own invariants."
>
> "`ChatMediator` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Mediator` in isolation?
2. How would you extend Mediator — Chat Room without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/mediator-chat-room/) (full)

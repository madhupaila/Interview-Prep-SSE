# Calendar Application

**Track:** Classic OOD  
**Companies:** Apple, Google, Microsoft  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O27-calendar.md](../../../Case Studies/lld/classic-ood/CS-LLD-O27-calendar.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Calendar Application domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design personal calendar: events, recurring rules, reminders, views.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Calendar Application? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design personal calendar? | Include in MVP — Design personal calendar |
| 5 | Requirement: events? | Include in MVP — events |
| 6 | Requirement: recurring rules? | Include in MVP — recurring rules |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- CalendarService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via RecurrenceRule interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Calendar` | Event container |
| `Event` | Title/time/location |
| `RecurrenceRule` | RRULE pattern |
| `Reminder` | Alert before event |
| `EventView` | Day/week/month |

**Nouns → classes:** `Calendar`, `Event`, `RecurrenceRule`, `Reminder`, `EventView`  
**Verbs → methods:** `checkout()`, `returnItem()`, `reserve()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  CalendarService    │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Calendar           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Event              │────>│  RecurrenceRule  │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class CalendarService {
        +Loan checkout(Member member, String id)
        +void returnItem(String id)
        +void reserve(String isbn)
    }
    class Calendar {
        +execute() void
    }
    class Event {
        +execute() void
    }
    class RecurrenceRule {
        +execute() void
    }
    class Reminder {
        +execute() void
    }
    class EventView {
        +execute() void
    }
    CalendarService --> Calendar
```

---

## 6. Public API / Key Methods

```java
public class CalendarService {
    public Loan checkout(Member member, String id);
    public void returnItem(String id);
    public void reserve(String isbn);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in Calendar Application |

**SOLID:**
- **S:** CalendarService orchestrates; entities hold state
- **O:** New behavior via new RecurrenceRule impl
- **D:** Depend on RecurrenceRule interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CalendarService
participant D as Calendar
U->>S: checkout()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as CalendarService
U->>S: checkout(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `CalendarService`."
>
> "Add new `Calendar` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Calendar Application — clarify in-memory scope and MVP flows first."
>
> "Entities: `Calendar`, `Event`, `RecurrenceRule`, `Reminder`, `EventView`. Domain structure separate from `CalendarService` orchestration."
>
> "Problem: Design personal calendar: events, recurring rules, reminders, views."
>
> "`Calendar` — event container; owns its own invariants."
>
> "`Event` — title/time/location; owns its own invariants."
>
> "`RecurrenceRule` — rrule pattern; owns its own invariants."
>
> "`CalendarService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Calendar Application without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/calendar/) (full)

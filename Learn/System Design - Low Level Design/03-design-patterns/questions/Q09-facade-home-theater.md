# Facade — Home Theater

**Track:** Design Patterns  
**Companies:** Sony, Samsung  
**Difficulty:** Easy  

---

## 1. Problem Statement

Simplify home theater subsystem with single watchMovie() facade.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | Single process or multi-threaded? | In-memory, single JVM; thread-safe if concurrent |
| 2 | Persistence needed? | In-memory for MVP; Repository interface if asked |
| 3 | MVP scope? | Core entities + 2 main flows |
| 4 | Extensibility? | One variation point via Strategy/interface |
| 5 | Error handling? | Domain exceptions, fail fast |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Core operations for facade — home theater
- Validate inputs and enforce business rules
- Support primary user flows end-to-end

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Extensible without modifying core logic (Open-Closed)
- Testable via dependency injection
- **Concurrency:** Single-threaded unless multi-user access specified. Use synchronized on shared mutable state if needed.

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| HomeTheaterFacade | Core domain entity / service |
| Projector | Core domain entity / service |
| Screen | Core domain entity / service |
| Amplifier | Core domain entity / service |
| DVDPlayer | Core domain entity / service |

**Relationships:** Service orchestrates domain entities; Strategy/interface at variation points.

**Nouns → classes:** `HomeTheaterFacade`, `Projector`, `Screen`, `Amplifier`, `DVDPlayer`  
**Verbs → methods:** `watchMovie()` and related operations

---

## 5. Class Diagram

```
┌─────────────────────┐
│  HomeTheaterFacadeService │──────> Strategy / Factory (interface)
│─────────────────────│
│ +watchMovie()  │
└─────────┬───────────┘
          │ uses
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  HomeTheaterFacade     │────>│  Projector  │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class MainService {
        +watchMovie()
    }
    class DomainRoot {
        +execute()
    }
    class Strategy {
        <<interface>>
        +apply()
    }
    MainService --> DomainRoot
    MainService ..> Strategy
```

---

## 6. Public API / Key Methods

```java
public class HomeTheaterFacadeService {
    public Result watchMovie();
    // Additional: validate, lookup, list as needed for Facade — Home Theater
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Facade | Primary variation point for facade — home theater |


**SOLID:**
- **S:** Service orchestrates; entities hold domain state
- **O:** New behavior via new Strategy/impl
- **D:** Depend on interfaces, not concrete classes

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
    participant U as User
    participant S as Service
    participant D as Domain
    U->>S: watchMovie()
    S->>D: validate / process
    D-->>S: result
    S-->>U: success
```

**Failure path:** Invalid input → throw `DomainException` with clear message.

---

## 9. Extensibility

> "To add new behavior, I'd introduce a new implementation of the Strategy interface — e.g. new pricing rule, allocation policy, or payment gateway — without editing `HomeTheaterFacadeService` core loop."

Extension example: add new `DVDPlayer` subclass or enum value + plug new Strategy at runtime.

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| State modeling | enum | State pattern | enum for simple; State for complex transitions |
| Variation | Strategy | if/else | Strategy for 2+ algorithms |
| Storage | in-memory Map | Repository interface | in-memory MVP; Repository if persistence asked |
| API return | domain object | primitive | domain object (type safety) |

---

## 11. Concurrency & Edge Cases


**Concurrency:** Single-threaded unless multi-user access specified. Use synchronized on shared mutable state if needed.

- Null/invalid input → fail fast with domain exception
- Empty collections → handle gracefully
- Duplicate operations → idempotent where applicable (domain check)

---

## 12. Interview Answer Script (15 min)

> "I'll design facade — home theater starting with clarifying scope — in-memory, single process, core flows only."
>
> "Entities I see: `HomeTheaterFacade`, `Projector`, `Screen`, `Amplifier`, `DVDPlayer`. I'll group them into domain structure and a service facade."
>
> "The variation point is Facade — for example different policies or algorithms without changing the orchestration loop."
>
> "Core API: `watchMovie()` — validate first, delegate to domain, return typed result."
>
> "For extensibility, new behavior = new interface implementation. Open-Closed principle."
>
> "Tradeoff: I'd use enum for simple states; State pattern only if transitions have side effects."
>
> "I can sketch the service method in Java — inject dependencies via constructor for testability."
>
> "If we needed millions of users and distributed deployment, I'd pivot to HLD — cache, queue, DB — but object model stays the same."

---

## 13. Follow-Up Questions

1. How would you make this thread-safe?
2. How would you add persistence?
3. How would you unit test the service?
4. What if we need plugin-style extensibility?
5. How does this map to a microservices HLD?

---

## 14. Related Links

- [Facade pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Pattern picker](../../00-interview-framework/04-pattern-picker.md)
- [Java implementation](../../09-code-implementations/java/patterns/facade-home-theater/) (skeleton)


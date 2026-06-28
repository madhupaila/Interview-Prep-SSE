# Proxy — Image Loader

**Track:** Design Patterns  
**Companies:** Google, Meta  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P10-proxy-image-loader.md](../../../Case Studies/lld/design-patterns/CS-LLD-P10-proxy-image-loader.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Proxy — Image Loader domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design virtual proxy lazy-loading high-res images with placeholder.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Proxy — Image Loader? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design virtual proxy lazy-loading high-r? | Include in MVP — Design virtual proxy lazy-loading high-res images  |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- ImageProxy handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via Image interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Image` | Interface |
| `HighResImage` | Real subject |
| `ImageProxy` | Lazy loader |
| `ImageCache` | Memoization |

**Nouns → classes:** `Image`, `HighResImage`, `ImageProxy`, `ImageCache`  
**Verbs → methods:** `create()`, `getById()`, `listAll()`, `delete()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ImageProxy         │──────>│ Proxy            │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteProxy    │
│  Image              │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  HighResImage       │────>│  ImageProxy      │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ImageProxy {
        +void create(Image entity)
        +Optional<Image> getById(String id)
        +List<Image> listAll()
        +void delete(String id)
    }
    class Image {
        <<interface>>
        +apply() void
    }
    class HighResImage {
        +execute() void
    }
    class ImageCache {
        +execute() void
    }
    ImageProxy --> Image
```

---

## 6. Public API / Key Methods

```java
public class ImageProxy {
    public void create(Image entity);
    public Optional<Image> getById(String id);
    public List<Image> listAll();
    public void delete(String id);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Proxy | Demonstrate Proxy pattern in proxy-image-loader |

**SOLID:**
- **S:** ImageProxy orchestrates; entities hold state
- **O:** New behavior via new Image impl
- **D:** Depend on Image interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ImageProxy
participant D as Image
U->>S: create()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as ImageProxy
U->>S: create(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Proxy` implementation plugs in at runtime — no change to `ImageProxy`."
>
> "Add new `Image` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Proxy | Proxy — 2+ behaviors |
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

> "I'll design Proxy — Image Loader — clarify in-memory scope and MVP flows first."
>
> "Entities: `Image`, `HighResImage`, `ImageProxy`, `ImageCache`. Domain structure separate from `ImageProxy` orchestration."
>
> "Problem: Design virtual proxy lazy-loading high-res images with placeholder."
>
> "`Image` — interface; owns its own invariants."
>
> "`HighResImage` — real subject; owns its own invariants."
>
> "`ImageProxy` — lazy loader; owns its own invariants."
>
> "`ImageProxy` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Proxy` in isolation?
2. How would you extend Proxy — Image Loader without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/proxy-image-loader/README.md) (full)

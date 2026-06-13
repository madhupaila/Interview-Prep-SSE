# Iterator — Playlist

**Track:** Design Patterns  
**Companies:** Spotify, Apple  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-P17-iterator-playlist.md](../../../Case Studies/lld/design-patterns/CS-LLD-P17-iterator-playlist.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Iterator — Playlist domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design custom iterator traversing playlist forward/backward/shuffle.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Iterator — Playlist? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design custom iterator traversing playli? | Include in MVP — Design custom iterator traversing playlist forward |
| 5 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 6 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Execute game turns with rule validation

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via Iterator interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Playlist` | Aggregate |
| `Iterator` | Interface |
| `SequentialIterator` | Forward |
| `ShuffleIterator` | Random order |

**Nouns → classes:** `Playlist`, `Iterator`, `SequentialIterator`, `ShuffleIterator`  
**Verbs → methods:** `addSong()`, `shuffle()`, `playNext()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  PlaylistIterator   │──────>│ Iterator         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteIterator │
│  Playlist           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Iterator           │────>│  SequentialIterator│
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class PlaylistIterator {
        +void addSong(String playlistId, String songId)
        +void shuffle(String playlistId)
        +List<Song> playNext()
    }
    class Playlist {
        +addSong(Song) void
        +shuffle() void
    }
    class Iterator {
        <<interface>>
        +apply() void
    }
    class SequentialIterator {
        +execute() void
    }
    class ShuffleIterator {
        +execute() void
    }
    PlaylistIterator --> Playlist
```

---

## 6. Public API / Key Methods

```java
public class PlaylistIterator {
    public void addSong(String playlistId, String songId);
    public void shuffle(String playlistId);
    public List<Song> playNext();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Iterator | Demonstrate Iterator pattern in iterator-playlist |

**SOLID:**
- **S:** PlaylistIterator orchestrates; entities hold state
- **O:** New behavior via new Iterator impl
- **D:** Depend on Iterator interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as PlaylistIterator
participant D as Playlist
U->>S: addSong()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as PlaylistIterator
U->>S: addSong(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Iterator` implementation plugs in at runtime — no change to `PlaylistIterator`."
>
> "Add new `Playlist` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Iterator | Iterator — 2+ behaviors |
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

> "I'll design Iterator — Playlist — clarify in-memory scope and MVP flows first."
>
> "Entities: `Playlist`, `Iterator`, `SequentialIterator`, `ShuffleIterator`. Domain structure separate from `PlaylistIterator` orchestration."
>
> "Problem: Design custom iterator traversing playlist forward/backward/shuffle."
>
> "`Playlist` — aggregate; owns its own invariants."
>
> "`Iterator` — interface; owns its own invariants."
>
> "`SequentialIterator` — forward; owns its own invariants."
>
> "`PlaylistIterator` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Iterator` in isolation?
2. How would you extend Iterator — Playlist without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/patterns/iterator-playlist/) (full)

# Playlist Manager

**Track:** Classic OOD  
**Companies:** Apple Music, Spotify  
**Difficulty:** Medium  

---

## Case Study

> **Full case study:** [CS-LLD-O42-playlist-manager.md](../../../Case Studies/lld/classic-ood/CS-LLD-O42-playlist-manager.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Playlist Manager domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design playlist CRUD, shuffle, repeat, collaborative editing.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Playlist Manager? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design playlist CRUD? | Include in MVP — Design playlist CRUD |
| 5 | Requirement: shuffle? | Include in MVP — shuffle |
| 6 | Requirement: repeat? | Include in MVP — repeat |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Execute game turns with rule validation

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via ShuffleStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Playlist` | Ordered tracks |
| `Song` | Track metadata |
| `User` | Owner |
| `PlaybackQueue` | Current order |
| `ShuffleStrategy` | Random order |

**Nouns → classes:** `Playlist`, `Song`, `User`, `PlaybackQueue`, `ShuffleStrategy`  
**Verbs → methods:** `addSong()`, `shuffle()`, `playNext()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  PlaylistService    │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Playlist           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Song               │────>│  User            │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class PlaylistService {
        +void addSong(String playlistId, String songId)
        +void shuffle(String playlistId)
        +List<Song> playNext()
    }
    class Playlist {
        +addSong(Song) void
        +shuffle() void
    }
    class Song {
        +execute() void
    }
    class User {
        -id: String
        -name: String
    }
    class PlaybackQueue {
        +execute() void
    }
    class ShuffleStrategy {
        <<interface>>
        +apply() void
    }
    PlaylistService --> Playlist
```

---

## 6. Public API / Key Methods

```java
public class PlaylistService {
    public void addSong(String playlistId, String songId);
    public void shuffle(String playlistId);
    public List<Song> playNext();
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Swappable algorithms |
| Queue | FIFO ordering of work items |

**SOLID:**
- **S:** PlaylistService orchestrates; entities hold state
- **O:** New behavior via new ShuffleStrategy impl
- **D:** Depend on ShuffleStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as PlaylistService
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
participant S as PlaylistService
U->>S: addSong(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `PlaylistService`."
>
> "Add new `Playlist` subtypes or enum values for new categories — Open-Closed."

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

> "I'll design Playlist Manager — clarify in-memory scope and MVP flows first."
>
> "Entities: `Playlist`, `Song`, `User`, `PlaybackQueue`, `ShuffleStrategy`. Domain structure separate from `PlaylistService` orchestration."
>
> "Problem: Design playlist CRUD, shuffle, repeat, collaborative editing."
>
> "`Playlist` — ordered tracks; owns its own invariants."
>
> "`Song` — track metadata; owns its own invariants."
>
> "`User` — owner; owns its own invariants."
>
> "`PlaylistService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Playlist Manager without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/playlist-manager/) (full)

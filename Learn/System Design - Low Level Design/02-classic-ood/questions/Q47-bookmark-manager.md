# Bookmark Manager

**Track:** Classic OOD  
**Companies:** Browser, Pinterest  
**Difficulty:** Easy  

---

## Case Study

> **Full case study:** [CS-LLD-O47-bookmark-manager.md](../../../Case Studies/lld/classic-ood/CS-LLD-O47-bookmark-manager.md)
> **Read order:** Case Study → this question → [Java implementation](../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Bookmark Manager domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design bookmarks: folders, tags, URL validation, search.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Bookmark Manager? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Nested folders? | Yes — folder tree |
| 5 | Tags? | Many-to-many on bookmarks |
| 6 | Duplicate URLs? | Reject or merge per policy |
| 7 | Search? | By title and tag |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- Add bookmark with URL validation and folder placement
- Organize bookmarks in nested folder tree (Composite)
- Tag bookmarks for multi-label classification
- Search bookmarks by title, URL, or tag

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via SearchIndex interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Bookmark` | URL + title |
| `Folder` | Hierarchy |
| `Tag` | Label |
| `BookmarkStore` | Persistence |
| `SearchIndex` | Title lookup |

**Nouns → classes:** `Bookmark`, `Folder`, `Tag`, `BookmarkStore`, `SearchIndex`  
**Verbs → methods:** `addBookmark()`, `createFolder()`, `search()`, `addTag()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  BookmarkService    │──────>│ Composite        │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteComposite│
│  Bookmark           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Folder             │────>│  Tag             │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class BookmarkService {
        +Bookmark addBookmark(String url, String title, String folderId)
        +Folder createFolder(String name, String parentId)
        +List<Bookmark> search(String query)
        +void addTag(String bookmarkId, String tag)
    }
    class Bookmark {
        -url: String
        -title: String
        +validateUrl() boolean
    }
    class Folder {
        -name: String
        -children: List
        +addChild(Folder) void
    }
    class Tag {
        -label: String
    }
    class BookmarkStore {
        <<interface>>
        +save(Bookmark) void
    }
    class SearchIndex {
        <<interface>>
        +search(String) List
    }
    BookmarkService --> Bookmark
```

---

## 6. Public API / Key Methods

```java
public class BookmarkService {
    public Bookmark addBookmark(String url, String title, String folderId);
    public Folder createFolder(String name, String parentId);
    public List<Bookmark> search(String query);
    public void addTag(String bookmarkId, String tag);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Composite | Tree structures |
| Repository | Persistence abstraction |

**SOLID:**
- **S:** BookmarkService orchestrates; entities hold state
- **O:** New behavior via new SearchIndex impl
- **D:** Depend on SearchIndex interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as BookmarkService
participant F as Folder
U->>S: addBookmark(url, title, folderId)
S->>S: validateUrl(url)
S->>F: place(bookmark)
S-->>U: Bookmark
```

**Failure path:**

```mermaid
sequenceDiagram
U->>S: addBookmark(invalidUrl)
S-->>U: InvalidUrlException
```

---

## 9. Extensibility

> "New `Composite` implementation plugs in at runtime — no change to `BookmarkService`."
>
> "Add new `Bookmark` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Composite | Composite — 2+ behaviors |
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

> "I'll design Bookmark Manager — clarify in-memory scope and MVP flows first."
>
> "Entities: `Bookmark`, `Folder`, `Tag`, `BookmarkStore`, `SearchIndex`. Domain structure separate from `BookmarkService` orchestration."
>
> "Problem: Design bookmarks: folders, tags, URL validation, search."
>
> "`Bookmark` — url + title; owns its own invariants."
>
> "`Folder` — hierarchy; owns its own invariants."
>
> "`Tag` — label; owns its own invariants."
>
> "`BookmarkService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Composite` in isolation?
2. How would you extend Bookmark Manager without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/bookmark-manager/) (skeleton)

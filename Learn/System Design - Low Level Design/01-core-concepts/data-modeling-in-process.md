# Data Modeling — In-Process

LLD focuses on **in-memory object graphs**. Persistence is optional abstraction.

---

## In-Memory Storage

```java
public class ParkingLot {
    private final List<ParkingFloor> floors = new ArrayList<>();
    private final Map<String, Ticket> activeTickets = new HashMap<>();
}
```

Default for interviews: **no database** unless interviewer asks.

---

## Repository Pattern (When Asked)

```java
public interface TicketRepository {
    void save(Ticket ticket);
    Optional<Ticket> findById(String id);
}

public class InMemoryTicketRepository implements TicketRepository {
    private final Map<String, Ticket> store = new ConcurrentHashMap<>();
    // ...
}
```

> "I'd introduce Repository if we need to swap in-memory for SQL — Dependency Inversion."

---

## ID Generation

| Approach | When |
|----------|------|
| `UUID.randomUUID()` | Generic unique IDs |
| `AtomicLong` increment | Simple ticket numbers |
| Snowflake / external | Mention for HLD scale only |

---

## Relationships in Memory

| Relationship | Java structure |
|--------------|----------------|
| One-to-many | `List<Floor>` in Lot |
| Many-to-many | `Map<User, List<Chat>>` both ways or join entity |
| Lookup by key | `Map<String, Spot>` |

---

## Related

- [LLD vs HLD Boundary](lld-vs-hld-boundary.md)
- [Testing and DI](testing-and-di.md)

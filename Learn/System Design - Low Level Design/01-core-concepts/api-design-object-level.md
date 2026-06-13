# API Design — Object Level

Method signatures and types signal senior judgment in LLD.

---

## Method Signatures

| Good | Avoid |
|------|-------|
| `Ticket park(Vehicle vehicle)` | `String park(String type, String plate)` |
| `void unpark(Ticket ticket)` | `void unpark(int id)` |
| `boolean isFull(VehicleType type)` | `int check()` |

Use domain types, not primitives, for core concepts.

---

## Enums vs Class Hierarchy

| Use enum | Use class hierarchy |
|----------|---------------------|
| Fixed set known at compile time | Behavior differs significantly per type |
| `VehicleType { CAR, TRUCK }` | Chess pieces with different move logic |
| `OrderStatus { PENDING, SHIPPED }` | Payment types with different settle flows |

**Hybrid:** enum for type + Strategy for behavior variation.

---

## Exceptions

```java
public class LotFullException extends RuntimeException { }
public class InvalidTicketException extends RuntimeException { }
```

| Checked vs unchecked | LLD pick |
|---------------------|----------|
| Unchecked (runtime) | Default for domain errors in interviews |
| Checked | Rarely — mention if API boundary |

---

## Optional and Null Safety

```java
public Optional<ParkingSpot> findSpot(Vehicle v);
```

> "Return Optional when spot may not exist — avoid null returns."

---

## Immutability

Value objects: `Money`, `Coordinates`, `Ticket` (after issue).

```java
public final class Ticket {
    private final String id;
    private final Instant issuedAt;
    // no setters
}
```

---

## Related

- [Data Modeling In-Process](data-modeling-in-process.md)
- [Common Anti-Patterns](common-anti-patterns.md)

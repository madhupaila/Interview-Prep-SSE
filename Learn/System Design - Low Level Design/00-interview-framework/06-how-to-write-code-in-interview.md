# How to Write Code in the Interview — Java

You typically have **8–12 minutes** to sketch code. Focus on structure and one happy path.

---

## What to Implement vs Pseudo-Code

| Implement (real Java) | Pseudo-code / skip |
|----------------------|-------------------|
| Core service method (park, move, placeOrder) | All getters/setters |
| Key interface + one impl | Full test class |
| Enums for types/states | Main method (unless asked) |
| One edge case check | Database / HTTP / file I/O |
| Domain exception throw | Logging infrastructure |

---

## Package Structure

```
com.lldprep.classic.parkinglot
├── model/          ParkingLot, ParkingSpot, Vehicle, Ticket
├── enums/          VehicleType, SpotType
├── strategy/       ParkingStrategy, NearestFirstStrategy
├── service/        ParkingLotService
├── exception/      LotFullException
└── ParkingLotDemo.java   (optional)
```

---

## Timeboxing (10 min)

| Minute | Task |
|--------|------|
| 0–2 | Enums + 2–3 entity class shells |
| 2–5 | Interface + service class with constructor injection |
| 5–9 | Implement ONE core method with edge case |
| 9–10 | Mention what you'd add with more time |

---

## Java Conventions for LLD

```java
// Prefer interfaces at variation points
public interface ParkingStrategy {
    Optional<ParkingSpot> findSpot(Vehicle vehicle, List<ParkingSpot> spots);
}

// Constructor injection
public class ParkingLotService {
    private final ParkingLot lot;
    private final ParkingStrategy strategy;

    public ParkingLotService(ParkingLot lot, ParkingStrategy strategy) {
        this.lot = lot;
        this.strategy = strategy;
    }
}

// Enum for fixed types
public enum VehicleType { CAR, MOTORCYCLE, TRUCK }

// Domain exception
public class LotFullException extends RuntimeException {
    public LotFullException(String message) { super(message); }
}
```

---

## Thread-Safe Sketch

```java
public synchronized Ticket park(Vehicle vehicle) {
    // OR: lock per floor / per spot for finer granularity
}

// OR
private final Map<String, ParkingSpot> spots = new ConcurrentHashMap<>();
```

Narrate **why** you chose synchronized vs concurrent collection.

---

## Narrate While Coding

> "I'm injecting ParkingStrategy for Open-Closed… park() first finds a spot via strategy, then assigns vehicle, then issues ticket… if no spot, throw LotFullException."

---

## Common Interviewer Follow-Ups

| Question | Response |
|----------|----------|
| "Add electric spots" | New `SpotType.ELECTRIC`, optional `ChargingCapable` interface |
| "Make thread-safe" | `synchronized park()` or lock per spot |
| "Add tests" | Mock strategy, verify park assigns correct spot |
| "Persist to DB" | Introduce `ParkingLotRepository` interface — out of MVP scope |

---

## Related

- [Java Implementations](../09-code-implementations/README.md)
- [Concurrency Fundamentals](../01-core-concepts/concurrency-fundamentals.md)
- [API Design Object Level](../01-core-concepts/api-design-object-level.md)

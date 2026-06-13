# OOP Pillars — LLD Interview Guide

The four pillars of OOP drive every LLD diagram. Senior candidates explain **when** to use each, not just definitions.

---

## Encapsulation

**Hide internal state; expose behavior through methods.**

```java
public class ParkingSpot {
    private Vehicle vehicle;  // hidden

    public boolean isAvailable() { return vehicle == null; }
    public void assign(Vehicle v) {
        if (!isAvailable()) throw new IllegalStateException("Occupied");
        this.vehicle = v;
    }
}
```

**Interview line:** "Spot encapsulates occupancy — callers can't set vehicle directly."

---

## Abstraction

**Show essential behavior; hide implementation.**

- Interfaces: `ParkingStrategy`, `PaymentProcessor`
- Abstract classes: `Vehicle` with common fields, abstract `getRequiredSpotType()`

**Interview line:** "Service depends on ParkingStrategy abstraction, not NearestFirst concrete class."

---

## Inheritance (IS-A)

**Use only for true subtype relationships.**

| Good IS-A | Bad IS-A |
|-----------|----------|
| `Sedan extends Vehicle` | `ParkingLot extends Building` |
| `Knight extends ChessPiece` | `Order extends List` |

**Prefer composition:** ParkingLot **has** floors, not **is** a floor.

---

## Polymorphism

**Same interface, different behavior.**

```java
ParkingStrategy strategy = new NearestFirstStrategy();
// swap to new CheapestFirstStrategy() without changing service
Optional<Spot> spot = strategy.findSpot(vehicle, spots);
```

Chess: each `ChessPiece` implements `move()` differently.

---

## Composition Over Inheritance

| Inheritance | Composition |
|-------------|-------------|
| Tight coupling | Flexible |
| Fragile base class | Change behavior by swapping parts |
| Deep hierarchies | Shallow, clear graphs |

> "I'll compose ParkingLot with floors and inject ParkingStrategy rather than subclassing SpecialParkingLot."

---

## Related

- [SOLID Principles](solid-principles.md)
- [API Design Object Level](api-design-object-level.md)

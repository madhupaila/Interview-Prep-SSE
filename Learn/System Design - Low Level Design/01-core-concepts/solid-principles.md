# SOLID Principles — LLD Examples

Each principle with a **violation** and **fix** you can cite in interviews.

---

## S — Single Responsibility

**One class, one reason to change.**

| Violation | Fix |
|-----------|-----|
| `ParkingLot` handles parking + payment + receipt printing | `ParkingLotService`, `PaymentService`, `ReceiptPrinter` |

> "Payment changes shouldn't require editing spot allocation logic."

---

## O — Open/Closed

**Open for extension, closed for modification.**

| Violation | Fix |
|-----------|-----|
| `if (type == "electric")` scattered in park() | `SpotType` enum + `ChargingCapable` interface; new types without editing park loop |

> "New allocation algorithm = new Strategy class, not editing ParkingLotService."

---

## L — Liskov Substitution

**Subtypes must work wherever parent is expected.**

| Violation | Fix |
|-----------|-----|
| `Truck.park()` throws on motorcycle spots when called as `Vehicle` | Override `getRequiredSpotType()`; service respects it |

> "Any Vehicle passed to park() must honor the contract — no surprise exceptions."

---

## I — Interface Segregation

**Clients shouldn't depend on methods they don't use.**

| Violation | Fix |
|-----------|-----|
| `IVehicle` with `fly()`, `drive()`, `sail()` | `Drivable`, `Flyable` — small interfaces |

> "Motorcycle only implements Drivable — not empty fly() method."

---

## D — Dependency Inversion

**Depend on abstractions, not concretions.**

| Violation | Fix |
|-----------|-----|
| `new NearestFirstStrategy()` inside ParkingLotService | Constructor: `ParkingLotService(lot, strategy)` |

> "High-level service doesn't know which strategy — injected at runtime or test."

---

## SOLID in One Diagram

```
ParkingLotService  ──depends on──>  ParkingStrategy (interface)
        │                                    ▲
        │ uses                               │ implements
        ▼                                    │
   ParkingLot                          NearestFirstStrategy
```

---

## Related

- [Senior SWE Signals](../00-interview-framework/05-senior-swe-signals.md)
- [Testing and DI](testing-and-di.md)

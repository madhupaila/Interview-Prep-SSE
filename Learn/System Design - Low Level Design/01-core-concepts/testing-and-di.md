# Testing & Dependency Injection — LLD

Design for testability even if you don't write tests in the interview.

---

## Constructor Injection

```java
public class ParkingLotService {
    public ParkingLotService(ParkingLot lot, ParkingStrategy strategy) {
        this.lot = lot;
        this.strategy = strategy;
    }
}
```

Enables: `new ParkingLotService(mockLot, mockStrategy)` in tests.

---

## Interface Seams

| Dependency | Interface |
|------------|-----------|
| Payment | `PaymentProcessor` |
| Persistence | `TicketRepository` |
| Time | `Clock` (for testing expiry) |
| Random | `RandomProvider` (for games) |

---

## What to Unit Test

- Strategy algorithms in isolation
- Domain rules (chess move validity, split logic)
- State transitions (vending machine)

---

## Interview Line

> "I'd unit test NearestFirstStrategy with a fixed list of spots — no need for full ParkingLot."

---

## Related

- [SOLID Principles](solid-principles.md)
- [Senior SWE Signals](../00-interview-framework/05-senior-swe-signals.md)

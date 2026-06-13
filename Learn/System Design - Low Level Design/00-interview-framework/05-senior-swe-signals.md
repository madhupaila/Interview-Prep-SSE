# Senior SWE Signals — LLD Round

Interviewers at Senior level look for **design judgment**, not just correct diagrams.

---

## What Separates Senior from Mid-Level

| Mid-Level | Senior |
|-----------|--------|
| Lists classes | Groups into clusters with clear boundaries |
| One big class | Service + domain entities + interfaces |
| "I'd use a database" | In-memory + Repository interface if persistence needed |
| Names one pattern | Names pattern + SOLID principle + tradeoff |
| Waits for "make it extensible" | Proactively shows extension points |
| Ignores concurrency | Calls out thread safety when relevant |
| Draws silently | Narrates relationships while drawing |

---

## SOLID — Say Aloud

| Principle | LLD phrase |
|-----------|--------------|
| **S** Single Responsibility | "PaymentService only handles payment — not spot allocation." |
| **O** Open/Closed | "New vehicle type = new enum value + maybe new Spot rule — no edit to core park loop." |
| **L** Liskov Substitution | "Any Vehicle subtype works in park() — motorcycle doesn't break truck logic." |
| **I** Interface Segregation | "Small interfaces: Parkable, Payable — not one giant IVehicle." |
| **D** Dependency Inversion | "ParkingLotService depends on ParkingStrategy interface, injected at construction." |

---

## Composition Over Inheritance

> "ParkingLot HAS floors and spots — I won't make ParkingLot extend Building. Inheritance only for true IS-A: Sedan extends Vehicle."

---

## Testability Seams

- Constructor injection for strategies and repositories
- Interfaces for external dependencies (payment, notification)
- Pure domain logic in entities (easy unit test)

> "I'd unit test NearestFirstStrategy in isolation by passing a mock list of spots."

---

## Thread Safety Callouts

When multi-threaded or concurrent access:

| Scenario | Approach |
|----------|----------|
| Shared mutable map | `ConcurrentHashMap` or synchronized |
| Check-then-act | Synchronize whole block or use atomic ops |
| Read-heavy, rare write | `ReadWriteLock` |
| Producer-consumer | `BlockingQueue` |
| Rate limiter | `synchronized` on token refill or atomic counters |

> "park() is check-then-act on spot availability — I'll synchronize on the spot or use compare-and-set."

---

## API Design Signals

- Return meaningful types (`Ticket`, `Optional<Spot>`) not raw strings
- Use enums for fixed sets (`OrderStatus`, `VehicleType`)
- Fail fast with domain exceptions (`LotFullException`, `InvalidTicketException`)
- Immutable value objects where possible (`Money`, `Coordinates`)

---

## Anti-Patterns to Avoid

| Anti-pattern | Senior fix |
|--------------|------------|
| God class | Split service / entity / strategy |
| Anemic domain (all logic in service) | Put behavior on entities when natural |
| Premature microservices | Stay in-process for LLD |
| Over-engineering | 4–8 classes for MVP, interfaces at 1–2 points |
| Pattern soup | Max 2–3 patterns, each justified |

---

## Closing Strong

End with:
1. One extensibility example answered
2. One tradeoff with explicit pick
3. Offer to code core method or deep-dive a follow-up

---

## Related

- [SOLID Principles](../01-core-concepts/solid-principles.md)
- [Common Anti-Patterns](../01-core-concepts/common-anti-patterns.md)
- [Testing and DI](../01-core-concepts/testing-and-di.md)

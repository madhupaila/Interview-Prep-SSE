# LLD Round Flow — 45–60 Minute Timeline

Senior LLD interviews follow a predictable rhythm. Owning the structure signals seniority.

---

## The 8-Step Flow

```
1. Clarify (5 min) → 2. Scope MVP (2 min) → 3. Identify entities (3 min)
→ 4. Class diagram (10 min) → 5. Public APIs (5 min) → 6. Patterns (5 min)
→ 7. Extensibility (3 min) → 8. Code sketch (10 min)
```

```mermaid
flowchart LR
  A[ClarifyReqs] --> B[ScopeMVP]
  B --> C[IdentifyEntities]
  C --> D[ClassDiagram]
  D --> E[PublicAPIs]
  E --> F[PatternsAndSOLID]
  F --> G[Extensibility]
  G --> H[CodeSketch]
```

---

## Step 1: Clarify Requirements (5 min)

**What to ask:**

| Category | Example questions |
|----------|-------------------|
| Users | Who operates the system? Single user or multi-user? |
| Scale | Single process or multi-threaded? Concurrent access? |
| Persistence | In-memory only or need database abstraction? |
| Scope | MVP features vs nice-to-have extensions? |
| Rules | Business rules fixed or configurable? |
| Errors | What happens on invalid input / full capacity? |

**Senior move:** Summarize back:
> "So we're designing an in-memory parking lot for a single building, multi-threaded entry/exit, no payment integration in MVP. Is that right?"

**Do NOT** start drawing until scope is aligned.

---

## Step 2: Scope MVP (2 min)

Explicitly bound the design:

> "For this round I'll model core entities, park/exit flows, and spot allocation. I'll mention electric charging and pricing as extensions but won't deep-dive unless you want to."

This prevents scope creep and shows prioritization.

---

## Step 3: Identify Entities (3 min)

**Noun → Class, Verb → Method:**

| Noun (entity) | Verb (operation) |
|---------------|------------------|
| ParkingLot | park, unpark |
| Vehicle | (data: type, plate) |
| ParkingSpot | isAvailable, assign |
| Ticket | issue, validate |

**Senior move:** Group into 2–4 clusters:
- **Structure:** Lot, Floor, Spot
- **Actors:** Vehicle, User (optional)
- **Workflow:** Ticket, PaymentService
- **Variation:** ParkingStrategy (interface)

---

## Step 4: Class Diagram (10 min)

Draw in this order:
1. Core entities (4–6 classes)
2. Enums for fixed types (`VehicleType`, `SpotType`)
3. Interfaces at variation points (`ParkingStrategy`, `PaymentProcessor`)
4. Service/facade class that orchestrates (`ParkingLotService`)
5. Relationships: composition (Lot has Floors), association (Spot holds Vehicle)

See [How to Draw Class Diagrams](02-how-to-draw-class-diagrams.md).

---

## Step 5: Public APIs (5 min)

Write 5–8 method signatures the interviewer cares about:

```java
public class ParkingLot {
    public Ticket park(Vehicle vehicle);
    public void unpark(Ticket ticket);
    public boolean isFull(VehicleType type);
}
```

Focus on **behavior**, not getters/setters.

---

## Step 6: Patterns & SOLID (5 min)

Name 1–3 patterns with **why**:

| Pattern | When to mention |
|---------|-----------------|
| Strategy | Multiple algorithms (spot allocation, pricing, payment) |
| Factory | Creating vehicles, game pieces, documents |
| State | Complex lifecycle (order, elevator, vending machine) |
| Observer | Event notifications (stock price, logger subscribers) |
| Command | Undo/redo operations |

**SOLID aloud:**
- **S:** ParkingLot orchestrates; PaymentService handles payment only
- **O:** New spot type via enum + interface, not editing core logic
- **L:** All Vehicle subtypes work with `park(Vehicle)`
- **I:** Small interfaces (`Parkable`, `Payable`) not fat ones
- **D:** Depend on `ParkingStrategy` interface, not concrete impl

---

## Step 7: Extensibility (3 min)

Answer proactively:

> "To add electric charging spots, I'd add `ChargingCapable` interface and `ElectricSpot` class. Spot allocation strategy stays the same — Open-Closed principle."

Common extension hooks: Strategy injection, plugin registry, enum + interface combo.

---

## Step 8: Code Sketch (10 min)

**What to implement:**
- One service class with 1–2 core methods
- One interface + one implementation
- Enums for types/states

**What to skip:**
- Full getters/setters
- Main method (unless asked)
- Database/persistence layer

See [How to Write Code in Interview](06-how-to-write-code-in-interview.md).

---

## Time Budget Summary

| Step | Minutes | Cumulative |
|------|---------|------------|
| Clarify | 5 | 5 |
| Scope MVP | 2 | 7 |
| Identify entities | 3 | 10 |
| Class diagram | 10 | 20 |
| Public APIs | 5 | 25 |
| Patterns & SOLID | 5 | 30 |
| Extensibility | 3 | 33 |
| Code sketch | 10 | 43 |
| Buffer / follow-ups | 5–17 | 48–60 |

---

## Pivot Signals

| Interviewer says | You do |
|------------------|--------|
| "Design for 10M users" | Pivot to [HLD](../01-core-concepts/lld-vs-hld-boundary.md) |
| "Make it thread-safe" | Add locks, concurrent collections, immutability |
| "Add feature X" | Show extensibility — interface + new impl |
| "Write the park method" | Focus code on one flow, narrate edge cases |

---

## Related

- [How to Draw Class Diagrams](02-how-to-draw-class-diagrams.md)
- [How to Explain](03-how-to-explain.md)
- [Pattern Picker](04-pattern-picker.md)
- [Senior SWE Signals](05-senior-swe-signals.md)

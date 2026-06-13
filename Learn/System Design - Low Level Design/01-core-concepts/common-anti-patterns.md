# Common Anti-Patterns — LLD

What interviewers penalize and how to fix.

---

## God Class

**Symptom:** One class with 20+ methods — park, pay, print, email, report.

**Fix:** Split into Service + domain entities + dedicated collaborators.

---

## Pattern Soup

**Symptom:** "I'll use Factory, Abstract Factory, Builder, Prototype for one vending machine."

**Fix:** 1–2 patterns max, each tied to a real variation point.

---

## Anemic Domain Model

**Symptom:** All logic in `ParkingLotService`; entities are pure data bags.

**Fix:** Put natural behavior on entities (`spot.assign()`, `piece.isValidMove()`).

---

## Premature Infrastructure

**Symptom:** Kafka, Redis, microservices in an LLD parking lot.

**Fix:** In-memory + interfaces. Pivot to HLD only if interviewer asks scale.

---

## Over-Engineering

**Symptom:** 15 classes for tic-tac-toe.

**Fix:** 4–6 classes for MVP; add interfaces only at real extension points.

---

## Inheritance Abuse

**Symptom:** `ElectricParkingLot extends ParkingLot extends Building extends Property`

**Fix:** Composition + Strategy + enum types.

---

## Related

- [Senior SWE Signals](../00-interview-framework/05-senior-swe-signals.md)
- [LLD vs HLD Boundary](lld-vs-hld-boundary.md)

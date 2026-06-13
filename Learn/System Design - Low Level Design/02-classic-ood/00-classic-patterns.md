# Classic OOD Patterns — Reusable LLD Templates

Quick patterns that recur across the 64 classic OOD questions.

---

## Pattern 1: Service + Strategy + Domain

**Use for:** Parking Lot, Ride Sharing, Splitwise, Coupon Engine

```
Service → Strategy (interface) → Domain entities
```

---

## Pattern 2: State Machine (enum or State pattern)

**Use for:** Vending Machine, Order, Trip status, Seat hold

Simple transitions → `enum`. Side effects per transition → State pattern.

---

## Pattern 3: Composite Hierarchy

**Use for:** File System, Org Chart, Comment Thread, Bus Route

Parent contains children; same interface for leaf and composite.

---

## Pattern 4: Booking + Lock + Inventory

**Use for:** Movie Booking, Hotel, Flight Seat, Table Reservation

1. Search availability  
2. Hold resource (time-bound)  
3. Confirm / release  

---

## Pattern 5: Observer / Event Bus

**Use for:** Notification, Stock feed, Pub/Sub, Price alerts

Subject publishes; subscribers react decoupled.

---

## Pattern 6: Game Loop

**Use for:** Chess, Tic-Tac-Toe, Snake & Ladder, Board Game Framework

`Game` + `Board` + `Player` + `TurnManager` + win validation Strategy.

---

## Related

- [Pattern Picker](../00-interview-framework/04-pattern-picker.md)
- [Question Q01 Parking Lot](questions/Q01-parking-lot.md)

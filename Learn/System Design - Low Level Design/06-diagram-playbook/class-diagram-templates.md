# Class Diagram Templates — Copy-Paste Patterns

---

## Template 1: Service + Strategy

```
┌─────────────────┐     ┌──────────────────┐
│  XxxService     │────>│  XxxStrategy     │<<interface>>
│─────────────────│     │──────────────────│
│ +doAction()     │     │ +execute()       │
└────────┬────────┘     └────────┬─────────┘
         │                       │
         │ uses                  │ implements
         ▼                       ▼
┌─────────────────┐     ┌──────────────────┐
│  DomainRoot     │     │ ConcreteStrategy │
└─────────────────┘     └──────────────────┘
```

---

## Template 2: Inheritance Tree (Game Pieces)

```
        ┌──────────────┐
        │  ChessPiece  │<<abstract>>
        │──────────────│
        │ +move()      │
        └──────┬───────┘
       ┌───────┼───────┐
       ▼       ▼       ▼
   ┌──────┐ ┌──────┐ ┌──────┐
   │ King │ │Queen │ │ Rook │
   └──────┘ └──────┘ └──────┘
```

---

## Template 3: Composition Hierarchy

```
ParkingLot ◇──1──*── ParkingFloor *──1──*── ParkingSpot
```

---

## Template 4: Observer

```
┌─────────────┐       ┌──────────────┐
│  Subject    │──────>│  Observer    │<<interface>>
│─────────────│  *    │──────────────│
│ +notify()   │       │ +update()    │
└─────────────┘       └──────┬───────┘
                             │ implements
                    ┌────────┴────────┐
                    ▼                 ▼
              EmailObserver    SMSObserver
```

---

## Related

- [How to Draw Class Diagrams](../00-interview-framework/02-how-to-draw-class-diagrams.md)
- [Mermaid Examples](mermaid-examples.md)

# Mermaid Examples — LLD

---

## classDiagram — Parking Lot

```mermaid
classDiagram
    class ParkingLotService {
        +park(Vehicle) Ticket
        +unpark(Ticket) void
    }
    class ParkingStrategy {
        <<interface>>
        +findSpot(Vehicle, List) ParkingSpot
    }
    class ParkingLot {
        -floors: List
    }
    class ParkingSpot {
        +isAvailable() boolean
        +assign(Vehicle) void
    }
    class Vehicle {
        -type: VehicleType
    }
    ParkingLotService --> ParkingLot
    ParkingLotService ..> ParkingStrategy
    ParkingLot o-- ParkingFloor
    ParkingFloor *-- ParkingSpot
    ParkingSpot --> Vehicle
```

---

## sequenceDiagram — Park Flow

```mermaid
sequenceDiagram
    participant U as Driver
    participant S as ParkingLotService
    participant ST as Strategy
    participant SP as Spot
    U->>S: park(vehicle)
    S->>ST: findSpot(vehicle, spots)
    ST-->>S: spot
    S->>SP: assign(vehicle)
    S-->>U: ticket
```

---

## stateDiagram — Vending Machine

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> HasMoney: coin
    HasMoney --> Dispensing: select
    Dispensing --> Idle: dispense
```

---

## Related

- [Class Diagram Templates](class-diagram-templates.md)

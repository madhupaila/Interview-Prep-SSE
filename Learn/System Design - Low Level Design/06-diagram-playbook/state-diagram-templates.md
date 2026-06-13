# State Diagram Templates

---

## Vending Machine

```mermaid
stateDiagram-v2
    [*] --> Idle
    Idle --> HasMoney: insertCoin
    HasMoney --> Dispensing: selectItem
    Dispensing --> Idle: dispense
    HasMoney --> Idle: cancel
    Idle --> SoldOut: empty
```

---

## Order Lifecycle

```mermaid
stateDiagram-v2
    [*] --> Created
    Created --> Paid: payment
    Paid --> Shipped: ship
    Shipped --> Delivered: deliver
    Created --> Cancelled: cancel
    Paid --> Refunded: refund
```

---

## Elevator

```mermaid
stateDiagram-v2
    [*] --> Stopped
    Stopped --> MovingUp: requestAbove
    Stopped --> MovingDown: requestBelow
    MovingUp --> Stopped: atFloor
    MovingDown --> Stopped: atFloor
```

---

## When Enum Is Enough

| States | Recommendation |
|--------|----------------|
| 2–5, simple transitions | `enum Status` |
| Side effects per transition | State pattern |

---

## Related

- [Pattern Picker](../00-interview-framework/04-pattern-picker.md)

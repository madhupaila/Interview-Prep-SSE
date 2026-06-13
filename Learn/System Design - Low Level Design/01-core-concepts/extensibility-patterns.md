# Extensibility Patterns — LLD

Show **where** the system grows without rewriting core logic.

---

## Strategy Injection

```java
public ParkingLotService(ParkingLot lot, ParkingStrategy strategy) {
    this.lot = lot;
    this.strategy = strategy;
}
```

New algorithm = new class implementing interface.

---

## Plugin Registry

```java
public class ToolRegistry {
    private final Map<String, Tool> tools = new HashMap<>();
    public void register(String name, Tool tool) { tools.put(name, tool); }
    public Tool get(String name) { return tools.get(name); }
}
```

Used in: notification channels, payment gateways, LLM tools.

---

## Rule Engine (Lightweight)

```java
public interface PricingRule {
    Money apply(OrderContext ctx);
}
// Chain rules: DiscountRule, TaxRule, ShippingRule
```

---

## Enum + Interface Combo

```java
public enum SpotType { REGULAR, HANDICAP, ELECTRIC }
public interface ChargingCapable {
    void startCharging(Vehicle v);
}
public class ElectricSpot extends ParkingSpot implements ChargingCapable { }
```

---

## Open-Closed Interview Line

> "Core park() loop stays unchanged. New spot type = new class + enum value. New allocation = new Strategy."

---

## Related

- [SOLID Principles](solid-principles.md)
- [Pattern Picker](../00-interview-framework/04-pattern-picker.md)

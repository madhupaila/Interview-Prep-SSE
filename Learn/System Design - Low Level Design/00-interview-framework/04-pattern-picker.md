# Pattern Picker — When to Use Which Design Pattern

Don't force patterns. Map **variation points** and **lifecycle complexity** to the right pattern.

---

## Decision Tree

```
Need to swap algorithms at runtime?
  YES → Strategy
  NO ↓
Need to create objects without naming concrete class?
  YES → Factory / Abstract Factory
  NO ↓
Object has complex state transitions with side effects?
  YES → State
  NO → use enum for simple states
  ↓
Need undo/redo or queue operations?
  YES → Command
  NO ↓
Need to notify many listeners on change?
  YES → Observer
  NO ↓
Need to add behavior without subclassing?
  YES → Decorator
  NO ↓
Need single instance (config, connection pool)?
  YES → Singleton (prefer enum singleton in Java)
```

---

## Problem → Pattern Mapping

| LLD Problem | Pattern | Why |
|-------------|---------|-----|
| Parking spot allocation | Strategy | Nearest / cheapest / largest-first |
| Payment gateways | Strategy | Stripe vs PayPal vs Apple Pay |
| Vehicle / document creation | Factory | Hide concrete type selection |
| Vending machine lifecycle | State | Idle → HasMoney → Dispensing → SoldOut |
| Text editor undo | Command | Encapsulate action + inverse |
| Stock price alerts | Observer | Many subscribers, one price change |
| Coffee add-ons | Decorator | Milk, whip, caramel stack on base |
| Logger with multiple outputs | Observer or Chain of Responsibility | File, console, remote |
| Support ticket routing | Chain of Responsibility | L1 → L2 → L3 |
| Org chart | Composite | Manager contains employees |
| Chess piece movement | Strategy per piece | Each piece different move rules |
| Rate limiter algorithms | Strategy | Token bucket vs sliding window |
| LLM provider swap | Strategy | OpenAI vs Anthropic vs local |
| RAG pipeline steps | Chain of Responsibility / Pipeline | Retrieve → rerank → generate |

---

## Pattern Count Guideline

| Round length | Patterns to name |
|--------------|------------------|
| 45 min | 1–2 (well justified) |
| 60 min | 2–3 |
| Never | 5+ (pattern soup) |

---

## Strategy vs State vs Command

| Pattern | Focus | Key question |
|---------|-------|--------------|
| **Strategy** | Interchangeable algorithms | "Can I swap how we pick a spot?" |
| **State** | Object behavior changes with internal state | "Does the vending machine act differently when sold out?" |
| **Command** | Encapsulate request as object | "Do I need undo or a command queue?" |

---

## Factory vs Builder vs Prototype

| Pattern | Use when |
|---------|----------|
| **Factory Method** | One product type, subclass decides which |
| **Abstract Factory** | Families of related products (UI theme) |
| **Builder** | Many optional fields (meal, HTTP request, house) |
| **Prototype** | Clone expensive-to-create objects (game board) |

---

## Creational Quick Pick

| Need | Pick |
|------|------|
| One global config | Enum Singleton |
| Create without `new` scattered | Factory |
| Complex object with 10+ fields | Builder |
| Copy existing instance | Prototype |

---

## Related

- [Design Patterns GoF](../01-core-concepts/design-patterns-gof.md)
- [Extensibility Patterns](../01-core-concepts/extensibility-patterns.md)
- [Design Patterns Track](../03-design-patterns/questions/)

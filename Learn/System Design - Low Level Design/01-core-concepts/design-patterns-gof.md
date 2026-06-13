# Design Patterns (GoF) — LLD Reference

All 23 Gang of Four patterns with intent and LLD problem mapping.

---

## Creational (5)

| Pattern | Intent | LLD mapping |
|---------|--------|-------------|
| **Singleton** | One instance | Config, thread pool (prefer enum) |
| **Factory Method** | Subclass decides product | Chess pieces, documents |
| **Abstract Factory** | Families of products | UI themes, cross-platform widgets |
| **Builder** | Step-by-step complex object | Meal, HTTP request, pizza |
| **Prototype** | Clone existing instance | Game board copy, document template |

---

## Structural (7)

| Pattern | Intent | LLD mapping |
|---------|--------|-------------|
| **Adapter** | Legacy interface wrapper | Old payment API → new PaymentProcessor |
| **Bridge** | Abstraction vs implementation | Remote control + device vendors |
| **Composite** | Tree structures | Org chart, file system folders |
| **Decorator** | Add behavior dynamically | Coffee toppings, stream wrappers |
| **Facade** | Simplified subsystem API | Home theater, library checkout |
| **Flyweight** | Share intrinsic state | Forest of trees (shared mesh) |
| **Proxy** | Surrogate / lazy load | Image loader, access control |

---

## Behavioral (11)

| Pattern | Intent | LLD mapping |
|---------|--------|-------------|
| **Chain of Responsibility** | Pass request along chain | Support tiers, servlet filters, guardrails |
| **Command** | Encapsulate request | Undo/redo, job queue |
| **Interpreter** | Grammar evaluation | Simple rule DSL (rare in interviews) |
| **Iterator** | Traverse collection | Custom deck, playlist |
| **Mediator** | Centralize communication | Chat room, air traffic |
| **Memento** | Snapshot state | Editor undo snapshots |
| **Observer** | Notify on change | Stock ticker, event bus |
| **State** | Behavior by internal state | Vending machine, TCP connection |
| **Strategy** | Swap algorithms | Parking allocation, rate limit, LLM provider |
| **Template Method** | Algorithm skeleton | Data parser, game turn loop |
| **Visitor** | Operations on object structure | Tax on cart items |

---

## Most Common in Interviews (Top 8)

1. Strategy  2. Factory  3. State  4. Observer  
5. Command  6. Singleton  7. Decorator  8. Builder

---

## Related

- [Pattern Picker](../00-interview-framework/04-pattern-picker.md)
- [Design Patterns Track](../03-design-patterns/questions/)

# Master Memory Map — Core LLD Concepts

**Print this page.** One-glance reference for interviews.

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    SENIOR LLD MEMORY MAP                                │
├─────────────────────────────────────────────────────────────────────────┤
│ INTERVIEW FLOW                                                          │
│   Clarify → Scope MVP → Entities → Class Diagram → APIs → Patterns →   │
│   Extensibility → Code sketch                                           │
├─────────────────────────────────────────────────────────────────────────┤
│ OOP                                                                     │
│   Encapsulation │ Inheritance (IS-A) │ Polymorphism │ Abstraction      │
│   Composition over inheritance │ Favor interfaces                       │
├─────────────────────────────────────────────────────────────────────────┤
│ SOLID                                                                   │
│   S: one reason to change │ O: open extension, closed modification     │
│   L: subtypes substitutable │ I: small interfaces │ D: depend on abstr. │
├─────────────────────────────────────────────────────────────────────────┤
│ PATTERN PICKER                                                          │
│   Swap algorithm → Strategy │ Complex lifecycle → State (or enum)      │
│   Undo/redo → Command │ Notify many → Observer │ Create w/o new → Factory│
│   Add behavior → Decorator │ Single instance → Enum Singleton          │
├─────────────────────────────────────────────────────────────────────────┤
│ UML                                                                     │
│   + public - private │ ◆ composition ◇ aggregation │ --▷ extends       │
│   ..▷ implements │ 1, *, 0..1 multiplicity                             │
├─────────────────────────────────────────────────────────────────────────┤
│ API DESIGN                                                              │
│   Enums for fixed sets │ Domain exceptions │ Optional for nullable     │
│   Return domain types (Ticket) not strings │ Immutability for values    │
├─────────────────────────────────────────────────────────────────────────┤
│ CONCURRENCY                                                             │
│   synchronized │ ReentrantLock │ ConcurrentHashMap │ BlockingQueue      │
│   check-then-act → sync whole block │ ReadWriteLock for read-heavy     │
├─────────────────────────────────────────────────────────────────────────┤
│ EXTENSIBILITY                                                           │
│   Strategy injection │ Plugin registry │ enum + interface combo         │
│   Repository interface for persistence (don't build DB in LLD)          │
├─────────────────────────────────────────────────────────────────────────┤
│ ANTI-PATTERNS                                                           │
│   God class │ Pattern soup │ Premature DB/microservices │ Anemic domain │
├─────────────────────────────────────────────────────────────────────────┤
│ LLD vs HLD                                                              │
│   Classes & objects → LLD │ Millions users, QPS, shards → HLD          │
└─────────────────────────────────────────────────────────────────────────┘
```

## Quick Pattern Picker

| Need | Pick |
|------|------|
| Multiple allocation algorithms | Strategy |
| Order/vending machine states | State or enum |
| Undo stack | Command |
| Price change alerts | Observer |
| Create vehicles/pieces | Factory |
| Thread-safe singleton | enum Singleton |
| Producer-consumer | BlockingQueue |
| Swap LLM provider | Strategy |

## Class Diagram Layers

```
Service (orchestration) → Strategy/Factory (variation)
        ↓
   Domain entities (Lot, Spot, Vehicle)
        ↓
   Enums + Value objects
```

## Related

- [LLD Round Flow](../00-interview-framework/01-lld-round-flow.md)
- [Pattern Picker](../00-interview-framework/04-pattern-picker.md)
- [Gen AI LLD Memory Map](../05-genai-llm-lld/memory-map-genai-lld.md)

# How to Explain & Narrate — LLD Interviews

Structure your spoken answer so the interviewer can follow your thinking. LLD is about **object modeling**, not capacity math.

---

## PREP Method (Adapted for LLD)

| Letter | Meaning | Example |
|--------|---------|---------|
| **P** | Point | "I'll model this as three clusters: lot structure, entry/exit workflow, and allocation strategy." |
| **R** | Reason | "I'm separating allocation into a Strategy because we may switch nearest-first vs cheapest." |
| **E** | Example | "When a car enters, the service asks the strategy for a spot, issues a ticket, assigns the vehicle." |
| **P** | Pattern | "This is Strategy pattern — open for new algorithms without changing ParkingLotService." |

---

## Transition Phrases

Use these to move between sections smoothly:

| Transition | Phrase |
|------------|--------|
| Start | "Let me clarify scope before I draw anything." |
| To diagram | "I'll start with the core entities and build outward." |
| To interface | "This is a variation point — I'll extract an interface here." |
| To flow | "Let me walk through the park flow step by step." |
| To pattern | "I'm applying Strategy here because…" |
| To extensibility | "If we needed to add X, the extension point would be…" |
| To tradeoff | "The tradeoff is enum simplicity vs State pattern flexibility — I'd pick enum because…" |
| To code | "I'll sketch the core park method — focus on happy path plus one edge case." |

---

## Tradeoff Language

> "Option A is an enum for order status — simple, compile-time safe. Option B is State pattern — better when transitions have side effects. For MVP with 5 states and simple transitions, I'd pick enum."

Always end with **Pick** and **why**.

---

## Narration Structure (12–18 min)

```
[0:00] Clarify + confirm scope (2 min)
[2:00] Entity clusters + nouns/verbs (2 min)
[4:00] Class diagram — draw and explain relationships (5 min)
[9:00] Walk main flow — park/exit (3 min)
[12:00] Patterns + SOLID (2 min)
[14:00] Extensibility — one concrete example (2 min)
[16:00] Code sketch — one method (3 min)
[19:00] Buffer for follow-ups
```

---

## Senior Phrases That Score Points

- "I'll depend on the interface, not the concrete implementation — Dependency Inversion."
- "Composition over inheritance here — a ParkingLot HAS floors, it ISN'T a floor."
- "I'm not building persistence unless we need it — YAGNI for a 45-minute round."
- "Thread safety: this map needs `ConcurrentHashMap` or synchronized block because multiple entry gates."
- "I'd inject the strategy via constructor for testability."

---

## What NOT to Say

| Avoid | Say instead |
|-------|-------------|
| "I'll use every pattern" | "Strategy and Factory cover the two variation points" |
| "Let me list all getters" | "Public API is park, unpark, isFull" |
| "We need microservices" | "That's HLD scope — here I'll keep it in-process" |
| Silence while drawing | Narrate: "ParkingLot owns a list of floors…" |

---

## Related

- [LLD Round Flow](01-lld-round-flow.md)
- [Senior SWE Signals](05-senior-swe-signals.md)
- [Pattern Picker](04-pattern-picker.md)

# Hospital Management

**Track:** Classic OOD  
**Companies:** Epic, Cerner, Amazon  
**Difficulty:** Hard  

---

## Case Study

> **Full case study:** [CS-LLD-O35-hospital-management.md](../../../Case Studies/lld/classic-ood/CS-LLD-O35-hospital-management.md)
> **Read order:** Case Study → this question → [Java implementation](../../09-code-implementations/)

**Business context:** Real-world context modeled after Leading products in the Hospital Management domain. Read the full case study for requirements, constraints, ADRs, and ops.

**Key constraints:** budget, timeline, team size, tech stack

---

## 1. Problem Statement

Design hospital system: patients, doctors, appointments, medical records.

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | What is MVP scope for Hospital Management? | Core entities + 2 primary flows; extensions deferred |
| 2 | Persistence? | In-memory; Repository interface if interviewer asks |
| 3 | Multi-threaded? | Synchronize shared state if concurrent users assumed |
| 4 | Requirement: Design hospital system? | Include in MVP — Design hospital system |
| 5 | Requirement: patients? | Include in MVP — patients |
| 6 | Requirement: doctors? | Include in MVP — doctors |
| 7 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |
| 8 | Scale to distributed? | Single JVM LLD; pivot HLD if asked |

---

## 3. Functional & Non-Functional Requirements

**Functional:**
- HospitalService handles primary workflow described in requirements
- Validate inputs before state changes
- Enforce domain constraints with exceptions
- Support listing and lookup of core entities

**Non-Functional:**
- Clear separation of concerns (SOLID)
- Open-Closed via SchedulingStrategy interface at variation points
- Constructor injection for testability
- Thread-safe if concurrent access is in clarifying assumptions

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
| `Patient` | Medical record owner |
| `Doctor` | Provider |
| `Appointment` | Scheduled visit |
| `Department` | Ward |
| `MedicalRecord` | History |
| `BillingAccount` | Charges |

**Nouns → classes:** `Patient`, `Doctor`, `Appointment`, `Department`, `MedicalRecord`, `BillingAccount`  
**Verbs → methods:** `book()`, `cancelAppointment()`, `getRecord()`

---

## 5. Class Diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  HospitalService    │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Patient            │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Doctor             │────>│  Appointment     │
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class HospitalService {
        +Appointment book(Patient patient, Doctor doctor, TimeSlot slot)
        +void cancelAppointment(String id)
        +MedicalRecord getRecord(String patientId)
    }
    class Patient {
        +execute() void
    }
    class Doctor {
        +execute() void
    }
    class Appointment {
        +execute() void
    }
    class Department {
        +execute() void
    }
    class MedicalRecord {
        +execute() void
    }
    class BillingAccount {
        +execute() void
    }
    HospitalService --> Patient
```

---

## 6. Public API / Key Methods

```java
public class HospitalService {
    public Appointment book(Patient patient, Doctor doctor, TimeSlot slot);
    public void cancelAppointment(String id);
    public MedicalRecord getRecord(String patientId);
}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | Variation point in Hospital Management |

**SOLID:**
- **S:** HospitalService orchestrates; entities hold state
- **O:** New behavior via new SchedulingStrategy impl
- **D:** Depend on SchedulingStrategy interface

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant S as HospitalService
participant D as Patient
U->>S: book()
S->>D: validate / process
D-->>S: ok
S-->>U: result
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant S as HospitalService
U->>S: book(invalid)
S-->>U: DomainException
```

---

## 9. Extensibility

> "New `Strategy` implementation plugs in at runtime — no change to `HospitalService`."
>
> "Add new `Patient` subtypes or enum values for new categories — Open-Closed."

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
| Variation | if/else | Strategy | Strategy — 2+ behaviors |
| State | enum | State pattern | enum for simple lifecycles |
| Storage | in-memory | Repository | in-memory MVP |
| API return | primitive | domain object | domain object — type safety |

---

## 11. Concurrency & Edge Cases

- Single-threaded MVP unless clarifying assumes concurrent access
- If multi-user: synchronize on mutable aggregates or use concurrent collections
- Fail fast on invalid input with domain exceptions
- Idempotent retries where duplicate operations are possible

---

## 12. Interview Answer Script (15 min)

> "I'll design Hospital Management — clarify in-memory scope and MVP flows first."
>
> "Entities: `Patient`, `Doctor`, `Appointment`, `Department`, `MedicalRecord`, `BillingAccount`. Domain structure separate from `HospitalService` orchestration."
>
> "Problem: Design hospital system: patients, doctors, appointments, medical records."
>
> "`Patient` — medical record owner; owns its own invariants."
>
> "`Doctor` — provider; owns its own invariants."
>
> "`Appointment` — scheduled visit; owns its own invariants."
>
> "`HospitalService` validates input, coordinates entities, returns typed results."
>
> "Identify variation points — inject interfaces for Open-Closed extensibility."
>
> "Walk happy path on whiteboard, then failure case with domain exception."
>
> "Tradeoff: enum vs State pattern; Strategy vs if/else — pick with justification."

---

## 13. Follow-Up Questions

1. How would you unit test `Strategy` in isolation?
2. How would you extend Hospital Management without modifying core service?
3. How would you add persistence behind a Repository?
4. How does this map to a distributed HLD?

---

## 14. Related Links

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/hospital-management/README.md) (skeleton)

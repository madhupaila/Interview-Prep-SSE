# Elevator System — Case Study

**Case Study ID:** CS-LLD-O02
**Track:** Classic OOD
**Companies:** Amazon, Microsoft, Samsung
**Difficulty:** Hard
**Related question:** [Q02-elevator.md](../../System Design - Low Level Design/02-classic-ood/questions/Q02-elevator.md)
**Java implementation:** [elevator](../../System Design - Low Level Design/09-code-implementations/java/classic/elevator)

---

## Part 1 — Business Context

**Industry analog:** Otis elevator group dispatch algorithms

This case study examines **Elevator System** — a system type commonly built at Amazon and similar organizations. Design an elevator system for a building with multiple elevators serving multiple floors. Support hall calls (up/down) and car calls (destination). Optimize dispatch.

---

**Why now:** Teams with 3–5 YOE full-stack backgrounds are expected to connect product requirements to concrete architecture — especially with GenAI/LLM components where cost, safety, and correctness trade off sharply.

**Success definition:** Meet NFR targets, ship MVP within constraints, and articulate tradeoffs using ADRs.

---

## Part 2 — Stakeholders & Personas

| Persona | Goals | Pain points | Success metric |
|---------|-------|-------------|----------------|
| End user | Complete core flows quickly | Slow, unreliable UX | Task completion rate > 95% |
| Product owner | Ship MVP on schedule | Scope creep | On-time V1 delivery |
| SRE / platform | Meet SLO with observability | Opaque failures | Error budget > 0 monthly |
| Security / compliance | Data protection, audit trail | Regulatory breach | Zero critical findings |

---

## Part 3 — Requirements

### Functional Requirements (MoSCoW)

| Priority | Requirement | Acceptance criteria |
|----------|-------------|---------------------|
| Must | **Functional:** | Verified in integration tests |
| Must | Request elevator from floor with direction | Verified in integration tests |
| Must | Select elevator via scheduling strategy | Verified in integration tests |
| Must | Move elevator floor-by-floor serving queued requests | Verified in integration tests |
| Must | Process internal destination buttons | Verified in integration tests |
| Won't (MVP) | Multi-region active-active | Documented in PRD |
| Won't (MVP) | Advanced ML personalization | Documented in PRD |

### Non-Functional Requirements

| Attribute | Target | Measurement |
|-----------|--------|-------------|
| Latency | p99 < 200ms | APM / distributed tracing |
| Availability | 99.9% | Uptime SLO dashboard |
| Throughput | 10K peak QPS (scale phase) | Load test report |
| Security | AuthN/Z, encryption at rest/transit | Annual pen test |
| Maintainability | Modular services, ADRs documented | Change failure rate < 15% |

**From requirements analysis:**
:**
- Thread-safe request queue
- Pluggable dispatch (Strategy)
- Low coupling between Building and Elevator state machines

---

### Clarifying Questions (Discovery Phase)

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | How many elevators and floors? | Configurable N elevators, M floors |
| 2 | Scheduling algorithm? | Strategy — SCAN default |
| 3 | Concurrent requests? | Yes — multiple floors press buttons simultaneously |
| 4 | Elevator types? | Standard passenger; freight is extension |
| 5 | Display status? | Show current floor and direction per elevator |
| 6 | Persistence? | In-memory |
| 7 | Emergency stop? | Extension — safety subsystem |
| 8 | Weight limit? | Extension — capacity check |

---

---

## Part 4 — Constraints

| Constraint | Detail | Impact on design |
|------------|--------|------------------|
| Budget | $50K/month infra at V1 scale | Prefer managed services over self-host |
| Team | 2 backend, 1 frontend, 1 ML engineer | MVP scope strictly bounded |
| Timeline | MVP in 8 weeks | Defer nice-to-have features |
| Tech | Cloud-native on AWS/GCP | Use existing org SSO and VPC |
| Build vs buy | Buy vector DB / LLM API; build orchestration | Focus engineering on differentiation |

---

## Part 5 — Tradeoffs & Architecture Decision Records

### ADR-001: Primary architecture pattern

**Status:** Accepted  
**Context:** Need to balance delivery speed, operability, and scale for Elevator System.  
**Decision:** Event-driven async for writes; cache-heavy sync read path.  
**Consequences:** Higher eventual consistency on analytics; simpler peak handling.  
**Alternatives considered:** Fully synchronous CRUD — rejected due to peak QPS.


### ADR-002: Data store selection

**Status:** Accepted  
**Context:** Mixed OLTP, cache, and search/vector needs.  
**Decision:** PostgreSQL for source of truth; Redis for hot path; specialized index where needed.  
**Consequences:** Operational complexity of multiple stores; optimal per access pattern.  
**Alternatives considered:** Single document DB — rejected for strong consistency requirements.


### ADR-003: Multi-tenancy model

**Status:** Accepted  
**Context:** B2B SaaS with strict isolation requirements.  
**Decision:** Logical tenant_id on all rows + encryption per tenant for sensitive payloads.  
**Consequences:** Cost-effective vs physical isolation; requires rigorous integration tests.  
**Alternatives considered:** Database-per-tenant — rejected at 10K tenant scale.


### Tradeoffs Summary (from design analysis)


| Decision | A | B | Pick |
|----------|---|---|------|
| Dispatch | if/else nearest | Strategy | Strategy — multiple algorithms |
| Movement | simulate ticks | event-driven | tick simulation for LLD clarity |
| Request storage | per-elevator PQ | global queue | per-elevator — locality |
| Door state | enum | State pattern | enum unless complex interlocks |

---



---

## Part 6 — Capacity & Cost Estimation

**Scale projection:** Start with single-region MVP; model QPS and storage at 10× current load before Scale phase.

### Cost ballpark (V1)

- Compute: $5–15K/mo\n- Managed DB/cache: $3–8K/mo\n- LLM API (if applicable): usage-based; budget caps per tenant

---

## Part 7 — High-Level Design (Scale Projection / HLD Boundary)

The LLD object model is correct for **single-process / in-memory MVP**. When the interviewer pivots to scale:

### Scale triggers

| Signal | HLD addition |
|--------|--------------|
| Multiple instances | Stateless API behind load balancer |
| Shared state | Redis / distributed cache |
| Write contention | Message queue + async workers |
| Global users | Multi-region read replicas; CDN |



### Distributed sketch

```
Client → CDN → LB → API (stateless) → Cache → DB
                              ↓
                         Message queue → Workers
```

### Pivot script

> "My object model stays — ParkingLotService, Strategy, entities. "
> "At scale I'd add a central occupancy registry in Redis, event bus for cross-garage sync, and shard by buildingId."


---

## Part 8 — Low-Level Design

### Problem recap

Design an elevator system for a building with multiple elevators serving multiple floors. Support hall calls (up/down) and car calls (destination). Optimize dispatch.

---

### Core entities

| Entity | Role |
|--------|------|
| `Building` | Owns floors and elevator bank |
| `Elevator` | Current floor, direction, door state |
| `ElevatorController` | Facade — accepts external requests |
| `Request` | Floor + direction or destination |
| `Direction` | UP, DOWN, IDLE enum |
| `SchedulingStrategy` | Pick best elevator for hall call |

**Nouns → classes:** `Building`, `Elevator`, `ElevatorController`, `Request`, `Direction`, `SchedulingStrategy`  
**Verbs → methods:** `requestElevator(floor, direction)`, `selectElevator(Request)`, `step()`

---

### Class diagram

```
┌─────────────────────┐       ┌──────────────────┐
│  ElevatorController │──────>│ Strategy         │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ ConcreteStrategy │
│  Building           │       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  Elevator           │────>│  ElevatorController│
└─────────────────────┘     └──────────────────┘
```

```mermaid
classDiagram
    class ElevatorController {
        +void requestElevator(int floor, Direction direction)
        +void selectDestination(Elevator e, int floor)
        +void stepAll()
    }
    class Building {
        +execute()
    }
    class Elevator {
        +execute()
    }
    class ElevatorController {
        +execute()
    }
    class Request {
        +execute()
    }
    class Direction {
        +execute()
    }
    class Strategy {
        <<interface>>
        +apply()
    }
    ElevatorController --> Building
    ElevatorController ..> Strategy
```

---

### Public API

```java
public class ElevatorController {
    public void requestElevator(int floor, Direction direction);
    public void selectDestination(Elevator e, int floor);
    public void stepAll();
}
```

---

### Design patterns & SOLID

| Pattern | Application |
|---------|-------------|
| Strategy | SCAN, nearest-car, load-balancing dispatch |
| State | Elevator door open/closed/moving |

**SOLID:**
- **S:** Elevator moves itself; controller only dispatches
- **O:** New scheduler without changing Elevator
- **D:** Controller depends on SchedulingStrategy interface

---

### Sequence diagrams

**Happy path:**

```mermaid
sequenceDiagram
participant U as User
participant C as ElevatorController
participant ST as SchedulingStrategy
participant E as Elevator
U->>C: requestElevator(5, UP)
C->>ST: select(elevators, request)
ST-->>C: elevator2
C->>E: addRequest(5, UP)
E-->>U: assigned
```

**Failure path:**

```mermaid
sequenceDiagram
participant U as User
participant C as ElevatorController
U->>C: requestElevator(99, UP)
C-->>U: InvalidFloorException
```

---

### Concurrency & edge cases

- Synchronize addRequest on each Elevator instance
- Invalid floor → InvalidFloorException
- Duplicate hall call same floor — idempotent add
- All elevators idle — nearest responds

---

---

## Part 9 — Implementation Roadmap

| Phase | Timeline | Scope | Out of scope |
|-------|----------|-------|--------------|
| MVP | 2 weeks | Single-region, core user flows, manual ops | Multi-region, advanced analytics |
| V1 | 3 months | Production SLO, auth, monitoring, connector integrations | Custom ML models |
| Scale | 12 months | Auto-scaling, cost optimization, enterprise compliance | Edge deployment |

**MVP success criteria for Elevator System:** Core flows demo-ready; p99 within 2× target; on-call runbook draft.

---

## Part 10 — Operations

### SLI / SLO

| SLI | Definition | SLO |
|-----|------------|-----|
| Availability | successful_requests / total_requests | 99.9% monthly |
| Latency | p99 response time | < 300ms |

### Observability

- **Metrics:** Request rate, error rate, latency histograms, queue depth, cache hit ratio
- **Logs:** Structured JSON with `trace_id`, `tenant_id`, `user_id`
- **Traces:** OpenTelemetry across API → workers → DB/cache/LLM

### Deployment

- Blue/green or canary via CI/CD; feature flags for risky changes
- Database migrations backward-compatible; expand-contract pattern

### Incident Runbook

**Scenario:** p99 latency spike 3× baseline.

1. Check error budget burn in Grafana
2. Identify hot shard / tenant via trace tags
3. Scale workers or enable degradation mode
4. Post-incident: ADR if architecture change needed

### Security Checklist

- Authentication via org SSO (OIDC)
- Authorization at API + data layer
- Encryption at rest (AES-256) and in transit (TLS 1.3)
- Audit log for admin and sensitive reads
- Secrets in vault; no keys in code


---

## Part 11 — Interview Walkthrough (30 min)

> This is a 30-minute senior loop for **Elevator System**. Spend 5 minutes on context, 10 on HLD, 10 on LLD/boundaries, 5 on ops.

> "I'll model a building with N elevators and a controller facade for external requests."
>
> "Hall calls carry floor + direction; car calls are destination floors inside the cabin."
>
> "SchedulingStrategy picks the best elevator — default SCAN but swappable."
>
> "Each Elevator maintains a priority queue of pending stops sorted by direction sweep."
>
> "stepAll() advances simulation — move one floor, open doors, dequeue served requests."
>
> "Thread safety: synchronize mutation of elevator request queues."
>
> "State: IDLE, UP, DOWN with door OPEN/CLOSED enum on Elevator."
>
> "For HLD scale — central dispatch service; LLD object graph unchanged."

> ---

> If the interviewer asks about millions of users, I pivot: same object model, but add Redis cache, message queue, and sharded DB — see HLD case study.



---

## Part 11b — Practical Learning Lab

### Hands-on exercises

1. **Whiteboard (15 min):** Draw LLD object model and patterns from memory after reading Parts 1–5.
2. **Tradeoff drill (10 min):** Pick one ADR and argue the rejected alternative for 2 minutes.
3. **Failure mode (10 min):** Pick one failure from Part 7/10; write a 5-step runbook.
4. **Pivot practice (5 min):** Practice the HLD↔LLD pivot script aloud.
5. **Timed mock (45 min):** Use the linked question file without looking at this case study.

### Production readiness checklist

- [ ] SLO defined and dashboarded
- [ ] Load test at 2× expected peak QPS
- [ ] Chaos test: kill one dependency; verify degradation
- [ ] Security review: auth, encryption, audit
- [ ] Runbook linked from on-call playbook
- [ ] Cost model reviewed with FinOps
- [ ] ADRs stored in repo `docs/adr/`

### Industry comparison

| Capability | Otis elevator group dispatch algorithms (reference) | This design (MVP) | Scale phase |
|------------|----------------------|-------------------|-------------|
| Core flow | Production-grade | MVP scope in Part 9 | Part 9 Scale column |
| Reliability | Multi-region | Single-region 99.9% | Multi-region failover |
| Observability | Full APM + SRE | Metrics + traces + logs | SLO error budgets |
| Security | Enterprise compliance | Checklist in Part 10 | SOC2 / pen test |


### Senior interviewer rubric

| Signal | Strong | Weak |
|--------|--------|------|
| Requirements | Measurable NFRs stated upfront | Vague "it should scale" |
| Constraints | Names budget, team, timeline | Ignores constraints |
| Tradeoffs | ADR with rejected alternative | Single option only |
| Depth | Failure modes unprompted | Happy path only |
| Communication | Structured 30-min narrative | Jumps to diagram |



---

## Part 12 — Related Links

- **Question file:** [Q02-elevator.md](../../System Design - Low Level Design/02-classic-ood/questions/Q02-elevator.md)
- **Template:** [case-study-template.md](../00-framework/case-study-template.md)
- **Industry standards:** [industry-standards-reference.md](../00-framework/industry-standards-reference.md)

- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)
- [SOLID principles](../../01-core-concepts/solid-principles.md)
- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)
- [Java implementation](../../09-code-implementations/java/classic/elevator/) (full)
- [HLD counterpart](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q30-parking-lot-elevator.md)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenerate all 114 LLD question markdown files at Parking Lot (Q01) detail level.

Usage:
    python _expand_all_questions.py

Architecture:
    - gen_all_specs.py  — META registry (114 questions) + make_spec() builder
    - _slug_details.py  — problem-specific overrides (clarify, APIs, sequences, scripts)
    - Skips Q01-parking-lot.md (hand-crafted gold standard preserved)

Output paths:
    02-classic-ood/questions/Q{nn}-{slug}.md
    03-design-patterns/questions/Q{nn}-{slug}.md
    04-concurrency-lld/questions/Q{nn}-{slug}.md
    05-genai-llm-lld/questions/Q{nn}-{slug}.md
"""

from __future__ import annotations

import os
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent

# Companion data modules (compact dicts per question):
#   gen_all_specs.py — META registry (114 questions) + make_spec()
#   _slug_details.py   — problem-specific overrides (clarify, APIs, sequences, scripts)

TRACKS = {
    "classic": ("02-classic-ood/questions", "Classic OOD", "classic"),
    "patterns": ("03-design-patterns/questions", "Design Patterns", "patterns"),
    "concurrency": ("04-concurrency-lld/questions", "Concurrency LLD", "concurrency"),
    "genai": ("05-genai-llm-lld/questions", "Gen AI LLD", "genai"),
}

HLD_PREFIX = "../System%20Design%20-%20High%20Level%20Design/"


def _ascii_diagram(service: str, entities: list[tuple[str, str]], iface: str = "Strategy") -> str:
    ent_names = [e[0] for e in entities[:4]]
    root = ent_names[0] if ent_names else "DomainRoot"
    second = ent_names[1] if len(ent_names) > 1 else "Entity"
    third = ent_names[2] if len(ent_names) > 2 else "SubEntity"
    return f"""```
┌─────────────────────┐       ┌──────────────────┐
│  {service:<19}│──────>│ {iface:<16} │<<interface>>
│─────────────────────│       │──────────────────│
│ +orchestrate()      │       │ +apply()         │
└─────────┬───────────┘       └────────┬─────────┘
          │ owns                       │ implements
          ▼                   ┌────────▼─────────┐
┌─────────────────────┐       │ Concrete{iface:<9}│
│  {root:<19}│       └──────────────────┘
└─────────┬───────────┘
          │ *
          ▼
┌─────────────────────┐     ┌──────────────────┐
│  {second:<19}│────>│  {third:<16}│
└─────────────────────┘     └──────────────────┘
```"""


def _mermaid_class(service: str, methods: list[str], entities: list[tuple[str, str]], iface: str = "Strategy") -> str:
    lines = ["classDiagram"]
    lines.append(f"    class {service} {{")
    for m in methods[:4]:
        ms = m.strip()
        if ms.startswith("public "):
            ms = ms[7:].strip()
        if not ms.startswith(("+", "-", "#", "~")):
            ms = "+" + ms
        lines.append(f"        {ms}")
    lines.append("    }")
    for en, _ in entities[:5]:
        lines.append(f"    class {en} {{")
        lines.append("        +execute()")
        lines.append("    }")
    lines.append(f"    class {iface} {{")
    lines.append("        <<interface>>")
    lines.append("        +apply()")
    lines.append("    }")
    if entities:
        lines.append(f"    {service} --> {entities[0][0]}")
    lines.append(f"    {service} ..> {iface}")
    return "\n".join(lines)


def render(spec: dict[str, Any]) -> str:
    track_key = spec["track"]
    _, track_label, java_track = TRACKS[track_key]
    num = spec["num"]
    slug = spec["slug"]
    title = spec["title"]
    companies = spec["companies"]
    diff = spec["difficulty"]
    service = spec["service"]
    methods = spec["methods"]
    entities = spec["entities"]
    patterns = spec["patterns"]
    solid = spec["solid"]
    clarify = spec["clarify"]
    functional = spec["functional"]
    non_functional = spec["non_functional"]
    nouns = spec["nouns"]
    verbs = spec["verbs"]
    happy = spec["happy_seq"]
    fail = spec["fail_seq"]
    ext = spec["extensibility"]
    tradeoffs = spec["tradeoffs"]
    concurrency = spec["concurrency"]
    script = spec["script"]
    followups = spec["followups"]
    impl = spec.get("impl", "skeleton")
    hld = spec.get("hld")

    clarify_rows = "\n".join(
        f"| {i} | {q} | {a} |" for i, (q, a) in enumerate(clarify, 1)
    )
    entity_rows = "\n".join(f"| `{name}` | {role} |" for name, role in entities)
    func_bullets = "\n".join(f"- {f}" for f in functional)
    nfr_bullets = "\n".join(f"- {f}" for f in non_functional)
    pattern_rows = "\n".join(f"| {p} | {app} |" for p, app in patterns)
    solid_lines = "\n".join(f"- **{k}:** {v}" for k, v in solid)
    trade_rows = "\n".join(f"| {d} | {a} | {b} | {p} |" for d, a, b, p in tradeoffs)
    conc_bullets = "\n".join(f"- {c}" for c in concurrency)
    script_quotes = "\n>\n".join(f'> "{p}"' for p in script)
    ext_quotes = "\n>\n".join(f'> "{e}"' for e in ext)
    follow_lines = "\n".join(f"{i}. {q}" for i, q in enumerate(followups, 1))

    java_sig = "\n".join(
        f"    {m.strip() if m.strip().startswith('public') else 'public ' + m.strip()};"
        for m in methods
    )
    iface_name = patterns[0][0] if patterns else "Strategy"

    ascii_diag = spec.get("ascii") or _ascii_diagram(service, entities, iface_name)
    mermaid_cls = spec.get("mermaid_class") or _mermaid_class(service, methods, entities, iface_name)

    impl_note = "full" if impl == "full" else "skeleton"
    java_link = f"../../09-code-implementations/java/{java_track}/{slug}/"

    links = [
        f"- [Strategy pattern](../../01-core-concepts/design-patterns-gof.md)",
        f"- [SOLID principles](../../01-core-concepts/solid-principles.md)",
        f"- [Concurrency fundamentals](../../01-core-concepts/concurrency-fundamentals.md)",
        f"- [Java implementation]({java_link}) ({impl_note})",
    ]
    if hld:
        links.append(f"- [HLD counterpart]({HLD_PREFIX}{hld})")
    if track_key == "genai":
        links.insert(0, f"- [Gen AI LLD memory map](../../05-genai-llm-lld/memory-map-genai-lld.md)")
    if track_key == "concurrency":
        links.insert(0, f"- [Concurrency LLD track](../../04-concurrency-lld/README.md)")

    return f"""# {title}

**Track:** {track_label}  
**Companies:** {companies}  
**Difficulty:** {diff}  

---

## 1. Problem Statement

{spec["problem"]}

---

## 2. Clarifying Questions

| # | Question | Expected answer |
|---|----------|-----------------|
{clarify_rows}

---

## 3. Functional & Non-Functional Requirements

**Functional:**
{func_bullets}

**Non-Functional:**
{nfr_bullets}

---

## 4. Core Entities & Relationships

| Entity | Role |
|--------|------|
{entity_rows}

**Nouns → classes:** {nouns}  
**Verbs → methods:** {verbs}

---

## 5. Class Diagram

{ascii_diag}

```mermaid
{mermaid_cls}
```

---

## 6. Public API / Key Methods

```java
public class {service} {{
{java_sig}
}}
```

---

## 7. Design Patterns & SOLID

| Pattern | Application |
|---------|-------------|
{pattern_rows}

**SOLID:**
{solid_lines}

---

## 8. Sequence Diagrams

**Happy path:**

```mermaid
sequenceDiagram
{happy}
```

**Failure path:**

```mermaid
sequenceDiagram
{fail}
```

---

## 9. Extensibility

{ext_quotes}

---

## 10. Tradeoffs

| Decision | A | B | Pick |
|----------|---|---|------|
{trade_rows}

---

## 11. Concurrency & Edge Cases

{conc_bullets}

---

## 12. Interview Answer Script (15 min)

{script_quotes}

---

## 13. Follow-Up Questions

{follow_lines}

---

## 14. Related Links

{chr(10).join(links)}
"""


def _d(**kw: Any) -> dict[str, Any]:
    return kw


# fmt: off
ALL_SPECS: list[dict[str, Any]] = []


def _hand_spec(
    track: str, num: int, slug: str, title: str, companies: str, difficulty: str,
    problem: str, clarify: list, functional: list, non_functional: list,
    entities: list, nouns: str, verbs: str, service: str, methods: list,
    patterns: list, solid: list, happy_seq: str, fail_seq: str,
    extensibility: list, tradeoffs: list, concurrency: list, script: list,
    followups: list, hld: str | None = None, impl: str = "skeleton", skip: bool = False,
    **extra: Any,
) -> dict[str, Any]:
    d = dict(
        track=track, num=num, slug=slug, title=title, companies=companies,
        difficulty=difficulty, problem=problem, clarify=clarify, functional=functional,
        non_functional=non_functional, entities=entities, nouns=nouns, verbs=verbs,
        service=service, methods=methods, patterns=patterns, solid=solid,
        happy_seq=happy_seq, fail_seq=fail_seq, extensibility=extensibility,
        tradeoffs=tradeoffs, concurrency=concurrency, script=script, followups=followups,
        hld=hld, impl=impl, skip=skip,
    )
    d.update(extra)
    return d


def _cl(*pairs: tuple[str, str]) -> list[tuple[str, str]]:
    return list(pairs)


def _seq(*lines: str) -> str:
    return "\n".join(lines)


def _register(spec: dict[str, Any]) -> None:
    ALL_SPECS.append(spec)

def _load_all_specs() -> None:
    """Populate ALL_SPECS with 114 problem-specific entries."""
    if ALL_SPECS:
        return

    from gen_all_specs import META, make_spec  # noqa: WPS433

    # Q01 Parking Lot — hand-crafted gold standard (skip overwrite)
    ALL_SPECS.append(_hand_spec(
        "classic", 1, "parking-lot", "Design Parking Lot",
        "Amazon, Microsoft, Google, Oracle", "Medium",
        "Design a parking lot with multiple floors and spot types (compact, large, handicap). "
        "Support vehicle entry (park), exit (unpark), and display availability. Optional: payment on exit.",
        _cl(
            ("Single building or multi-building?", "Single parking lot, multiple floors"),
            ("Vehicle types?", "Motorcycle, car, truck — different spot sizes"),
            ("Multi-threaded entry gates?", "Yes — multiple gates concurrent"),
            ("Payment in scope?", "MVP: ticket on entry; payment interface on exit"),
            ("Spot allocation policy?", "Configurable — nearest first default"),
            ("Persistence?", "In-memory"),
            ("Electric charging?", "Extension — not MVP"),
            ("Valet?", "Extension"),
        ),
        ["Park vehicle → assign spot, issue ticket", "Unpark with ticket → free spot",
         "Report availability by vehicle type", "Reject when no compatible spot available"],
        ["Thread-safe entry/exit at multiple gates", "Extensible allocation policy (Strategy)",
         "SOLID — payment separate from parking"],
        [("ParkingLot", "Root aggregate — floors, tickets"), ("ParkingFloor", "Collection of spots on one level"),
         ("ParkingSpot", "Holds one vehicle; has SpotType"), ("Vehicle", "Type + license plate"),
         ("Ticket", "Issued on park; used on exit"), ("ParkingLotService", "Orchestrates park/unpark"),
         ("ParkingStrategy", "Spot allocation algorithm"), ("PaymentService", "Optional exit payment")],
        "`ParkingLot`, `ParkingFloor`, `ParkingSpot`, `Vehicle`, `Ticket`, `ParkingLotService`, `ParkingStrategy`",
        "`park(Vehicle)`, `unpark(Ticket)`, `isFull(VehicleType)`",
        "ParkingLotService",
        ["Ticket park(Vehicle vehicle)", "void unpark(Ticket ticket)", "boolean isFull(VehicleType type)"],
        [("Strategy", "Spot allocation — nearest, cheapest, largest-first"),
         ("Factory", "Optional Vehicle factory from plate + type")],
        [("S", "PaymentService only handles payment"), ("O", "New strategy without editing park loop"),
         ("L", "All Vehicle types work in park()"), ("D", "Service depends on ParkingStrategy interface")],
        _seq(
            "participant D as Driver", "participant S as ParkingLotService", "participant ST as Strategy",
            "participant SP as Spot", "participant P as PaymentService",
            "D->>S: park(vehicle)", "S->>ST: findSpot(vehicle, availableSpots)", "ST-->>S: spot",
            "S->>SP: assign(vehicle)", "S-->>D: ticket", "D->>S: unpark(ticket)",
            "S->>P: charge(ticket)", "S->>SP: vacate()",
        ),
        _seq(
            "participant D as Driver", "participant S as ParkingLotService", "participant ST as Strategy",
            "D->>S: park(truck)", "S->>ST: findSpot(truck, spots)", "ST-->>S: empty",
            "S-->>D: LotFullException",
        ),
        ["Electric spots: add SpotType.ELECTRIC and ChargingCapable interface on ElectricSpot.",
         "Pricing rules: inject PricingStrategy into PaymentService."],
        [("Allocation", "if/else", "Strategy", "Strategy — 2+ policies"),
         ("Spot state", "enum", "State pattern", "enum Occupied/Available"),
         ("Thread safety", "sync lot", "sync per spot", "sync per spot — finer granularity"),
         ("Ticket ID", "UUID", "AtomicLong", "AtomicLong — readable tickets")],
        ["check-then-act on spot: synchronize on ParkingSpot during assign/vacate",
         "Lot full for vehicle type → LotFullException",
         "Invalid/expired ticket on exit → InvalidTicketException",
         "Motorcycle in compact spot OK; truck needs large spot"],
        ["I'll design an in-memory parking lot for one building with multiple floors and concurrent entry gates.",
         "Three clusters: structure — Lot, Floor, Spot; workflow — Service, Ticket, Payment; variation — ParkingStrategy.",
         "Vehicle has type — motorcycle, car, truck. Spot has compatible types via SpotType enum.",
         "park() asks strategy for a spot from available compatible spots, assigns vehicle, issues ticket.",
         "unpark() validates ticket, calls PaymentService, vacates spot. synchronize on spot for thread safety.",
         "Strategy pattern for nearest-first vs other policies — injected at construction.",
         "Extensions: electric charging via new spot type; valet as separate service facade.",
         "If interviewer asks millions of users — pivot to HLD with central occupancy service and Redis."],
        ["How would you add dynamic pricing by hour?", "How would you support reserved spots?",
         "Design for multiple parking lots (registry)?", "How to test NearestFirstStrategy in isolation?"],
        hld="03-classic-hld/questions/Q30-parking-lot-elevator.md", impl="full", skip=True,
    ))

    # Q02 Elevator — enhanced hand-crafted
    ALL_SPECS.append(_hand_spec(
        "classic", 2, "elevator", "Elevator System", "Amazon, Microsoft, Samsung", "Hard",
        "Design an elevator system for a building with multiple elevators serving multiple floors. "
        "Support hall calls (up/down) and car calls (destination). Optimize dispatch.",
        _cl(
            ("How many elevators and floors?", "Configurable N elevators, M floors"),
            ("Scheduling algorithm?", "Strategy — SCAN default"),
            ("Concurrent requests?", "Yes — multiple floors press buttons simultaneously"),
            ("Elevator types?", "Standard passenger; freight is extension"),
            ("Display status?", "Show current floor and direction per elevator"),
            ("Persistence?", "In-memory"),
            ("Emergency stop?", "Extension — safety subsystem"),
            ("Weight limit?", "Extension — capacity check"),
        ),
        ["Request elevator from floor with direction", "Select elevator via scheduling strategy",
         "Move elevator floor-by-floor serving queued requests", "Process internal destination buttons"],
        ["Thread-safe request queue", "Pluggable dispatch (Strategy)",
         "Low coupling between Building and Elevator state machines"],
        [("Building", "Owns floors and elevator bank"), ("Elevator", "Current floor, direction, door state"),
         ("ElevatorController", "Facade — accepts external requests"), ("Request", "Floor + direction or destination"),
         ("Direction", "UP, DOWN, IDLE enum"), ("SchedulingStrategy", "Pick best elevator for hall call")],
        "`Building`, `Elevator`, `ElevatorController`, `Request`, `Direction`, `SchedulingStrategy`",
        "`requestElevator(floor, direction)`, `selectElevator(Request)`, `step()`",
        "ElevatorController",
        ["void requestElevator(int floor, Direction direction)", "void selectDestination(Elevator e, int floor)",
         "void stepAll()"],
        [("Strategy", "SCAN, nearest-car, load-balancing dispatch"), ("State", "Elevator door open/closed/moving")],
        [("S", "Elevator moves itself; controller only dispatches"), ("O", "New scheduler without changing Elevator"),
         ("D", "Controller depends on SchedulingStrategy interface")],
        _seq("participant U as User", "participant C as ElevatorController", "participant ST as SchedulingStrategy",
             "participant E as Elevator", "U->>C: requestElevator(5, UP)", "C->>ST: select(elevators, request)",
             "ST-->>C: elevator2", "C->>E: addRequest(5, UP)", "E-->>U: assigned"),
        _seq("participant U as User", "participant C as ElevatorController",
             "U->>C: requestElevator(99, UP)", "C-->>U: InvalidFloorException"),
        ["New dispatch policy: implement SchedulingStrategy and inject at startup.",
         "Express elevator: subclass Elevator with restricted floor range."],
        [("Dispatch", "if/else nearest", "Strategy", "Strategy — multiple algorithms"),
         ("Movement", "simulate ticks", "event-driven", "tick simulation for LLD clarity"),
         ("Request storage", "per-elevator PQ", "global queue", "per-elevator — locality"),
         ("Door state", "enum", "State pattern", "enum unless complex interlocks")],
        ["Synchronize addRequest on each Elevator instance", "Invalid floor → InvalidFloorException",
         "Duplicate hall call same floor — idempotent add", "All elevators idle — nearest responds"],
        ["I'll model a building with N elevators and a controller facade for external requests.",
         "Hall calls carry floor + direction; car calls are destination floors inside the cabin.",
         "SchedulingStrategy picks the best elevator — default SCAN but swappable.",
         "Each Elevator maintains a priority queue of pending stops sorted by direction sweep.",
         "stepAll() advances simulation — move one floor, open doors, dequeue served requests.",
         "Thread safety: synchronize mutation of elevator request queues.",
         "State: IDLE, UP, DOWN with door OPEN/CLOSED enum on Elevator.",
         "For HLD scale — central dispatch service; LLD object graph unchanged."],
        ["How would you handle peak morning traffic?", "Design for elevator maintenance mode?",
         "How to prevent starvation on high floors?", "Unit test SCAN strategy in isolation?"],
        hld="03-classic-hld/questions/Q30-parking-lot-elevator.md", impl="full",
    ))

    for track_key, rows in (
        ("classic_rest", META["classic_rest"]),
        ("patterns", META["patterns"]),
        ("concurrency", META["concurrency"]),
        ("genai", META["genai"]),
    ):
        for row in rows:
            s = make_spec(track_key, row)
            # normalize keys for render()
            s["difficulty"] = s.get("difficulty", row[4])
            ALL_SPECS.append(s)


def main() -> int:
    _load_all_specs()
    written = 0
    skipped = 0
    errors: list[str] = []

    for spec in ALL_SPECS:
        track_key = spec["track"]
        folder, _, _ = TRACKS[track_key]
        num = spec["num"]
        slug = spec["slug"]
        out_dir = ROOT / folder
        out_path = out_dir / f"Q{num:02d}-{slug}.md"

        if spec.get("skip"):
            skipped += 1
            print(f"SKIP  {out_path.relative_to(ROOT)}")
            continue

        try:
            out_dir.mkdir(parents=True, exist_ok=True)
            content = render(spec)
            out_path.write_text(content, encoding="utf-8")
            written += 1
            print(f"WRITE {out_path.relative_to(ROOT)}")
        except Exception as exc:  # noqa: BLE001
            errors.append(f"{out_path}: {exc}")
            print(f"ERROR {out_path.relative_to(ROOT)}: {exc}", file=sys.stderr)

    print(f"\nDone: {written} written, {skipped} skipped, {len(errors)} errors")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

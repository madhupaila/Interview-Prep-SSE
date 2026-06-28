# How to Read Case Studies

Case studies bridge **real product thinking** and **interview execution**. Each document follows the same 12-part flow: business context → requirements → constraints → tradeoffs → HLD → LLD → ops.

---

## Two Learning Paths

### Path A — HLD First (System Design Round)

1. Read **Part 1–4** (context, requirements, constraints) — 15 min
2. Sketch your own diagram before reading **Part 7**
3. Compare with ADRs in **Part 5** — note what you missed
4. Read **LLD Boundary** in Part 8 — prepare for "design the classes" follow-up
5. Practice **Part 11** walkthrough aloud

### Path B — LLD First (Object Design Round)

1. Read **Part 1–3** for domain vocabulary — 10 min
2. Design classes before reading **Part 8**
3. Read **Scale Projection** in Part 7 — prepare for HLD pivot
4. Code against [Java implementations](../../System%20Design%20-%20Low%20Level%20Design/09-code-implementations/)
5. Practice **Part 11** with object-first narration

### Path C — Full Stack / Senior Loop (Recommended)

1. Start with **paired/** case studies (end-to-end HLD + LLD)
2. Read individual HLD and LLD case studies for depth
3. Do the linked question file as a timed mock (45 min)
4. Review ops section (Part 10) — senior signal differentiator

---

## Suggested Weekly Cadence (3–5 YOE)

| Day | Activity |
|-----|----------|
| Mon | Case study Parts 1–5 (context + decisions) |
| Tue | HLD Part 7 + whiteboard |
| Wed | LLD Part 8 + class diagram |
| Thu | Timed mock using linked question file |
| Fri | Ops + 30-min walkthrough recording |

---

## Paired vs Individual Case Studies

| Type | Location | When to use |
|------|----------|-------------|
| **Paired** | [paired/](../paired/) | End-to-end learning; senior full-stack rounds |
| **HLD individual** | [hld/](../hld/) | System design interview prep |
| **LLD individual** | [lld/](../lld/) | OOD / patterns / concurrency rounds |

Individual files cross-link to paired docs when a canonical end-to-end narrative exists.

---

## Integration with Question Files

Every HLD/LLD question file includes a **Case Study** block at the top linking here. Recommended order:

```
Case Study (full narrative) → Question file (interview script) → Java code (LLD)
```

The question file stays **interview-focused** (15-min script, diagrams). The case study adds **product context, constraints, roadmap, and ops**.

---

## Related

- [Case Study Template](case-study-template.md)
- [Industry Standards Reference](industry-standards-reference.md)
- [Case Studies Index](../index.md)
- [LLD vs HLD Boundary](../../System%20Design%20-%20Low%20Level%20Design/01-core-concepts/lld-vs-hld-boundary.md)

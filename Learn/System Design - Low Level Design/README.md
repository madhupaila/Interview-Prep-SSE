# Senior SWE LLD Interview Prep Guide

**Target:** 3–5 YOE Full Stack Engineer → Senior Software Engineer (Gen AI / LLM focus)

A modular, interview-ready study system with **114 company-tagged LLD questions**, framework playbooks, memory maps, class diagrams, spoken answer scripts, and Java reference implementations.

---

## How to Use This Repo

1. **Week 0 (recommended):** Read [Case Studies Library](../Case%20Studies/README.md) — start with [Parking Lot LLD case study](../Case%20Studies/lld/classic-ood/CS-LLD-O01-parking-lot.md) or a [paired end-to-end doc](../Case%20Studies/paired/CS-PAIR-01-enterprise-rag.md).
2. **Week 1:** Read [Interview Framework](00-interview-framework/) + [Diagram Playbook](06-diagram-playbook/) — learn *how* to answer any LLD question.
3. **Week 2:** Study [Core Concepts](01-core-concepts/) + memorize [Memory Maps](01-core-concepts/memory-map-master.md).
4. **Weeks 3–4:** Complete [Design Patterns Track](03-design-patterns/) (25 questions) — case study → question → code.
5. **Weeks 5–6:** Complete [Classic OOD Track](02-classic-ood/) (64 questions).
6. **Week 7:** Complete [Concurrency LLD Track](04-concurrency-lld/) (15 questions).
7. **Week 8:** Complete [Gen AI LLD Track](05-genai-llm-lld/) (10 questions) + mocks.
8. **Before each interview:** Check [Company Question Index](07-company-question-index.md) for likely questions.
9. **For code practice:** See [Java Implementations](09-code-implementations/).

---

## Repository Structure

| Folder | Contents |
|--------|----------|
| [Case Studies](../Case%20Studies/) | **219 end-to-end case studies** (requirements → LLD → scale projection) + 20 paired HLD+LLD narratives |
| [00-interview-framework/](00-interview-framework/) | 8-step flow, class diagrams, narration, pattern picker, code guidance |
| [01-core-concepts/](01-core-concepts/) | OOP, SOLID, GoF patterns, UML, concurrency, anti-patterns |
| [02-classic-ood/](02-classic-ood/) | **60 full question scripts** |
| [03-design-patterns/](03-design-patterns/) | **25 pattern-focused question scripts** |
| [04-concurrency-lld/](04-concurrency-lld/) | **15 thread-safety question scripts** |
| [05-genai-llm-lld/](05-genai-llm-lld/) | **10 Gen AI object-design scripts** |
| [06-diagram-playbook/](06-diagram-playbook/) | Class, sequence, state diagram templates |
| [07-company-question-index.md](07-company-question-index.md) | Company × question lookup |
| [08-study-schedule/](08-study-schedule/) | 8-week day-by-day plan |
| [09-code-implementations/](09-code-implementations/) | Java reference code (25 full + 85 skeletons) |

---

## Question Count

| Track | Questions | Location |
|-------|-----------|----------|
| Classic OOD | 64 | [02-classic-ood/questions/](02-classic-ood/questions/) |
| Design Patterns | 25 | [03-design-patterns/questions/](03-design-patterns/questions/) |
| Concurrency LLD | 15 | [04-concurrency-lld/questions/](04-concurrency-lld/questions/) |
| Gen AI / LLM LLD | 10 | [05-genai-llm-lld/questions/](05-genai-llm-lld/questions/) |
| **Total** | **114** | |

---

## Per-Question Template

Every question file includes **Parking Lot-level detail** (all 14 sections):

1. Company tags + difficulty
2. **8 problem-specific** clarifying questions (not generic templates)
3. Functional & non-functional requirements
4. Core entities & relationships with roles
5. Class diagram (ASCII + Mermaid with entity-specific methods)
6. Public API / key Java methods
7. Design patterns & SOLID (correct pattern names, not interface names)
8. Sequence diagrams (happy path + failure path)
9. Extensibility discussion
10. Tradeoffs table with Pick
11. Concurrency & edge cases
12. **Full 8–10 paragraph interview answer script**
13. Follow-up questions
14. Related links (concepts, Java impl, HLD counterpart)

**Regenerate questions** (after editing specs): `python _expand_all_questions.py`

---

## How to Answer Any LLD Question

```
1. Clarify (5 min) → 2. Scope MVP (2 min) → 3. Identify entities (3 min)
→ 4. Class diagram (10 min) → 5. Public APIs (5 min) → 6. Patterns (5 min)
→ 7. Extensibility (3 min) → 8. Code sketch (10 min)
```

**Senior move:** Name 1–3 patterns with justification — not pattern soup. Draw interfaces at variation points.

---

## Mock Interview Checklist

- [ ] Clarify requirements before drawing (5 min)
- [ ] State MVP scope explicitly
- [ ] Identify nouns → classes, verbs → methods
- [ ] Draw class diagram with interfaces for extensibility
- [ ] Walk through 2 main flows (sequence diagram)
- [ ] Name patterns and SOLID principles aloud
- [ ] Discuss extensibility without being prompted
- [ ] Sketch core method in Java (10 min)
- [ ] Mention thread safety if multi-threaded

---

## Quick Links

- [Case Studies Index](../Case%20Studies/index.md)
- [Enterprise RAG Paired Case Study](../Case%20Studies/paired/CS-PAIR-01-enterprise-rag.md)
- [8-Week Study Plan](08-study-schedule/8-week-plan.md)
- [LLD Round Flow](00-interview-framework/01-lld-round-flow.md)
- [How to Draw Class Diagrams](00-interview-framework/02-how-to-draw-class-diagrams.md)
- [Pattern Picker](00-interview-framework/04-pattern-picker.md)
- [Master Memory Map](01-core-concepts/memory-map-master.md)
- [Gen AI LLD Memory Map](05-genai-llm-lld/memory-map-genai-lld.md)
- [LLD vs HLD Boundary](01-core-concepts/lld-vs-hld-boundary.md)
- [Company Question Index](07-company-question-index.md)
- [HLD Prep Guide (sibling)](../System%20Design%20-%20High%20Level%20Design/README.md)
- [Case Studies (sibling)](../Case%20Studies/README.md)
- [React Prep Guide (sibling)](../Frontend%20-%20React/README.md)
- [DSA Patterns Mastery (sibling)](../DSA%20-%20Algorithms/README.md)
- [Learn hub](../README.md)

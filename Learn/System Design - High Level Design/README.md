# Senior SWE HLD Interview Prep Guide

**Target:** 3–5 YOE Full Stack Engineer → Senior Software Engineer (Gen AI / LLM focus)

A modular, interview-ready study system with **105 company-tagged HLD questions**, framework playbooks, memory maps, and spoken answer scripts.

---

## How to Use This Repo

1. **Week 0 (recommended):** Skim [Case Studies Library](../Case%20Studies/README.md) — read [How to Read Case Studies](../Case%20Studies/00-framework/how-to-read-case-studies.md) and one paired example ([Enterprise RAG](../Case%20Studies/paired/CS-PAIR-01-enterprise-rag.md)).
2. **Week 1:** Read [Interview Framework](00-interview-framework/) + [Diagram Playbook](04-diagram-playbook/) — learn *how* to answer any question.
3. **Week 2:** Study [Core Concepts](01-core-concepts/) + memorize [Memory Maps](01-core-concepts/memory-map-master.md).
4. **Weeks 3–5:** Complete [Gen AI / LLM Track](02-genai-llm-hld/) (40 questions) — read **case study first**, then timed question mock.
5. **Weeks 6–8:** Complete [Classic HLD Track](03-classic-hld/) (65 questions) — same case-study-first flow.
6. **Before each interview:** Check [Company Question Index](05-company-question-index.md) for likely questions.

---

## Repository Structure

| Folder | Contents |
|--------|----------|
| [Case Studies](../Case%20Studies/) | **219 end-to-end case studies** (business context → HLD → ops) + 20 paired HLD+LLD narratives |
| [00-interview-framework/](00-interview-framework/) | 7-step flow, diagram rules, narration templates, component picker |
| [01-core-concepts/](01-core-concepts/) | Scalability, caching, DBs, queues, APIs, consistency, security, observability |
| [02-genai-llm-hld/](02-genai-llm-hld/) | Gen AI framework + **40 full question scripts** |
| [03-classic-hld/](03-classic-hld/) | Classic patterns + **65 full question scripts** |
| [04-diagram-playbook/](04-diagram-playbook/) | Standard + Gen AI diagram templates |
| [05-company-question-index.md](05-company-question-index.md) | Company × question lookup |
| [06-study-schedule/](06-study-schedule/) | 8-week day-by-day plan |

---

## Question Count

| Track | Questions | Location |
|-------|-----------|----------|
| Gen AI / LLM | 40 | [02-genai-llm-hld/questions/](02-genai-llm-hld/questions/) |
| Classic HLD | 65 | [03-classic-hld/questions/](03-classic-hld/questions/) |
| **Total** | **105** | |

---

## Per-Question Template

Every question file includes a **Case Study** link at the top, then:

1. Company tags
2. Clarifying questions (with expected answers)
3. Functional & non-functional requirements
4. Capacity estimation
5. HLD diagram (ASCII + Mermaid)
6. Component choices & alternatives
7. Deep dive topics
8. Tradeoffs table
9. Failure modes & degradation
10. **Full interview answer script** (spoken walkthrough)
11. Follow-up questions

---

## Mock Interview Checklist

- [ ] Clarify requirements before drawing (5 min)
- [ ] State MVP scope explicitly
- [ ] Show back-of-envelope math
- [ ] Draw numbered diagram (read path + write path if different)
- [ ] Proactively discuss tradeoffs
- [ ] Mention observability, security, cost
- [ ] Cover failure modes without being prompted

---

## Quick Links

- [Case Studies Index](../Case%20Studies/index.md)
- [Enterprise RAG Case Study (paired)](../Case%20Studies/paired/CS-PAIR-01-enterprise-rag.md)
- [8-Week Study Plan](06-study-schedule/8-week-plan.md)
- [HLD Round Flow](00-interview-framework/01-hld-round-flow.md)
- [How to Draw Diagrams](00-interview-framework/02-how-to-draw-diagrams.md)
- [Gen AI Memory Map](02-genai-llm-hld/memory-map-genai.md)
- [Master Memory Map](01-core-concepts/memory-map-master.md)
- Sibling tracks: [LLD](../System%20Design%20-%20Low%20Level%20Design/README.md) · [Case Studies](../Case%20Studies/README.md) · [React](../Frontend%20-%20React/README.md) · [DSA](../DSA%20-%20Algorithms/README.md) · [Learn hub](../README.md)

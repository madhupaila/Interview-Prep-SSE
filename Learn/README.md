# Senior SWE Interview Prep — Learn

**Target:** 3–5 YOE Full Stack Engineer → **Senior Software Engineer** (Gen AI / LLM focus)

A unified interview preparation library: system design, frontend, DSA, and end-to-end case studies — same learning style across every track (memory maps, company-tagged questions, spoken answer scripts, study schedules).

---

## Tracks

| Track | Focus | Start here |
|-------|--------|------------|
| [System Design — HLD](System%20Design%20-%20High%20Level%20Design/README.md) | 105 distributed-system questions | [8-week plan](System%20Design%20-%20High%20Level%20Design/06-study-schedule/8-week-plan.md) |
| [System Design — LLD](System%20Design%20-%20Low%20Level%20Design/README.md) | 114 OOD / patterns / concurrency / GenAI LLD | [8-week plan](System%20Design%20-%20Low%20Level%20Design/08-study-schedule/8-week-plan.md) |
| [Case Studies](Case%20Studies/README.md) | 219 end-to-end narratives (requirements → HLD → LLD → ops) + 20 paired | [How to read](Case%20Studies/00-framework/how-to-read-case-studies.md) |
| [Frontend — React](Frontend%20-%20React/README.md) | 80 React + GenAI UI questions | [Memory mapping](Frontend%20-%20React/00-interview-framework/05-structured-preparation-and-memory-mapping.md) |
| [DSA — Algorithms](DSA%20-%20Algorithms/README.md) | 24 patterns, 313 Python questions | [90-day plan](DSA%20-%20Algorithms/07-study-schedule/master-90-day-plan.md) |

---

## Recommended Study Order

**Full loop (12–16 weeks):**

1. **Week 0:** [Case Studies](Case%20Studies/README.md) — read one paired doc ([Enterprise RAG](Case%20Studies/paired/CS-PAIR-01-enterprise-rag.md)) to see the full narrative.
2. **Weeks 1–8:** HLD + LLD tracks in parallel with matching case studies before each mock.
3. **Weeks 5–10:** React track (memory maps daily + speak answers aloud).
4. **Weeks 1–12 (ongoing):** DSA Tier A → B → C with pattern drills.

**Interview in 4 weeks:** Pick **one** coding track (DSA Tier-A sprint) + **one** design track (HLD or LLD) + daily React flashcards.

---

## Cross-Track Connections

| If you're studying… | Also read… |
|--------------------|------------|
| HLD RAG (Q02) | [Case Study CS-HLD-G02](Case%20Studies/hld/genai/CS-HLD-G02-rag-document-qa.md) · [LLD RAG Orchestrator](System%20Design%20-%20Low%20Level%20Design/05-genai-llm-lld/questions/Q01-rag-orchestrator.md) · [React Q01 Streaming Chat](Frontend%20-%20React/02-genai-llm-react/questions/Q01-build-streaming-chat-ui.md) |
| LLD Parking Lot | [Case Study CS-LLD-O01](Case%20Studies/lld/classic-ood/CS-LLD-O01-parking-lot.md) · [HLD Q30](System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q30-parking-lot-elevator.md) |
| DSA patterns | Same cue → pattern discipline as React memory zones |

---

## Maintenance

Regenerate bulk content after editing data modules:

```bash
cd "Case Studies" && python _generate_case_studies.py
cd "Frontend - React" && python _generate_react_questions.py
cd "DSA - Algorithms" && python _generate_dsa_questions.py
```

Repair relative links after moving folders:

```bash
cd "Learn" && python _fix_learn_links.py
```

Validate DSA Python solutions:

```bash
cd "DSA - Algorithms" && python _validate_solutions.py
```

---

## Other Resources

- [System Design Handbook (PDF)](System%20Design%20-%20Hand%20Book.pdf) — supplementary reference

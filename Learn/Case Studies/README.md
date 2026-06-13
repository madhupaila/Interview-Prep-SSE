# Case Studies Library

**Target:** 3–5 YOE Full Stack Engineer → Senior Software Engineer (Gen AI / LLM focus)

End-to-end case studies for **219 topics** across HLD and LLD tracks. Each case study walks from **business context** through **requirements, constraints, tradeoffs, HLD, LLD, and operations** — the way real senior engineers ship systems, not just whiteboard them.

---

## What's Inside

| Folder | Count | Description |
|--------|-------|-------------|
| [00-framework/](00-framework/) | 3 | Template, reading guide, industry standards |
| [hld/genai/](hld/genai/) | 40 | GenAI / LLM high-level design case studies |
| [hld/classic/](hld/classic/) | 65 | Classic distributed systems HLD |
| [lld/classic-ood/](lld/classic-ood/) | 64 | Object-oriented design case studies |
| [lld/design-patterns/](lld/design-patterns/) | 25 | GoF pattern case studies |
| [lld/concurrency/](lld/concurrency/) | 15 | Thread-safety case studies |
| [lld/genai/](lld/genai/) | 10 | GenAI object-design case studies |
| [paired/](paired/) | ~20 | Unified HLD + LLD end-to-end narratives |
| [index.md](index.md) | 1 | Master index of all 219 entries |

---

## How to Use

1. **Start here:** [How to Read Case Studies](00-framework/how-to-read-case-studies.md)
2. **GenAI path:** [paired/CS-PAIR-01-enterprise-rag.md](paired/CS-PAIR-01-enterprise-rag.md) → HLD Q02 → LLD Q01
3. **Classic path:** [hld/classic/CS-HLD-C01-url-shortener.md](hld/classic/CS-HLD-C01-url-shortener.md)
4. **OOD path:** [lld/classic-ood/CS-LLD-O01-parking-lot.md](lld/classic-ood/CS-LLD-O01-parking-lot.md)
5. **Timed mock:** Use linked question file after reading case study
6. **Code practice:** [Java implementations](../System%20Design%20-%20Low%20Level%20Design/09-code-implementations/)

---

## Case Study vs Question File

| Case Study | Question File |
|------------|---------------|
| Business context, stakeholders, constraints | Interview-optimized problem statement |
| MoSCoW requirements + measurable NFRs | Clarifying Q&A table |
| ADRs with industry rationale | Tradeoffs table |
| 3-phase implementation roadmap | Capacity estimation |
| SLI/SLO, incident runbooks | Failure modes |
| 30-min full walkthrough | 15-min interview script |

Every question file links to its case study at the top.

---

## Regenerate Content

```bash
cd "Case Studies"
python _generate_case_studies.py          # Generate all case study .md files
python _generate_case_studies.py --index  # Regenerate index.md only
python _link_case_studies.py              # Inject Case Study blocks into question files
```

Gold-standard files (hand-authored, generator skips overwrite unless `--force`):

- `paired/CS-PAIR-01-enterprise-rag.md`
- `hld/classic/CS-HLD-C01-url-shortener.md`
- `lld/classic-ood/CS-LLD-O01-parking-lot.md`

---

## Related Tracks

- [HLD Prep Guide](../System%20Design%20-%20High%20Level%20Design/README.md)
- [LLD Prep Guide](../System%20Design%20-%20Low%20Level%20Design/README.md)
- [LLD vs HLD Boundary](../System%20Design%20-%20Low%20Level%20Design/01-core-concepts/lld-vs-hld-boundary.md)

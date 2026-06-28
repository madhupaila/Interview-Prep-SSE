# Industry Standards Reference

Apply these frameworks when reading or writing case studies. Each case study should explicitly reference at least **3** of the standards below in ADRs, NFR tables, or ops sections.

---

## AWS Well-Architected Framework (6 Pillars)

| Pillar | Apply when | Example in case study |
|--------|------------|----------------------|
| Operational Excellence | All | Runbooks, CI/CD, change management |
| Security | All | IAM, encryption, audit logs |
| Reliability | Distributed systems | Multi-AZ, failover, RPO/RTO |
| Performance Efficiency | High QPS / LLM | Caching, CDN, model routing |
| Cost Optimization | SaaS, GenAI | Reserved capacity, semantic cache |
| Sustainability | Large infra | Region selection, batch vs realtime |

---

## Google SRE — SLI, SLO, Error Budgets

```
SLI = quantified measure of service level
SLO = target value for SLI over a window
Error budget = 1 - SLO (allowed unreliability)
```

**Common SLIs:**

| Service type | SLI | Typical SLO |
|--------------|-----|-------------|
| API | Availability (successful / total) | 99.9% |
| API | Latency p99 | < 200ms (sync), < 8s (RAG) |
| LLM | Faithfulness / citation accuracy | > 95% on eval set |
| Batch pipeline | Freshness (lag) | < 15 min |

**Error budget policy:** When budget exhausted, freeze features; focus on reliability work.

---

## Architecture Decision Records (ADR)

Format (Michael Nygard):

```markdown
### ADR-NNN: Title

**Status:** Proposed | Accepted | Deprecated
**Date:** YYYY-MM-DD
**Context:** Forces at play — requirements, constraints, team skills
**Decision:** What we chose
**Consequences:** Positive and negative outcomes
**Alternatives considered:** Option B, Option C — why rejected
```

Store ADRs in case study Part 5. In production, keep in `docs/adr/` in the repo.

---

## ISO/IEC 25010 — NFR Quality Attributes

| Attribute | Sub-characteristics | Interview signal |
|-----------|---------------------|------------------|
| Performance | Time behavior, capacity | QPS, p99 latency |
| Reliability | Availability, fault tolerance | SLO, failover |
| Security | Confidentiality, integrity | AuthZ, encryption |
| Maintainability | Modularity, testability | SOLID, patterns |
| Portability | Adaptability | Multi-cloud, abstractions |

Map NFR table in Part 3 to ISO 25010 attributes.

---

## OWASP LLM Top 10 (GenAI Case Studies)

| Risk | Mitigation in design |
|------|---------------------|
| LLM01 Prompt injection | Input sanitization, tool sandboxing |
| LLM02 Insecure output | Output guardrails, schema validation |
| LLM03 Training data poisoning | N/A for RAG; vet fine-tune data |
| LLM04 Model DoS | Rate limits, token budgets |
| LLM05 Supply chain | Pin model versions, audit deps |
| LLM06 Sensitive disclosure | ACL on retrieval, PII redaction |
| LLM07 Insecure plugins | Tool registry, least privilege |
| LLM08 Excessive agency | Human-in-loop for destructive actions |
| LLM09 Overreliance | Citations, confidence scores, refuse |
| LLM10 Model theft | API keys, watermarking |

Reference in GenAI HLD/LLD case studies Part 4 (constraints) and Part 10 (security).

---

## 12-Factor App (SaaS / Platform Topics)

1. Codebase — one repo, many deploys  
2. Dependencies — explicit, isolated  
3. Config — env vars, not code  
4. Backing services — attach as resources  
5. Build, release, run — strict separation  
6. Processes — stateless, share-nothing  
7. Port binding — self-contained HTTP  
8. Concurrency — scale via processes  
9. Disposability — fast startup/shutdown  
10. Dev/prod parity  
11. Logs — event streams  
12. Admin processes — one-off tasks  

Apply to multi-tenant SaaS HLD case studies (RAG, API gateway, feature flags).

---

## Real Product References (Use in Part 1)

| Domain | Products to cite |
|--------|------------------|
| URL shortener | Bitly, TinyURL |
| RAG / enterprise search | Glean, Notion AI, Harvey, Coveo |
| Chat / LLM | ChatGPT, Claude, Gemini |
| Code assistant | GitHub Copilot, Cursor, Cody |
| Ride sharing | Uber, Lyft |
| Payments | Stripe, PayPal |
| Streaming | Netflix, Spotify, YouTube |
| Messaging | WhatsApp, Slack, Discord |
| E-commerce | Amazon, Shopify |
| Maps / delivery | Google Maps, DoorDash |

Avoid generic "a company" — name the analog and what they do well.

---

## Related

- [Case Study Template](case-study-template.md)
- [HLD Observability](../../System%20Design%20-%20High%20Level%20Design/01-core-concepts/observability-sre.md)
- [GenAI Evaluation & Safety](../../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/04-evaluation-safety-cost.md)

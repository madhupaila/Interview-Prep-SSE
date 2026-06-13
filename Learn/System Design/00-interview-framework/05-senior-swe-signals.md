# Senior SWE Signals in HLD Interviews

What separates Senior from Mid-level in system design rounds.

---

## Mid-Level vs Senior

| Dimension | Mid-Level | Senior |
|-----------|-----------|--------|
| Scope | Jumps to diagram | Clarifies and bounds MVP |
| Scale | Vague ("millions of users") | Shows math, identifies bottleneck |
| Tradeoffs | Names technologies | Compares options with quantified reasoning |
| Failures | Only if asked | Proactive degradation and DR |
| Ops | Rarely mentioned | Observability, rollout, on-call impact |
| Cost | Ignored | Unit economics, build vs buy |
| Security | Bolt-on mention | Multi-tenancy, auth flow, data isolation |
| Communication | Monologue | Checks in, offers deep-dive choices |

---

## The 10 Senior Signals

### 1. Requirements Engineering
Ask about ambiguous requirements. State assumptions explicitly. Get alignment before designing.

### 2. Prioritization
> "I'll design core flow first; admin analytics is out of scope unless you want it."

### 3. Quantified Decisions
Every major choice tied to a number: QPS, storage, latency, cost per request.

### 4. Evolution Path
> "Monolith first for 3 engineers; extract feed service when it hits 5K QPS."

### 5. Operability
Mention metrics, alerts, runbooks, SLOs without being prompted.

### 6. Failure-First Thinking
Circuit breakers, timeouts, retries with backoff, idempotency keys, DLQ.

### 7. Security & Compliance
PII handling, encryption, audit logs, GDPR deletion — especially for Gen AI.

### 8. Cross-Team Awareness
> "This schema change requires coordination with the billing team's service."

### 9. Build vs Buy
> "We'd use Stripe for payments rather than PCI scope ourselves."

### 10. Interview Facilitation
Guide the conversation: "I can deep-dive on sharding or caching — which is more useful?"

---

## Gen AI Senior Signals

- **Token economics:** Cost per 1K queries, caching embeddings
- **Eval pipeline:** How you measure regression before deploy
- **Grounding:** RAG, citations, confidence thresholds for hallucination
- **Safety:** PII redaction, prompt injection defense, content filters
- **Latency UX:** Streaming tokens, progressive rendering
- **Model lifecycle:** Versioning, rollback, A/B between models

---

## Red Flags That Downlevel You

1. No clarifying questions
2. Single technology answer without alternatives
3. Cannot estimate scale
4. Diagram with no data stores or cache
5. No mention of what breaks
6. Over-engineering (microservices + Kafka for 100 users)
7. Under-engineering (single DB, no replication at 10M DAU)

---

## How to Practice Senior Signals

1. Record yourself doing a 45-min mock
2. Count tradeoff statements — aim for 5+
3. Check: did you mention observability and failure modes unprompted?
4. Peer review: can they follow your diagram without questions?

---

## Phrases to Internalize

- "The bottleneck at this scale is..."
- "I'd accept eventual consistency here because..."
- "For rollout, I'd use feature flags and canary..."
- "If this service fails, the user experience degrades to..."
- "Unit cost at this volume favors..."
- "We need idempotency on this write because retries are inevitable."

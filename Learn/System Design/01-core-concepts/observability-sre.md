# Observability & SRE

## Definition

**Observability** is the ability to understand system internal state from external outputs: metrics, logs, traces.

---

## Three Pillars

| Pillar | Purpose | Tools |
|--------|---------|-------|
| Metrics | Aggregated numbers over time | Prometheus, Datadog |
| Logs | Discrete events | ELK, CloudWatch |
| Traces | Request flow across services | Jaeger, Zipkin |

---

## Key Metrics Frameworks

**RED (services):**
- **R**ate — requests per second
- **E**rrors — error rate
- **D**uration — latency percentiles

**USE (resources):**
- **U**tilization — CPU, memory %
- **S**aturation — queue depth
- **E**rrors — hardware/software errors

---

## SLOs, SLIs, Error Budgets

| Term | Definition |
|------|------------|
| SLI | Metric you measure (p99 latency < 200ms) |
| SLO | Target (99.9% of requests meet SLI) |
| SLA | Contract with penalties |
| Error budget | 100% - SLO — allowed downtime for releases |

> "99.9% availability = 43 min downtime/month — that's our error budget."

---

## Alerting

- Alert on symptoms (user-facing latency), not causes (CPU) when possible
- Reduce alert fatigue — actionable alerts only
- Runbooks linked to alerts

---

## Distributed Tracing

- Propagate trace ID across services (`X-Trace-Id`)
- Identify slow spans in request path
- Critical for microservices debugging

---

## Gen AI Observability

| Metric | Why |
|--------|-----|
| Tokens in/out | Cost tracking |
| Time to first token | UX latency |
| Retrieval recall@k | RAG quality |
| Hallucination rate | Safety (human or LLM-judge eval) |
| Model version | Regression tracking |

---

## Interview Phrases

> "RED metrics per service; p99 latency alert at 500ms."
> "Distributed tracing with OpenTelemetry across all services."
> "SLO 99.95% — error budget gates production deploys."

---

## Memory Map

```
OBSERVABILITY
├── Metrics (RED) | Logs | Traces
├── SLO → error budget → deploy gate
├── Alert on symptoms, link runbooks
├── Trace ID propagated cross-service
└── Gen AI: tokens, TTFT, retrieval quality
```

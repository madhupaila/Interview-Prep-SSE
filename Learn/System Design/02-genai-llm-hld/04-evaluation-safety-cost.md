# Evaluation, Safety & Cost

Production Gen AI requires eval pipelines, safety guardrails, and cost control.

---

## Evaluation Pipeline

```
Offline eval (pre-deploy)          Online eval (post-deploy)
├── Golden dataset               ├── User thumbs up/down
├── Automated metrics            ├── LLM-as-judge sampling
├── Regression vs baseline       ├── A/B test new model
└── Human review queue           └── Alert on metric drop
```

### Metrics

| Metric | How to measure |
|--------|----------------|
| Answer relevance | LLM-judge or human rubric |
| Faithfulness (RAG) | Claims supported by context? |
| Retrieval recall@k | Relevant doc in top-K |
| Latency | TTFT, total time |
| Cost | $/1K queries |
| Safety | Toxicity classifier, policy violations |

---

## LLM-as-Judge

- Use strong model to score weaker model outputs
- Rubric: relevance 1–5, faithfulness yes/no
- Sample 1–5% of production traffic for continuous eval

---

## Safety Guardrails

### Input

- PII detection and redaction
- Prompt injection detection (classifier, delimiter isolation)
- Content policy filter (blocked topics)

### Output

- Toxicity / hate speech filter
- Hallucination check (citation verification for RAG)
- PII leak detection in response

### Architecture

```
Input → InputGuard → LLM → OutputGuard → User
              ↓                    ↓
         block/warn           block/rewrite
```

---

## Prompt Injection Defense

1. Separate system and user content with delimiters
2. Never execute instructions from retrieved documents blindly
3. Input classifier for jailbreak patterns
4. Least-privilege tool permissions

---

## Cost Optimization

| Technique | Savings |
|-----------|---------|
| Model routing (small for easy queries) | 50–70% |
| Semantic cache | 20–40% on repeated/similar |
| Prompt caching (API feature) | 50% on cached prefix |
| Shorter prompts (better retrieval) | Variable |
| Batch embedding on ingest | 10× vs realtime |
| Quantization (INT8/FP8) | 2× throughput self-host |

**Track:** Cost per query, per tenant, per feature.

---

## Compliance

- Audit log: prompt hash, model version, retrieval sources, response
- Data residency: region-specific model endpoints
- Right to deletion: remove user data from vector index
- SOC2/HIPAA: BAA with provider or self-host

---

## Deployment & Rollback

- Model registry with versioned weights
- Canary 5% traffic to new model
- Auto-rollback if faithfulness score drops > 5%
- Feature flags for prompt versions

---

## Interview Phrases

> "Golden set of 500 Q&A pairs — block deploy if faithfulness drops."
> "Input and output guardrails with block vs rewrite policies."
> "Model router cuts cost 60% by sending FAQs to Haiku-class model."

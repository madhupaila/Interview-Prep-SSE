# How to Explain Your HLD in an Interview

Structure your narration so the interviewer can follow without getting lost.

---

## Opening Script

> "Before I start drawing, I'd like to clarify a few requirements to make sure we're aligned on scope."

After clarifying:

> "Great. I'll design the MVP for [core feature], estimate scale, draw the high-level architecture, and then we can deep-dive wherever you'd like."

---

## Transition Phrases

| Moment | What to say |
|--------|-------------|
| After estimates | "At this scale, the main bottleneck will be [X]. I'll address that when we deep-dive." |
| Before diagram | "I'll draw top-down: clients, edge, services, then data layer." |
| Switching diagrams | "The write path is different — let me draw that separately." |
| Starting deep dive | "For the feed read path, the key decision is fan-out on write vs read." |
| Tradeoff | "I considered A and B. A gives [benefit] but costs [downside]. Given our read-heavy workload, I'd pick A." |
| Failure mode | "If [component] fails, we degrade by [behavior] rather than returning 500." |

---

## The PREP Method for Deep Dives

**P**roblem → **R**equirements → **E**xplanation → **P**roof (numbers/tradeoff)

**Example (Twitter feed):**

> **Problem:** Users need a home timeline of tweets from people they follow.
> **Requirements:** p99 < 200ms, 300M DAU, celebrities have 50M followers.
> **Explanation:** Fan-out on write breaks for celebrities, so we hybrid — precompute for normal users, merge on read for celebrities.
> **Proof:** 500 follows × 200 bytes/tweet × 800 tweets cached = 80MB per user — too much for fan-out on write at scale for all users.

---

## Tradeoff Language Templates

### Option comparison

> "There are three approaches: [A], [B], and [C]. [A] optimizes for latency, [B] for cost, [C] for consistency. Given [constraint], I'd start with [choice] and migrate to [other] when [trigger]."

### Cost awareness

> "Self-hosting the LLM saves API cost at > 50M tokens/day but adds GPU ops burden. I'd start with OpenAI API and switch when unit economics justify it."

### Consistency

> "We can accept eventual consistency for the feed — users don't need to see a tweet within 100ms globally. But payment status must be strongly consistent."

---

## Senior Phrases That Land Well

- "I'd instrument this with p99 latency and error rate per service."
- "This endpoint must be idempotent — we use client-generated UUIDs."
- "We need a dead-letter queue for failed fan-out jobs."
- "Multi-tenancy isolation: row-level tenant_id + separate encryption keys."
- "Rollout: feature flag + shadow traffic before full cutover."
- "Backpressure: if the queue depth exceeds threshold, reject new writes with 503."

---

## What NOT to Say

| Avoid | Say instead |
|-------|-------------|
| "We'll just scale it" | "We shard by user_id into 256 partitions" |
| "Use microservices" | "I'd split auth and feed because they scale independently" |
| "Add Kafka" | "Kafka gives us replay and decouples producers from consumers" |
| "It depends" (alone) | "It depends on read/write ratio — here's how I'd decide..." |

---

## Handling "I Don't Know"

> "I haven't designed that exact component, but I'd approach it by [first principles]. I'd also check [AWS docs / similar system] and validate with a load test."

Honesty + structured thinking beats faking expertise.

---

## Closing the Round

> "To summarize: we have [architecture] handling [scale], with [key tradeoffs]. Main risks are [X] and [Y], mitigated by [Z]. Happy to go deeper on any area."

Ask:

> "Is there a specific component you'd like me to expand on?"

---

## Gen AI Specific Narration

- Mention **token budget** and **context window** limits
- Explain **RAG** as "retrieve relevant chunks, then generate with citations"
- Discuss **hallucination** mitigation: grounding, confidence thresholds, human review
- State **model routing**: small model for simple queries, large for complex

See Gen AI questions in [02-genai-llm-hld/questions/](../02-genai-llm-hld/questions/).

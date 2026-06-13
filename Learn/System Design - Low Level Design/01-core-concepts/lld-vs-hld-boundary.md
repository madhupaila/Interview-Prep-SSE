# LLD vs HLD Boundary

Know when to stay in **object design** vs pivot to **distributed systems**.

---

## Quick Decision

| Signal | Round type |
|--------|------------|
| "Design the classes for…" | **LLD** |
| "Design a system for 10M users…" | **HLD** |
| "Object-oriented design of parking lot" | **LLD** |
| "How would you scale globally?" | **HLD** (after LLD MVP) |
| "Write the park() method" | **LLD** |
| "QPS, sharding, cache layer" | **HLD** |

---

## Same Problem, Different Rounds

| Problem | LLD focus | HLD focus |
|---------|-----------|-----------|
| Parking Lot | ParkingLot, Spot, Ticket, Strategy | Multi-site sync, payment API, sensors |
| Rate Limiter | Token bucket class, thread-safe | Redis cluster, per-tenant limits, edge |
| Messenger | User, Chat, Message objects | WebSocket fleet, Cassandra, push |
| LRU Cache | LinkedHashMap / custom DLL | Distributed cache, eviction at scale |
| RAG | Retriever, Generator interfaces | Vector DB, embedding pipeline, GPU |
| Elevator | Elevator, Request, Scheduler algo | Building controller, safety regs, IoT |

---

## Pivot Script

> "At object level I'd model ParkingLot with Strategy for allocation. If we need to support 500 buildings nationwide, I'd add a central registry service, event bus for occupancy sync, and shard by buildingId — happy to go deeper on HLD."

---

## End-to-End Case Studies (Paired HLD + LLD)

Read the **paired case study first** for the full narrative, then drill into individual rounds.

| Topic | Paired case study | HLD question | LLD question |
|-------|-------------------|--------------|--------------|
| Enterprise RAG | [CS-PAIR-01](../../Case%20Studies/paired/CS-PAIR-01-enterprise-rag.md) | [HLD Q02 RAG](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q02-rag-document-qa.md) | [LLD Q01 RAG Orchestrator](../05-genai-llm-lld/questions/Q01-rag-orchestrator.md) |
| Parking Lot at scale | [CS-PAIR-02](../../Case%20Studies/paired/CS-PAIR-02-parking-lot-at-scale.md) | [HLD Q30](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q30-parking-lot-elevator.md) | [LLD Q01 Parking Lot](../02-classic-ood/questions/Q01-parking-lot.md) |
| ChatGPT / memory | [CS-PAIR-03](../../Case%20Studies/paired/CS-PAIR-03-chatgpt-conversational-ai.md) | [HLD Q01 ChatGPT](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q01-design-chatgpt-clone.md) | [LLD Q04 Memory](../05-genai-llm-lld/questions/Q04-conversation-memory-manager.md) |
| Rate-limited API | [CS-PAIR-04](../../Case%20Studies/paired/CS-PAIR-04-rate-limited-api.md) | [HLD Q43](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q43-rate-limited-api-platform.md) | [LLD Q14 Rate Limiter](../02-classic-ood/questions/Q14-rate-limiter.md) |
| WhatsApp messenger | [CS-PAIR-05](../../Case%20Studies/paired/CS-PAIR-05-whatsapp-messenger.md) | [HLD Q04](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q04-whatsapp-messenger.md) | [LLD Q24 Messenger](../02-classic-ood/questions/Q24-messenger-1to1.md) |
| Twitter news feed | [CS-PAIR-06](../../Case%20Studies/paired/CS-PAIR-06-twitter-news-feed.md) | [HLD Q02 Feed](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q02-twitter-feed.md) | [LLD Q43 News Feed](../02-classic-ood/questions/Q43-news-feed-object-model.md) |
| Distributed cache / LRU | [CS-PAIR-07](../../Case%20Studies/paired/CS-PAIR-07-distributed-cache-lru.md) | [HLD Q12 Cache](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q12-distributed-cache.md) | [LLD Q13 LRU](../02-classic-ood/questions/Q13-lru-cache.md) |
| Multi-agent workflow | [CS-PAIR-08](../../Case%20Studies/paired/CS-PAIR-08-multi-agent-workflow.md) | [HLD Q08](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q08-multi-agent-workflow.md) | [LLD Q10 Coordinator](../05-genai-llm-lld/questions/Q10-multi-agent-coordinator.md) |
| Prompt management | [CS-PAIR-09](../../Case%20Studies/paired/CS-PAIR-09-prompt-management.md) | [HLD Q13](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q13-prompt-management.md) | [LLD Q03 Template Engine](../05-genai-llm-lld/questions/Q03-prompt-template-engine.md) |
| LLM API gateway | [CS-PAIR-10](../../Case%20Studies/paired/CS-PAIR-10-llm-api-gateway.md) | [HLD Q05 Gateway](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q05-llm-api-gateway.md) | [LLD Q06 Provider Abstraction](../05-genai-llm-lld/questions/Q06-llm-provider-abstraction.md) |
| Code assistant | [CS-PAIR-11](../../Case%20Studies/paired/CS-PAIR-11-code-assistant-copilot.md) | [HLD Q03 Copilot](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q03-code-assistant-copilot.md) | [LLD Q02 Tool Registry](../05-genai-llm-lld/questions/Q02-agent-tool-registry.md) |
| Uber ride sharing | [CS-PAIR-12](../../Case%20Studies/paired/CS-PAIR-12-uber-ride-sharing.md) | [HLD Q05 Uber](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q05-uber-ride-sharing.md) | [LLD Q21 Ride](../02-classic-ood/questions/Q21-ride-sharing-uber.md) |
| Notification system | [CS-PAIR-13](../../Case%20Studies/paired/CS-PAIR-13-notification-system.md) | [HLD Q14](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q14-notification-system.md) | [LLD Q25](../02-classic-ood/questions/Q25-notification-system.md) |
| Online judge | [CS-PAIR-14](../../Case%20Studies/paired/CS-PAIR-14-online-judge.md) | [HLD Q29 LeetCode](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q29-online-judge-leetcode.md) | [LLD Q61](../02-classic-ood/questions/Q61-online-judge.md) |
| LLM evaluation | [CS-PAIR-15](../../Case%20Studies/paired/CS-PAIR-15-llm-evaluation.md) | [HLD Q14 Eval](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q14-llm-evaluation-platform.md) | [LLD Q07 Pipeline](../05-genai-llm-lld/questions/Q07-evaluation-pipeline.md) |
| Content moderation | [CS-PAIR-16](../../Case%20Studies/paired/CS-PAIR-16-content-moderation-llm.md) | [HLD Q15](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q15-content-moderation-llm.md) | [LLD Q08 Guardrails](../05-genai-llm-lld/questions/Q08-guardrail-safety-chain.md) |
| Streaming LLM | [CS-PAIR-17](../../Case%20Studies/paired/CS-PAIR-17-streaming-llm.md) | [HLD Q02 RAG](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q02-rag-document-qa.md) | [LLD Q09 Streaming](../05-genai-llm-lld/questions/Q09-streaming-response-aggregator.md) |
| Distributed rate limiter | [CS-PAIR-18](../../Case%20Studies/paired/CS-PAIR-18-distributed-rate-limiter.md) | [HLD Q11](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q11-distributed-rate-limiter.md) | [LLD Q08 Concurrent](../04-concurrency-lld/questions/Q08-rate-limiter-concurrent.md) |
| Web crawler | [CS-PAIR-19](../../Case%20Studies/paired/CS-PAIR-19-web-crawler.md) | [HLD Q09 Crawler](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q09-web-crawler.md) | [LLD Q11 Multithreaded](../04-concurrency-lld/questions/Q11-web-crawler-multithreaded.md) |
| Token budget / cost | [CS-PAIR-20](../../Case%20Studies/paired/CS-PAIR-20-token-budget-cost.md) | [HLD Q34 Routing](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q34-cost-optimized-llm-routing.md) | [LLD Q05 Token Budget](../05-genai-llm-lld/questions/Q05-token-budget-manager.md) |

**Full index:** [Case Studies index.md](../../Case%20Studies/index.md)

---

## Cross-Links to HLD Guide (Quick Reference)

| LLD Question | HLD Counterpart |
|--------------|-----------------|
| Rate Limiter | [HLD Q43 Rate-Limited API](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q43-rate-limited-api-platform.md) |
| LRU Cache | [HLD Caching](../System%20Design%20-%20High%20Level%20Design/01-core-concepts/caching.md) |
| 1:1 Messenger | [HLD Q04 WhatsApp](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q04-whatsapp-messenger.md) |
| Parking Lot / Elevator | [HLD Q30](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q30-parking-lot-elevator.md) |
| RAG Orchestrator | [HLD Q02 RAG](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q02-rag-document-qa.md) |
| News Feed (objects) | [HLD Q02 Twitter Feed](../System%20Design%20-%20High%20Level%20Design/03-classic-hld/questions/Q02-twitter-feed.md) |

---

## Related

- [Case Studies README](../../Case%20Studies/README.md)
- [How to Read Case Studies](../../Case%20Studies/00-framework/how-to-read-case-studies.md)
- [HLD Prep Guide README](../System%20Design%20-%20High%20Level%20Design/README.md)
- [LLD Round Flow](../00-interview-framework/01-lld-round-flow.md)

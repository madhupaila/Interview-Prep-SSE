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

## Cross-Links to HLD Guide

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

- [HLD Prep Guide README](../System%20Design%20-%20High%20Level%20Design/README.md)
- [LLD Round Flow](../00-interview-framework/01-lld-round-flow.md)

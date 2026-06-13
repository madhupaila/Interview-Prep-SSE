# How to Draw HLD Diagrams

A clear diagram is half the interview. Follow these rules for whiteboard, Excalidraw, or virtual boards.

---

## Standard Layout (Top → Bottom)

```
                    ┌─────────────┐
                    │   Clients   │
                    │ Web / Mobile│
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │  CDN / DNS  │
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │Load Balancer│
                    └──────┬──────┘
                           │
                    ┌──────▼──────┐
                    │ API Gateway │
                    └──────┬──────┘
                           │
         ┌─────────────────┼─────────────────┐
         │                 │                 │
    ┌────▼────┐      ┌─────▼─────┐    ┌─────▼─────┐
    │Service A│      │ Service B │    │ Service C │
    └────┬────┘      └─────┬─────┘    └─────┬─────┘
         │                 │                 │
         └────────┬────────┴────────┬────────┘
                  │                 │
           ┌──────▼──────┐   ┌──────▼──────┐
           │    Redis    │   │  PostgreSQL │
           │   (cache)   │   │  (primary)  │
           └─────────────┘   └──────┬──────┘
                                    │
                              ┌─────▼─────┐
                              │  Replica  │
                              └───────────┘

         ┌─────────────┐
         │    Kafka    │ ─ ─ ─ ▶ ┌─────────────┐
         │   (queue)   │         │   Workers   │
         └─────────────┘         └─────────────┘
              (dashed = async)
```

---

## Symbols Convention

| Shape | Meaning | Examples |
|-------|---------|----------|
| Rectangle | Service / component | UserService, FeedService |
| Cylinder | Database / storage | Postgres, S3, Redis |
| Cloud | External API | Stripe, OpenAI API |
| Hexagon | Gateway / proxy | API Gateway, LLM Gateway |
| Dashed arrow | Async / event | Kafka publish, webhook |
| Solid arrow | Sync request | HTTP, gRPC |

---

## Numbered Flow (Always)

Label the hot path ① ② ③ so you can narrate:

```
User ①→ API Gateway ②→ Feed Service ③→ Redis (cache hit) → return
                              │
                              └── cache miss ④→ DB ⑤→ populate cache
```

---

## When to Draw Multiple Diagrams

| Scenario | Diagrams needed |
|----------|-----------------|
| Read ≠ write path | Separate read + write |
| Batch + real-time | Online path + offline pipeline |
| Gen AI / RAG | Ingestion pipeline + query path |
| Multi-region | Per-region + global routing |

**Say aloud:** "Let me draw the write path first, then the read path — they're different."

---

## Gen AI Layer (Add After API Gateway)

```
┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ Doc      │───▶│ Chunker  │───▶│ Embedder │───▶│ VectorDB │
│ Ingestion│    │          │    │ Service  │    │          │
└──────────┘    └──────────┘    └──────────┘    └────┬─────┘
                                                     │
User Query ──▶ API ──▶ Retriever ──▶ Reranker ──▶ LLM Gateway ──▶ Response
                          ▲              │
                          └──── VectorDB ┘
```

---

## Diagram Anti-Patterns

| Bad | Good |
|-----|------|
| 20 boxes, no grouping | Group by layer (edge, app, data) |
| Unlabeled arrows | Label: `GET /feed`, `gRPC` |
| One giant diagram | 2–3 focused diagrams |
| Missing cache/queue | Show async and cache explicitly |
| DB drawn as box | Use cylinder for storage |

---

## Narration While Drawing

1. **Start with users** — "Users hit our system from mobile and web..."
2. **Add edge** — "Traffic goes through CDN for static assets..."
3. **Core services** — "I'll split into three services: auth, feed, and media..."
4. **Data layer** — "Hot data in Redis, durable store in Postgres..."
5. **Async** — "Writes also publish to Kafka for fan-out workers..."

Draw slowly enough to explain each box as you add it.

---

## Whiteboard Tips

- Leave space on the right for deep-dive expansions
- Use consistent box sizes per layer
- Erase and redraw rather than cluttering corrections
- Put estimates (QPS, storage) in a corner box

---

## Tools

| Tool | Best for |
|------|----------|
| Excalidraw | Practice, clean diagrams |
| draw.io | Complex multi-page |
| Virtual whiteboard (Coderpad, HackerRank) | Live interviews |
| Paper | Mock practice |

See [04-diagram-playbook/](../04-diagram-playbook/) for copy-paste templates.

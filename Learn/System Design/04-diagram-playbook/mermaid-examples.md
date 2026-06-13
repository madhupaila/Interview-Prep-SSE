# Mermaid Diagram Examples

Ready-to-use Mermaid diagrams for practice and interviews.

---

## Classic: URL Shortener

```mermaid
flowchart LR
  User[User] --> LB[LoadBalancer]
  LB --> API[ShortenerAPI]
  API --> Cache[Redis]
  API --> DB[(PostgreSQL)]
  API --> KC[KeyCounterService]
```

---

## Classic: Twitter Feed (Fan-out)

```mermaid
flowchart TB
  Write[PostTweet] --> TweetDB[(TweetDB)]
  TweetDB --> Kafka[Kafka]
  Kafka --> Fanout[FanoutWorkers]
  Fanout --> TimelineCache[RedisTimelines]
  Read[GetFeed] --> API[FeedAPI]
  API --> TimelineCache
```

---

## Classic: Uber Matching

```mermaid
flowchart TB
  Rider[RiderApp] --> API[RideAPI]
  Driver[DriverApp] --> API
  API --> Match[MatchingService]
  Match --> Geo[GeoIndexRedis]
  Match --> TripDB[(TripDB)]
  API --> Notify[NotificationService]
```

---

## Classic: Chat System

```mermaid
flowchart TB
  Client[Client] --> WS[WebSocketGateway]
  WS --> ChatSvc[ChatService]
  ChatSvc --> MQ[Kafka]
  ChatSvc --> MsgDB[(Cassandra)]
  MQ --> Push[PushWorkers]
  Push --> WS
```

---

## Gen AI: RAG System

```mermaid
flowchart TB
  subgraph ingest [Ingestion]
    S3[S3] --> Parser[Parser]
    Parser --> Chunk[Chunker]
    Chunk --> Embed[Embedder]
    Embed --> VDB[(VectorDB)]
  end
  subgraph query [Query]
    User[User] --> GW[APIGateway]
    GW --> Ret[Retriever]
    Ret --> VDB
    Ret --> Rank[Reranker]
    Rank --> LLM[LLMGateway]
    LLM --> Out[Guardrails]
    Out --> User
  end
```

---

## Gen AI: LLM API Gateway

```mermaid
flowchart LR
  Client[Client] --> GW[LLMGateway]
  GW --> Router[ModelRouter]
  Router --> Small[SmallModel]
  Router --> Large[LargeModel]
  GW --> Cache[SemanticCache]
  GW --> RL[RateLimiter]
  GW --> Obs[Metrics]
```

---

## Gen AI: Multi-Agent Platform

```mermaid
flowchart TB
  User[User] --> Orch[Orchestrator]
  Orch --> AgentA[ResearchAgent]
  Orch --> AgentB[WriterAgent]
  AgentA --> Tools[ToolRegistry]
  AgentB --> Tools
  Tools --> LLM[LLMGateway]
  Orch --> State[(StateStore)]
```

---

## Distributed: Rate Limiter

```mermaid
flowchart LR
  Client[Client] --> GW[APIGateway]
  GW --> RL[RateLimiterRedis]
  RL -->|allowed| Svc[BackendService]
  RL -->|429| Client
```

---

## Notes for Live Interviews

- Many virtual whiteboards support Mermaid; if not, redraw as boxes
- Keep diagrams under 12 nodes for clarity
- Use subgraphs to group layers

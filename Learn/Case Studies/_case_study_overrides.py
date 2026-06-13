"""Per-topic case study overrides: industry analogs, business context, ADRs, constraints."""

from __future__ import annotations

# slug -> override dict (merged with defaults in get_override)

INDUSTRY_ANALOGS: dict[str, str] = {
    "rag-document-qa": "Glean and Notion AI — enterprise knowledge search with grounded answers",
    "design-chatgpt-clone": "ChatGPT / Claude — conversational AI with memory and tool use",
    "code-assistant-copilot": "GitHub Copilot and Cursor — inline code completion and chat",
    "url-shortener": "Bitly — link shortening, analytics, and branded domains",
    "twitter-feed": "Twitter/X and LinkedIn feed — fan-out on write vs read",
    "whatsapp-messenger": "WhatsApp and iMessage — 1:1 messaging at billions scale",
    "uber-ride-sharing": "Uber and Lyft — real-time matching and trip lifecycle",
    "parking-lot": "SP+ and ParkMobile — multi-garage occupancy and payments",
    "parking-lot-elevator": "Otis elevator dispatch and smart parking platforms",
    "rate-limited-api-platform": "Stripe and Cloudflare — API rate limits and abuse protection",
    "rate-limiter": "Stripe rate limiter and Envoy local rate limit",
    "lru-cache": "Redis and Memcached — in-process cache vs distributed cache",
    "distributed-cache": "Amazon ElastiCache and Redis Cluster",
    "llm-api-gateway": "OpenAI API and Azure OpenAI — model routing and quotas",
    "rag-orchestrator": "LangChain / LlamaIndex RAG pipeline — retrieve, rerank, generate",
    "multi-agent-workflow": "Microsoft AutoGen and CrewAI — multi-agent orchestration",
    "notification-system": "Twilio and Firebase Cloud Messaging",
    "netflix-video-streaming": "Netflix Open Connect CDN and adaptive bitrate",
    "payment-system-stripe": "Stripe Payment Intents and idempotent APIs",
    "search-engine": "Google Search — crawl, index, rank, serve",
    "google-docs-collab": "Google Docs OT/CRDT operational transform",
    "feature-flag-system": "LaunchDarkly and Split.io",
    "distributed-tracing": "Jaeger and Datadog APM",
    "ecommerce-amazon": "Amazon catalog, cart, and checkout",
    "slack-team-chat": "Slack channels, threads, and search",
    "spotify-streaming": "Spotify recommendation and streaming",
    "youtube": "YouTube upload, transcode, and CDN delivery",
    "dropbox-file-storage": "Dropbox block sync and deduplication",
    "airbnb-search-booking": "Airbnb search ranking and booking flow",
    "online-judge-leetcode": "LeetCode judge workers and sandbox",
    "online-judge": "LeetCode — submit, compile, run, verdict",
    "web-crawler": "Googlebot crawl frontier and politeness",
    "web-crawler-multithreaded": "Googlebot — parallel fetch with URL frontier",
    "embedding-service-scale": "OpenAI embeddings API and Cohere embed",
    "prompt-management": "LangSmith and Humanloop — prompt versioning",
    "prompt-template-engine": "Jinja2-style prompt templates with variables",
    "conversation-memory-manager": "ChatGPT conversation history and summarization",
    "token-budget-manager": "OpenAI token counting and context window limits",
    "llm-provider-abstraction": "LiteLLM — unified provider interface",
    "evaluation-pipeline": "OpenAI evals and HuggingFace Evaluate",
    "guardrail-safety-chain": "Anthropic Constitutional AI and OpenAI moderation",
    "streaming-response-aggregator": "ChatGPT SSE streaming and token aggregation",
    "multi-agent-coordinator": "CrewAI task delegation between agents",
    "agent-tool-registry": "OpenAI function calling and tool schemas",
    "cost-optimized-llm-routing": "Martian and OpenRouter — model routing by cost/latency",
    "hallucination-detection": "RAGAS faithfulness metrics and NLI verification",
    "pdf-citation-rag": "Harvey AI legal RAG with precise citations",
    "medical-qa-compliance": "Epic + LLM with HIPAA audit trails",
    "legal-contract-analysis": "Harvey and Ironclad — contract clause extraction",
    "food-delivery-doordash": "DoorDash dispatch and ETA prediction",
    "stock-trading": "Robinhood and NASDAQ matching engine patterns",
    "cdn-design": "CloudFront and Akamai edge caching",
    "api-gateway": "Kong and AWS API Gateway",
    "logging-system": "Splunk and ELK stack ingestion",
    "metrics-monitoring": "Datadog and Prometheus/Grafana",
    "identity-sso": "Okta and Auth0 OIDC/SAML",
    "multi-tenant-saas": "Salesforce org isolation and row-level security",
    "ab-testing-platform": "Optimizely and Google Experimentation",
    "data-pipeline-etl": "Airflow and dbt batch pipelines",
    "pastebin": "Pastebin and GitHub Gist — text share with TTL",
    "pastebin-ood": "Pastebin object model — paste, expiry, visibility",
    "instagram-photo-sharing": "Instagram feed and media CDN",
    "linkedin-connections": "LinkedIn BFS connection suggestions",
    "ticketmaster-booking": "Ticketmaster seat locking and inventory",
    "hotel-reservation": "Booking.com availability and overbooking",
    "yelp-nearby-places": "Yelp geo search and reviews",
    "map-routing": "Google Maps routing and traffic-aware ETA",
    "zoom-video-conferencing": "Zoom SFU/MCU and signaling",
    "email-service": "Gmail SMTP ingestion and storage",
    "distributed-job-scheduler": "Airflow and Quartz distributed scheduling",
    "distributed-lock": "Chubby/ZooKeeper and Redis Redlock",
    "configuration-service": "Netflix Archaius and Spring Cloud Config",
    "bloom-filter-service": "Chrome Safe Browsing and Cassandra BF",
    "consistent-hashing-ring": "Dynamo and Cassandra token ring",
    "iot-device-platform": "AWS IoT Core device shadow",
    "leaderboard-gaming": "Redis sorted sets for real-time ranks",
    "typeahead-autocomplete": "Google search suggest and Trie prefix index",
    "news-aggregator": "Google News and Apple News ranking",
    "ad-click-aggregator": "Google Ads real-time click aggregation",
    "web-analytics": "Google Analytics event pipeline",
    "subscription-billing": "Stripe Billing and dunning",
    "backup-disaster-recovery": "AWS Backup cross-region RPO/RTO",
    "fraud-detection-rules-ml": "Stripe Radar rules + ML scoring",
    "fraud-detection-llm": "PayPal LLM feature extraction for fraud",
    "rule-based-chatbot": "Dialogflow pre-LLM intent matching",
    "meme-viral-content": "Imgur viral ranking and CDN",
    "global-chat-translation": "WhatsApp real-time message translation",
    "live-sports-cdn": "ESPN low-latency live streaming",
    "realtime-analytics-dashboard": "Grafana live metrics and Flink windows",
    "tinder-dating": "Tinder geo sharding and swipe queue",
    "reddit-forum": "Reddit post ranking and moderation",
    "strategy-payment": "Stripe multi-gateway payment routing",
    "command-undo-redo": "Photoshop and Google Docs undo stack",
    "observer-stock-ticker": "Bloomberg real-time price feeds",
    "state-vending-machine": "Automated retail state machines",
    "producer-consumer": "Kafka consumer groups pattern",
    "concurrent-lru-cache": "Caffeine cache concurrent eviction",
    "thread-pool-executor": "Java ExecutorService and ForkJoinPool",
    "bank-transfer-deadlock": "Banking transfer ordering to prevent deadlock",
    "dining-philosophers": "Classic concurrency problem — resource ordering",
    "download-manager": "Internet Download Manager parallel chunks",
    "job-scheduler-pool": "Sidekiq and Celery worker pools",
    "elevator": "Otis elevator group dispatch algorithms",
    "vending-machine": "Automated retail inventory and change",
    "atm": "NCR ATM transaction and cash dispensing",
    "chess": "Chess.com game engine and move validation",
    "shopping-cart": "Amazon cart and checkout session",
    "messenger-1to1": "WhatsApp message delivery states",
    "news-feed-object-model": "Facebook News Feed object graph",
    "ride-sharing-uber": "Uber trip state machine and matching",
    "splitwise": "Splitwise balance simplification graph",
    "movie-ticket-booking": "BookMyShow seat lock and payment",
    "library-management": "OCLC library catalog systems",
    "hotel-booking": "Booking.com reservation engine",
    "restaurant-food-ordering": "Toast POS kitchen display",
    "digital-wallet": "PayPal wallet and ledger",
    "config-manager": "Netflix Archaius dynamic config",
    "cache-aside-ood": "Redis cache-aside at object level",
}

OVERRIDES: dict[str, dict] = {
    "rag-document-qa": {
        "industry_analog": INDUSTRY_ANALOGS["rag-document-qa"],
        "business_context": (
            "**Industry analog:** Glean and Notion AI — employees search internal docs with AI-generated answers.\n\n"
            "Acme Corp (fictional enterprise) has 10K B2B tenants, 10M documents, and 50M queries/day. "
            "Legal and compliance require **citations on every answer** and **zero cross-tenant data leaks**. "
            "The product team must ship MVP in 8 weeks with a team of 4 engineers.\n\n"
            "**Why now:** GenAI made semantic search accessible, but enterprises won't adopt without ACL-aware retrieval "
            "and hallucination controls.\n\n"
            "**Success:** p99 query latency < 8s, citation accuracy > 95%, SOC2 Type II within 12 months."
        ),
        "constraints": [
            ("Budget", "$80K/mo infra + $120K/mo LLM API at scale", "Semantic cache + model routing"),
            ("Team", "2 backend, 1 ML, 1 infra", "Buy Pinecone; build orchestration"),
            ("Timeline", "MVP 8 weeks", "English only; 3 connector types"),
            ("Compliance", "SOC2, GDPR delete within 24h", "Audit log on every query"),
            ("Hallucination", "Near-zero tolerance", "Citation validator + refuse path"),
        ],
        "adrs": [
            {
                "id": "001", "title": "Vector store at 100M chunks",
                "context": "100M vectors × 1536 dims ≈ 600 GB; need hybrid search.",
                "decision": "Pinecone managed + Elasticsearch BM25 with reciprocal rank fusion.",
                "consequences": "Vendor cost; ops simplicity; proven at scale.",
                "alternatives": "pgvector — rejected above 30M vectors per index.",
            },
            {
                "id": "002", "title": "ACL enforcement point",
                "context": "Users must never retrieve unauthorized chunks.",
                "decision": "Metadata filter in vector DB query before ranking — never post-filter only.",
                "consequences": "Slightly slower queries; security invariant testable in CI.",
                "alternatives": "Post-filter after retrieval — rejected (leak risk + wasted compute).",
            },
            {
                "id": "003", "title": "Answer format",
                "context": "Need machine-verifiable citations.",
                "decision": "Structured JSON: `{answer, citations[]}` + NLI faithfulness check.",
                "consequences": "Easier validation; slightly higher latency.",
                "alternatives": "Free text — rejected for enterprise compliance.",
            },
        ],
        "fr_must": [
            ("Document upload + Drive/Confluence sync", "E2E ingest → query in staging"),
            ("Q&A with page-level citations", "Eval set faithfulness > 95%"),
            ("Tenant admin + usage dashboard", "Admin can view audit log"),
            ("GDPR delete purges vectors in 24h", "Integration test confirms zero chunks"),
        ],
        "nfr_table": [
            ("Latency", "p99 < 8s end-to-end query", "Distributed tracing"),
            ("Availability", "99.9%", "Monthly error budget"),
            ("Isolation", "Zero cross-tenant retrieval in pen test", "Security CI suite"),
            ("Ingestion lag", "< 15 min for connector updates", "Pipeline lag metric"),
        ],
        "incident": (
            "**Scenario:** Retrieval returns empty for known-good documents.\n\n"
            "1. Check embedding model version drift vs index\n"
            "2. Verify ACL filter not over-restrictive for user groups\n"
            "3. Compare BM25 vs vector recall on failing queries\n"
            "4. Roll back recent chunking config change if regression"
        ),
    },
    "url-shortener": {
        "industry_analog": INDUSTRY_ANALOGS["url-shortener"],
        "business_context": (
            "**Industry analog:** Bitly — URL shortening for marketing campaigns with click analytics.\n\n"
            "Marketing teams share 100M new links/day; redirects hit 10B/day (100:1 read-heavy). "
            "Peak redirect QPS ~350K requires CDN + Redis. Product also wants custom aliases for enterprise tier.\n\n"
            "**Success:** Sub-50ms p99 redirect (cache hit), 99.99% redirect availability, analytics lag < 1 min."
        ),
        "constraints": [
            ("Read QPS", "350K peak redirects", "CDN + Redis mandatory"),
            ("Storage", "~180 TB over 10 years", "Shard Postgres by code hash"),
            ("Abuse", "Malware links damage brand", "Async scan + blocklist"),
            ("ID uniqueness", "Global collision-free", "Counter + base62 or hash+retry"),
        ],
        "adrs": [
            {
                "id": "001", "title": "ID generation",
                "context": "100M creates/day; must be unique globally.",
                "decision": "Distributed counter ranges per shard + base62 encode.",
                "consequences": "Ordered IDs; counter service is critical path.",
                "alternatives": "Hash+retry — viable; mention in interview for distributed writes.",
            },
            {
                "id": "002", "title": "Redirect HTTP code",
                "context": "SEO and browser caching behavior.",
                "decision": "HTTP 301 permanent redirect.",
                "consequences": "Browsers cache; good for static short links.",
                "alternatives": "302 — for links that change destination frequently.",
            },
        ],
    },
    "parking-lot": {
        "industry_analog": INDUSTRY_ANALOGS["parking-lot"],
        "business_context": (
            "**Industry analog:** ParkMobile / SP+ — mobile parking with garage occupancy.\n\n"
            "Design the **in-process object model** for a multi-floor garage: motorcycles, cars, trucks; "
            "multiple entry gates concurrent; ticket on entry, payment on exit.\n\n"
            "**Success:** Correct spot assignment, thread-safe concurrent gates, extensible allocation policy."
        ),
        "constraints": [
            ("Scope", "Single building, in-memory MVP", "No distributed registry in LLD round"),
            ("Concurrency", "Multiple entry gates", "Sync per spot, not whole lot"),
            ("Extensibility", "New spot types (EV charging) later", "Strategy + Open-Closed"),
        ],
        "scale_projection": (
            "| Scale signal | HLD addition |\n|--------------|-------------|\n"
            "| 500 garages nationwide | Central registry service + Redis occupancy |\n"
            "| Real-time availability app | WebSocket fan-out from occupancy events |\n"
            "| Sensor-based spots | IoT ingestion → event bus → update spot state |"
        ),
        "adrs": [
            {
                "id": "001", "title": "Spot allocation",
                "context": "Multiple policies: nearest, cheapest, largest-first.",
                "decision": "Strategy pattern — `ParkingStrategy` interface.",
                "consequences": "Test policies in isolation; inject at construction.",
                "alternatives": "if/else in service — rejected when 2+ policies.",
            },
            {
                "id": "002", "title": "Concurrency granularity",
                "context": "Multiple gates park/unpark simultaneously.",
                "decision": "Synchronize on `ParkingSpot` during assign/vacate.",
                "consequences": "Finer than lot-level lock; avoids unnecessary blocking.",
                "alternatives": "Synchronize whole lot — simpler but lower throughput.",
            },
        ],
    },
    "rag-orchestrator": {
        "industry_analog": INDUSTRY_ANALOGS["rag-orchestrator"],
        "business_context": (
            "**Industry analog:** LangChain/LlamaIndex in-process RAG pipeline.\n\n"
            "Design the **object model** for retrieve → rerank → assemble context → generate. "
            "Vector DB and LLM API are external (HLD). Focus on SOLID, testability, and swappable components."
        ),
    },
    "design-chatgpt-clone": {
        "industry_analog": INDUSTRY_ANALOGS["design-chatgpt-clone"],
        "business_context": (
            "**Industry analog:** ChatGPT — conversational UI with streaming, memory, and optional tools.\n\n"
            "100M MAU, billions of messages, streaming tokens via SSE, multi-model routing, content moderation."
        ),
    },
    "rate-limiter": {
        "industry_analog": INDUSTRY_ANALOGS["rate-limiter"],
    },
    "rate-limited-api-platform": {
        "industry_analog": INDUSTRY_ANALOGS["rate-limited-api-platform"],
    },
    "messenger-1to1": {
        "industry_analog": INDUSTRY_ANALOGS["messenger-1to1"],
    },
    "whatsapp-messenger": {
        "industry_analog": INDUSTRY_ANALOGS["whatsapp-messenger"],
    },
}


def get_override(slug: str, kind: str, title: str) -> dict:
    """Return merged override dict for a topic."""
    base: dict = {}
    if slug in OVERRIDES:
        base.update(OVERRIDES[slug])
    elif slug.replace("-", "_") in OVERRIDES:
        base.update(OVERRIDES[slug.replace("-", "_")])

    if "industry_analog" not in base and slug in INDUSTRY_ANALOGS:
        base["industry_analog"] = INDUSTRY_ANALOGS[slug]

    # Try partial slug match
    if "industry_analog" not in base:
        for k, v in INDUSTRY_ANALOGS.items():
            if k in slug or slug in k:
                base["industry_analog"] = v
                break

    if "industry_analog" not in base:
        base["industry_analog"] = f"Leading products in the {title} domain"

    return base

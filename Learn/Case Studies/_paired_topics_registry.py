"""HLD ↔ LLD paired topics registry for unified case studies."""

from __future__ import annotations

PAIRED_TOPICS: list[dict] = [
    {
        "id": "01",
        "slug": "enterprise-rag",
        "title": "Enterprise RAG Document Q&A",
        "hld": {"track": "genai", "num": 2, "file": "Q02-rag-document-qa.md"},
        "lld": {"track": "genai", "num": 1, "file": "Q01-rag-orchestrator.md"},
    },
    {
        "id": "02",
        "slug": "parking-lot-at-scale",
        "title": "Parking Lot at Scale",
        "hld": {"track": "classic", "num": 30, "file": "Q30-parking-lot-elevator.md"},
        "lld": {"track": "classic-ood", "num": 1, "file": "Q01-parking-lot.md"},
    },
    {
        "id": "03",
        "slug": "chatgpt-conversational-ai",
        "title": "ChatGPT-like Conversational AI",
        "hld": {"track": "genai", "num": 1, "file": "Q01-design-chatgpt-clone.md"},
        "lld": {"track": "genai", "num": 4, "file": "Q04-conversation-memory-manager.md"},
    },
    {
        "id": "04",
        "slug": "rate-limited-api",
        "title": "Rate-Limited API Platform",
        "hld": {"track": "classic", "num": 43, "file": "Q43-rate-limited-api-platform.md"},
        "lld": {"track": "classic-ood", "num": 14, "file": "Q14-rate-limiter.md"},
    },
    {
        "id": "05",
        "slug": "whatsapp-messenger",
        "title": "WhatsApp / 1:1 Messenger",
        "hld": {"track": "classic", "num": 4, "file": "Q04-whatsapp-messenger.md"},
        "lld": {"track": "classic-ood", "num": 24, "file": "Q24-messenger-1to1.md"},
    },
    {
        "id": "06",
        "slug": "twitter-news-feed",
        "title": "Twitter News Feed",
        "hld": {"track": "classic", "num": 2, "file": "Q02-twitter-feed.md"},
        "lld": {"track": "classic-ood", "num": 43, "file": "Q43-news-feed-object-model.md"},
    },
    {
        "id": "07",
        "slug": "distributed-cache-lru",
        "title": "Distributed Cache / LRU",
        "hld": {"track": "classic", "num": 12, "file": "Q12-distributed-cache.md"},
        "lld": {"track": "classic-ood", "num": 13, "file": "Q13-lru-cache.md"},
    },
    {
        "id": "08",
        "slug": "multi-agent-workflow",
        "title": "Multi-Agent Workflow Platform",
        "hld": {"track": "genai", "num": 8, "file": "Q08-multi-agent-workflow.md"},
        "lld": {"track": "genai", "num": 10, "file": "Q10-multi-agent-coordinator.md"},
    },
    {
        "id": "09",
        "slug": "prompt-management",
        "title": "Prompt Management & Versioning",
        "hld": {"track": "genai", "num": 13, "file": "Q13-prompt-management.md"},
        "lld": {"track": "genai", "num": 3, "file": "Q03-prompt-template-engine.md"},
    },
    {
        "id": "10",
        "slug": "llm-api-gateway",
        "title": "LLM API Gateway / Model Router",
        "hld": {"track": "genai", "num": 5, "file": "Q05-llm-api-gateway.md"},
        "lld": {"track": "genai", "num": 6, "file": "Q06-llm-provider-abstraction.md"},
    },
    {
        "id": "11",
        "slug": "code-assistant-copilot",
        "title": "Code Assistant (Copilot-like)",
        "hld": {"track": "genai", "num": 3, "file": "Q03-code-assistant-copilot.md"},
        "lld": {"track": "genai", "num": 2, "file": "Q02-agent-tool-registry.md"},
    },
    {
        "id": "12",
        "slug": "uber-ride-sharing",
        "title": "Uber Ride Sharing",
        "hld": {"track": "classic", "num": 5, "file": "Q05-uber-ride-sharing.md"},
        "lld": {"track": "classic-ood", "num": 21, "file": "Q21-ride-sharing-uber.md"},
    },
    {
        "id": "13",
        "slug": "notification-system",
        "title": "Notification System",
        "hld": {"track": "classic", "num": 14, "file": "Q14-notification-system.md"},
        "lld": {"track": "classic-ood", "num": 25, "file": "Q25-notification-system.md"},
    },
    {
        "id": "14",
        "slug": "online-judge",
        "title": "Online Judge (LeetCode)",
        "hld": {"track": "classic", "num": 29, "file": "Q29-online-judge-leetcode.md"},
        "lld": {"track": "classic-ood", "num": 61, "file": "Q61-online-judge.md"},
    },
    {
        "id": "15",
        "slug": "llm-evaluation",
        "title": "LLM Evaluation Platform",
        "hld": {"track": "genai", "num": 14, "file": "Q14-llm-evaluation-platform.md"},
        "lld": {"track": "genai", "num": 7, "file": "Q07-evaluation-pipeline.md"},
    },
    {
        "id": "16",
        "slug": "content-moderation-llm",
        "title": "Content Moderation for LLM Apps",
        "hld": {"track": "genai", "num": 15, "file": "Q15-content-moderation-llm.md"},
        "lld": {"track": "genai", "num": 8, "file": "Q08-guardrail-safety-chain.md"},
    },
    {
        "id": "17",
        "slug": "streaming-llm",
        "title": "Streaming LLM Responses",
        "hld": {"track": "genai", "num": 2, "file": "Q02-rag-document-qa.md"},
        "lld": {"track": "genai", "num": 9, "file": "Q09-streaming-response-aggregator.md"},
    },
    {
        "id": "18",
        "slug": "distributed-rate-limiter",
        "title": "Distributed Rate Limiter",
        "hld": {"track": "classic", "num": 11, "file": "Q11-distributed-rate-limiter.md"},
        "lld": {"track": "concurrency", "num": 8, "file": "Q08-rate-limiter-concurrent.md"},
    },
    {
        "id": "19",
        "slug": "web-crawler",
        "title": "Web Crawler at Scale",
        "hld": {"track": "classic", "num": 9, "file": "Q09-web-crawler.md"},
        "lld": {"track": "concurrency", "num": 11, "file": "Q11-web-crawler-multithreaded.md"},
    },
    {
        "id": "20",
        "slug": "token-budget-cost",
        "title": "Token Budget & Cost Control",
        "hld": {"track": "genai", "num": 34, "file": "Q34-cost-optimized-llm-routing.md"},
        "lld": {"track": "genai", "num": 5, "file": "Q05-token-budget-manager.md"},
    },
]

GOLD_STANDARD_SKIP = {
    "paired/CS-PAIR-01-enterprise-rag.md",
    "hld/classic/CS-HLD-C01-url-shortener.md",
    "lld/classic-ood/CS-LLD-O01-parking-lot.md",
}


def pair_by_hld(track: str, num: int) -> dict | None:
    for p in PAIRED_TOPICS:
        h = p["hld"]
        if h["track"] == track and h["num"] == num:
            return p
    return None


def pair_by_lld(track: str, num: int) -> dict | None:
    for p in PAIRED_TOPICS:
        l = p["lld"]
        if l["track"] == track and l["num"] == num:
            return p
    return None


def pair_doc_name(pair: dict) -> str:
    return f"CS-PAIR-{pair['id']}-{pair['slug']}.md"

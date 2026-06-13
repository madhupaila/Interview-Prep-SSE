# RAG Pipeline Deep Dive

Retrieval-Augmented Generation: ground LLM answers in your private data.

---

## Pipeline Stages

### 1. Document Ingestion

- **Sources:** S3, Google Drive, Confluence, databases
- **Triggers:** Upload webhook, scheduled sync, CDC from source DB
- **Queue:** SQS/Kafka for async processing

### 2. Parsing

| Format | Parser |
|--------|--------|
| PDF | PyMuPDF, Unstructured, Adobe API |
| HTML | BeautifulSoup, readability |
| Code | Tree-sitter for AST-aware chunks |
| Office | python-docx, openpyxl |

Extract: text, tables, headings, page numbers (for citations).

### 3. Chunking

| Strategy | Size | Use |
|----------|------|-----|
| Fixed token | 256–512 tokens | General docs |
| Semantic | Variable | Preserve meaning boundaries |
| Parent-child | Small child, large parent | Precise retrieval + rich context |

**Overlap:** 10–20% between chunks to avoid boundary cuts.

### 4. Embedding

- Models: `text-embedding-3-small`, Cohere embed, open-source BGE
- Batch embed for throughput (100+ chunks per API call)
- Store: vector + metadata (doc_id, chunk_id, tenant_id, page, ACL)

### 5. Indexing

- **Vector DB:** Pinecone, Weaviate, pgvector, Milvus
- **Metadata filters:** tenant_id, doc_type, date range
- **Hybrid:** BM25 (Elasticsearch) + vector fusion (RRF)

---

## Query Path

1. Embed user query (same model as ingestion)
2. Vector search top-K (20–50)
3. Optional: BM25 keyword search, merge results
4. Rerank top 20 → top 5 (cross-encoder)
5. Build prompt: system + context chunks + user query
6. LLM generate with citation instructions
7. Post-process: verify citations exist in context

---

## Chunking Deep Dive (Interview Favorite)

> "I use 512-token chunks with 10% overlap. For structured docs, I chunk by heading sections. For code, AST-based chunks per function."

**Tradeoff:** Smaller chunks = precise retrieval, less context. Larger = more context, noisier retrieval.

---

## Freshness

- **Version field** on documents; invalidate old chunks on update
- **CDC** from source systems triggers re-ingestion
- **TTL** on stale content if acceptable

---

## Hallucination Mitigation

1. Grounding: only answer from retrieved context
2. "I don't know" when retrieval score low
3. Citations required in prompt
4. Post-generation citation verification
5. Human review queue for low-confidence answers

---

## Storage Estimate

```
10M documents × 10 chunks/doc = 100M chunks
1536 dims × 4 bytes = 6KB per vector
100M × 6KB ≈ 600 GB vectors (+ metadata ~200 GB)
→ Pinecone or sharded Milvus; pgvector if < 50M vectors
```

---

## Interview Phrases

> "Hybrid search — BM25 catches exact product IDs, vectors catch semantic similarity."
> "Reranker improves precision from 70% to 85% recall@5."
> "Tenant isolation via metadata filter on every query."

# RAG UI Patterns

Frontend for **retrieval-augmented** answers — citations, sources, trust.

---

## Layout Options

| Pattern | Product analog | When |
|---------|----------------|------|
| **Inline citations** | Perplexity, Google AI Overviews | Default for Q&A |
| **Side source panel** | Notion AI, Glean | Long docs, legal |
| **Highlight in doc** | Harvey | PDF viewer + answer |
| **Footnote list** | Academic tools | Formal citations |

---

## Citation Data Model

```typescript
interface Citation {
  id: string;
  title: string;
  snippet: string;
  page?: number;
  url?: string;
}

interface AssistantMessage {
  content: string;
  citations: Citation[];
  faithfulness?: 'high' | 'low' | 'unknown';
}
```

---

## UX for Trust

- Show **sources before** or **alongside** answer
- "Answer only from your documents" badge
- Empty retrieval: "No relevant documents found" — no fake answer
- Low confidence: muted styling + expand sources

---

## Component Breakdown

- `AnswerPanel` — markdown body with `[1]` anchor links
- `CitationChip` — click opens `SourceDrawer`
- `DocumentUploadZone` — drag-drop + ingest progress (poll or SSE)
- `RetrievalDebug` — dev-only chunk scores (internal tools)

---

## Interview Script

> "RAG UI separates answer text from citation metadata. I render citation chips that open a drawer with snippet and page. If the API returns zero sources, I show an explicit empty state — never stream a confident answer without sources in enterprise mode. I sanitize HTML in snippets. Upload flow shows ingestion status per document because RAG latency is async."

---

## Related Questions

- [Q04 RAG citation UI](questions/Q04-rag-citation-source-panel.md)
- [Q05 Document upload ingest status](questions/Q05-document-upload-ingest-status.md)

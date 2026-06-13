# Gen AI LLD Memory Map

**Print this page.** In-process object design for Gen AI — complements [HLD Gen AI Memory Map](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/memory-map-genai.md).

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    GEN AI LLD MEMORY MAP                                │
├─────────────────────────────────────────────────────────────────────────┤
│ RAG PIPELINE (objects)                                                  │
│   Query → Retriever → Reranker → ContextAssembler → Generator → Answer │
│   Interfaces at each stage for swapping implementations                 │
├─────────────────────────────────────────────────────────────────────────┤
│ AGENT                                                                   │
│   ToolRegistry │ ToolExecutor │ Planner │ AgentContext │ MemoryStore   │
├─────────────────────────────────────────────────────────────────────────┤
│ PROMPT                                                                  │
│   PromptTemplate │ VariableResolver │ TemplateVersion │ render()       │
├─────────────────────────────────────────────────────────────────────────┤
│ MEMORY                                                                  │
│   ConversationMemory │ TokenCounter │ MemoryPolicy (trim/summarize)     │
├─────────────────────────────────────────────────────────────────────────┤
│ PROVIDER                                                                │
│   LLMProvider (Strategy) │ OpenAI │ Anthropic │ LocalModel             │
├─────────────────────────────────────────────────────────────────────────┤
│ SAFETY                                                                  │
│   GuardrailChain │ PIIFilter │ ToxicityFilter │ InjectionFilter        │
├─────────────────────────────────────────────────────────────────────────┤
│ EVAL                                                                    │
│   EvalRunner │ GoldenCase │ Metric │ Scorer │ aggregate()               │
├─────────────────────────────────────────────────────────────────────────┤
│ STREAMING                                                               │
│   StreamAggregator │ TokenChunk │ onToken() → AggregatedResponse       │
├─────────────────────────────────────────────────────────────────────────┤
│ MULTI-AGENT                                                             │
│   SupervisorAgent │ WorkerAgent │ AgentCoordinator (Mediator)            │
├─────────────────────────────────────────────────────────────────────────┤
│ LLD vs HLD                                                              │
│   LLD: class boundaries, interfaces, testability                      │
│   HLD: vector DB, GPU fleet, Kafka, rate limits at scale                │
└─────────────────────────────────────────────────────────────────────────┘
```

## Quick Picker

| Need | LLD class |
|------|-----------|
| Swap retrieval | `Retriever` interface |
| Swap model | `LLMProvider` Strategy |
| Tool calling | `ToolRegistry` + `ToolExecutor` |
| Trim history | `MemoryPolicy` Strategy |
| Block unsafe output | `GuardrailChain` |
| Run golden evals | `EvalRunner` Template Method |

## Related

- [Gen AI LLD Questions](questions/)
- [HLD RAG Q02](../System%20Design%20-%20High%20Level%20Design/02-genai-llm-hld/questions/Q02-rag-document-qa.md)
- [LLD vs HLD Boundary](../01-core-concepts/lld-vs-hld-boundary.md)

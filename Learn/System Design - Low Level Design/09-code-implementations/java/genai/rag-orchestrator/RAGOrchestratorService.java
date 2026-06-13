package com.lldprep.genai.ragorchestrator;

/**
 * Full reference implementation for LLD: rag-orchestrator
 * See question: 02-classic-ood/questions or matching track
 */
public class RAGOrchestratorService {
    private final RAGOrchestrator domain;

    public RAGOrchestratorService(RAGOrchestrator domain) {
        this.domain = domain;
    }

    public void answer() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

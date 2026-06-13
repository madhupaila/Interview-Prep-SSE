package com.lldprep.genai.ragorchestrator;

import java.util.List;
import java.util.stream.Collectors;

public class RAGOrchestrator {
    private final Retriever retriever;
    private final Generator generator;

    public RAGOrchestrator(Retriever retriever, Generator generator) {
        this.retriever = retriever;
        this.generator = generator;
    }

    public String answer(String query) {
        List<String> chunks = retriever.retrieve(query);
        String context = chunks.stream().collect(Collectors.joining("\n"));
        return generator.generate(query, context);
    }
}

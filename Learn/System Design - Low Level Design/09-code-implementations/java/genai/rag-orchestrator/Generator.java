package com.lldprep.genai.ragorchestrator;

public interface Generator {
    String generate(String query, String context);
}

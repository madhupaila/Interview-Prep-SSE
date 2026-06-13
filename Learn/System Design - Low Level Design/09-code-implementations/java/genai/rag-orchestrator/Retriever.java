package com.lldprep.genai.ragorchestrator;

import java.util.List;

public interface Retriever {
    List<String> retrieve(String query);
}

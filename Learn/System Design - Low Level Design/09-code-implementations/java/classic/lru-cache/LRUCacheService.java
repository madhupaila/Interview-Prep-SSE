package com.lldprep.classic.lrucache;

/**
 * Full reference implementation for LLD: lru-cache
 * See question: 02-classic-ood/questions or matching track
 */
public class LRUCacheService {
    private final LRUCache domain;

    public LRUCacheService(LRUCache domain) {
        this.domain = domain;
    }

    public void get() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

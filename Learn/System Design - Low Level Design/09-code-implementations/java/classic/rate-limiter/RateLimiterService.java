package com.lldprep.classic.ratelimiter;

/**
 * Full reference implementation for LLD: rate-limiter
 * See question: 02-classic-ood/questions or matching track
 */
public class RateLimiterService {
    private final RateLimiter domain;

    public RateLimiterService(RateLimiter domain) {
        this.domain = domain;
    }

    public void allowRequest() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

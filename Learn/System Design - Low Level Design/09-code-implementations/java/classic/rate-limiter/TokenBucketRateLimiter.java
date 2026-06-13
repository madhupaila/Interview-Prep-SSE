package com.lldprep.classic.ratelimiter;

public class TokenBucketRateLimiter {
    private final long capacity;
    private final double refillPerMs;
    private double tokens;
    private long lastRefillMs;

    public TokenBucketRateLimiter(long capacity, long refillPerSecond) {
        this.capacity = capacity;
        this.tokens = capacity;
        this.refillPerMs = refillPerSecond / 1000.0;
        this.lastRefillMs = System.currentTimeMillis();
    }

    public synchronized boolean allowRequest() {
        refill();
        if (tokens >= 1) {
            tokens -= 1;
            return true;
        }
        return false;
    }

    private void refill() {
        long now = System.currentTimeMillis();
        long elapsed = now - lastRefillMs;
        if (elapsed > 0) {
            tokens = Math.min(capacity, tokens + elapsed * refillPerMs);
            lastRefillMs = now;
        }
    }
}

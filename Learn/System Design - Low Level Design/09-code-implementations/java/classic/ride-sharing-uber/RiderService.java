package com.lldprep.classic.ridesharinguber;

/**
 * Full reference implementation for LLD: ride-sharing-uber
 * See question: 02-classic-ood/questions or matching track
 */
public class RiderService {
    private final Rider domain;

    public RiderService(Rider domain) {
        this.domain = domain;
    }

    public void requestRide() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

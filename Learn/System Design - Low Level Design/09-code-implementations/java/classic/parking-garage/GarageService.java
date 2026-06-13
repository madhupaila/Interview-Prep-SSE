package com.lldprep.classic.parkinggarage;

/**
 * Full reference implementation for LLD: parking-garage
 * See question: 02-classic-ood/questions or matching track
 */
public class GarageService {
    private final Garage domain;

    public GarageService(Garage domain) {
        this.domain = domain;
    }

    public void enterGate() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

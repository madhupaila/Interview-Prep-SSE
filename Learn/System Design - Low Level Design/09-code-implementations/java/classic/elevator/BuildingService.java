package com.lldprep.classic.elevator;

/**
 * Full reference implementation for LLD: elevator
 * See question: 02-classic-ood/questions or matching track
 */
public class BuildingService {
    private final Building domain;

    public BuildingService(Building domain) {
        this.domain = domain;
    }

    public void requestElevator() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

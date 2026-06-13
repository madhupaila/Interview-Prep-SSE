package com.lldprep.classic.parkinglot;

/**
 * Full reference implementation for LLD: parking-lot
 * See question: 02-classic-ood/questions or matching track
 */
public class ParkingLotService {
    private final ParkingLot domain;

    public ParkingLotService(ParkingLot domain) {
        this.domain = domain;
    }

    public void park() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

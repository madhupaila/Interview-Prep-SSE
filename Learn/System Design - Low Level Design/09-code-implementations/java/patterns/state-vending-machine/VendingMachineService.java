package com.lldprep.patterns.statevendingmachine;

/**
 * Full reference implementation for LLD: state-vending-machine
 * See question: 02-classic-ood/questions or matching track
 */
public class VendingMachineService {
    private final VendingMachine domain;

    public VendingMachineService(VendingMachine domain) {
        this.domain = domain;
    }

    public void insertCoin() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

package com.lldprep.patterns.observerstockticker;

/**
 * Full reference implementation for LLD: observer-stock-ticker
 * See question: 02-classic-ood/questions or matching track
 */
public class StockService {
    private final Stock domain;

    public StockService(Stock domain) {
        this.domain = domain;
    }

    public void update() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

package com.lldprep.classic.deckofcards;

/**
 * Full reference implementation for LLD: deck-of-cards
 * See question: 02-classic-ood/questions or matching track
 */
public class CardService {
    private final Card domain;

    public CardService(Card domain) {
        this.domain = domain;
    }

    public void deal() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

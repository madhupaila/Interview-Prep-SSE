package com.lldprep.classic.snakeandladder;

/**
 * Full reference implementation for LLD: snake-and-ladder
 * See question: 02-classic-ood/questions or matching track
 */
public class BoardService {
    private final Board domain;

    public BoardService(Board domain) {
        this.domain = domain;
    }

    public void playTurn() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

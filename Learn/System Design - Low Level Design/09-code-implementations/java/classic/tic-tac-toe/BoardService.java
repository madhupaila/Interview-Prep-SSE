package com.lldprep.classic.tictactoe;

/**
 * Full reference implementation for LLD: tic-tac-toe
 * See question: 02-classic-ood/questions or matching track
 */
public class BoardService {
    private final Board domain;

    public BoardService(Board domain) {
        this.domain = domain;
    }

    public void playMove() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

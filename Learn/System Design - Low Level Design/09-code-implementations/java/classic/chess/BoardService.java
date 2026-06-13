package com.lldprep.classic.chess;

/**
 * Full reference implementation for LLD: chess
 * See question: 02-classic-ood/questions or matching track
 */
public class BoardService {
    private final Board domain;

    public BoardService(Board domain) {
        this.domain = domain;
    }

    public void makeMove() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

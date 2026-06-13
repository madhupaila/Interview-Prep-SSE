package com.lldprep.patterns.commandundoredo;

/**
 * Full reference implementation for LLD: command-undo-redo
 * See question: 02-classic-ood/questions or matching track
 */
public class CommandService {
    private final Command domain;

    public CommandService(Command domain) {
        this.domain = domain;
    }

    public void execute() {
        // Core business logic — see question markdown for full design
        domain.execute();
    }
}

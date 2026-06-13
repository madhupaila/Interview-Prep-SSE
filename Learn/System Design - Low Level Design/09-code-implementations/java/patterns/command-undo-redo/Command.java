package com.lldprep.patterns.commandundoredo;

public interface Command {
    void execute();
    void undo();
}

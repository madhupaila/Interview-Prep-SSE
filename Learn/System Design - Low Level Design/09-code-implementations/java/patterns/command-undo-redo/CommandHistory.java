package com.lldprep.patterns.commandundoredo;

import java.util.ArrayDeque;
import java.util.Deque;

public class CommandHistory {
    private final Deque<Command> history = new ArrayDeque<>();

    public void execute(Command cmd) {
        cmd.execute();
        history.push(cmd);
    }

    public void undo() {
        if (!history.isEmpty()) history.pop().undo();
    }
}

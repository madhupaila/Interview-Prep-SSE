package com.lldprep.patterns.commandundoredo;

public class InsertCommand implements Command {
    private final Editor editor;
    private final String text;

    public InsertCommand(Editor editor, String text) {
        this.editor = editor;
        this.text = text;
    }

    @Override
    public void execute() { editor.insert(text); }

    @Override
    public void undo() { editor.delete(text.length()); }
}

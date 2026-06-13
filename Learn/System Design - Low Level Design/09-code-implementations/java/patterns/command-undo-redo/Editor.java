package com.lldprep.patterns.commandundoredo;

public class Editor {
    private final StringBuilder text = new StringBuilder();

    public void insert(String s) { text.append(s); }
    public void delete(int len) { text.setLength(Math.max(0, text.length() - len)); }
    public String getText() { return text.toString(); }
}

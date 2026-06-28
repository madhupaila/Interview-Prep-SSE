# Word Search II  ·  LeetCode #212

**Pattern:** Trie
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Meta, Google, Microsoft

---

## Memory Hook (Recognition Cue)

> **Find many words on a board → trie of words + board DFS**

---

## Problem

Return all words from the list that can be formed on the board (4-directional, no reuse).

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

_See solution below._

---

## Pattern Identification

Searching each word separately is wasteful; a trie lets one DFS over the board match all words simultaneously.

---

## Solution (Python)

```python
def find_words(board: list[list[str]], words: list[str]) -> list[str]:
    root = {}
    for w in words:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node['$'] = w
    rows, cols = len(board), len(board[0])
    res = []
    def dfs(r, c, node):
        ch = board[r][c]
        if ch not in node:
            return
        nxt = node[ch]
        if '$' in nxt:
            res.append(nxt.pop('$'))             # found; avoid duplicates
        board[r][c] = '#'
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                dfs(nr, nc, nxt)
        board[r][c] = ch
    for r in range(rows):
        for c in range(cols):
            dfs(r, c, root)
    return res
```

**Complexity:** Time O(R·C·4^L), Space O(total chars).

---

## Edge Cases & Pitfalls

- Empty input
- Single element
- All duplicates / negatives

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Trie](../../../01-patterns/trie.md)
- Related questions: `implement-trie`, `word-search`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

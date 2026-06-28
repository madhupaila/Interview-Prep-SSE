# Design Add and Search Words Data Structure  ·  LeetCode #211

**Pattern:** Trie
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Search with '.' wildcard → trie + DFS on wildcard**

---

## Problem

Support `addWord` and `search` where `.` matches any single character.

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

Cue maps to **Trie** — see [pattern sheet](../../../01-patterns/trie.md).

---

## Solution (Python)

```python
class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return '$' in node
            ch = word[i]
            if ch == '.':
                return any(dfs(child, i + 1)
                           for k, child in node.items() if k != '$')
            return ch in node and dfs(node[ch], i + 1)
        return dfs(self.root, 0)
```

**Complexity:** Time O(L) avg, O(26^L) worst, Space O(total chars).

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
- Related questions: `implement-trie`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

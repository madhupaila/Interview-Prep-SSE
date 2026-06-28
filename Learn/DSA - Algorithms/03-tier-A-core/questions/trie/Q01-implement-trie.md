# Implement Trie (Prefix Tree)  ·  LeetCode #208

**Pattern:** Trie
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Meta, Microsoft

---

## Memory Hook (Recognition Cue)

> **Prefix dictionary → nested children dict + is_word flag**

---

## Problem

Implement a trie with `insert`, `search`, and `startsWith`.

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
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node['$'] = True                          # word-end marker

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and '$' in node

    def startsWith(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node:
                return None
            node = node[ch]
        return node
```

**Complexity:** Time O(L) per op, Space O(total chars).

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
- Related questions: `design-add-search-words`, `word-search-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

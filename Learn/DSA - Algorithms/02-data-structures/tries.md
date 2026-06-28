# Trie (Prefix Tree)

A tree keyed by characters. Insert/search in O(L) regardless of how many words are stored. Ideal for prefix queries and dictionaries.

---

## Implementation

```python
class TrieNode:
    def __init__(self):
        self.children = {}      # char -> TrieNode
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            node = node.children.setdefault(ch, TrieNode())
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._walk(word)
        return node is not None and node.is_word

    def starts_with(self, prefix: str) -> bool:
        return self._walk(prefix) is not None

    def _walk(self, s):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```

### Array-backed (lowercase a–z) for speed

```python
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.is_word = False
# index: ord(ch) - ord('a')
```

---

## Complexity

| Operation | Cost |
|-----------|------|
| Insert | O(L) |
| Search / startsWith | O(L) |
| Space | O(total chars) |

(L = word length; independent of number of words stored.)

---

## When to Use

| Use | Instead of |
|-----|------------|
| Prefix queries, autocomplete | scanning all words |
| Wildcard word search | regex over a list |
| Word-search board + many words | repeated board DFS per word |
| Max XOR (binary trie) | pairwise comparison |

---

## Pitfalls

- A `set` is simpler if you only need exact membership.
- For board search, combine with DFS and prune found words.

---

## Related Patterns

- [Trie pattern](../01-patterns/trie.md), [Backtracking](../01-patterns/backtracking.md)

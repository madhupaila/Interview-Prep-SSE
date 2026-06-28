# Pattern: Trie (Prefix Tree)

## Recognition Cues

- "**Prefix** search", "starts with", "autocomplete"
- "Word dictionary", "add and search word" (with wildcards)
- Many strings sharing prefixes; repeated prefix queries
- "Longest word", "replace words", word-search on a board with a dictionary

## Core Idea

A tree where each node represents a character; paths spell words. Children stored in a dict; a flag marks word ends. Lookup/insert is O(length), independent of how many words are stored.

---

## Template

```python
class TrieNode:
    def __init__(self):
        self.children = {}
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
        node = self._find(word)
        return node is not None and node.is_word

    def starts_with(self, prefix: str) -> bool:
        return self._find(prefix) is not None

    def _find(self, s: str):
        node = self.root
        for ch in s:
            if ch not in node.children:
                return None
            node = node.children[ch]
        return node
```

### Wildcard search (DFS for `.`)

```python
def search_wild(self, word):
    def dfs(node, i):
        if i == len(word):
            return node.is_word
        ch = word[i]
        if ch == '.':
            return any(dfs(c, i + 1) for c in node.children.values())
        return ch in node.children and dfs(node.children[ch], i + 1)
    return dfs(self.root, 0)
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Prefix queries, autocomplete, dictionary | Single membership test → use a set |
| Word-search board + many words | No shared-prefix benefit |

## Complexity

- Insert/search: **O(L)** per word (L = length). Space: O(total chars).

## Variants & Pitfalls

- **Implement Trie**, **Add and Search Word** (wildcard), **Word Search II** (trie + board DFS), **Replace Words**, **Longest Word in Dictionary**, **Maximum XOR** (binary trie).
- Pitfall: prune visited words in Word Search II to avoid duplicates; use `setdefault` for clean inserts.

## Linked Questions

- Tier A: Implement Trie (Prefix Tree)
- Tier B: Design Add and Search Words, Replace Words, Longest Word in Dictionary
- Tier C: Word Search II, Maximum XOR of Two Numbers, Stream of Characters

## Related

- [Backtracking](backtracking.md) · [Trie DS](../02-data-structures/tries.md)

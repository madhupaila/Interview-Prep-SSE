# Replace Words  ·  LeetCode #648

**Pattern:** Trie
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Replace word by shortest root prefix → trie lookup**

---

## Problem

Replace each word in a sentence with the shortest dictionary root that is its prefix.

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
def replace_words(dictionary: list[str], sentence: str) -> str:
    root = {}
    for w in dictionary:
        node = root
        for ch in w:
            node = node.setdefault(ch, {})
        node['$'] = True

    def shortest_root(word):
        node = root
        for i, ch in enumerate(word):
            if ch not in node:
                break
            node = node[ch]
            if '$' in node:
                return word[:i + 1]
        return word

    return " ".join(shortest_root(w) for w in sentence.split())
```

**Complexity:** Time O(total chars), Space O(total chars).

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

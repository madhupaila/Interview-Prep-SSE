# Word Break II  ·  LeetCode #140

**Pattern:** Dynamic Programming
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **All sentence segmentations → memoized backtracking**

---

## Problem

Return all sentences formed by adding spaces so each word is in the dictionary.

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

Cue maps to **Dynamic Programming** — see [pattern sheet](../../../01-patterns/dynamic-programming.md).

---

## Solution (Python)

```python
from functools import cache

def word_break(s: str, word_dict: list[str]) -> list[str]:
    words = set(word_dict)
    @cache
    def dfs(start):
        if start == len(s):
            return [""]
        res = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in words:
                for rest in dfs(end):
                    res.append(word + ("" if rest == "" else " " + rest))
        return res
    return dfs(0)
```

**Complexity:** Time O(2^N), Space O(2^N).

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

- Pattern sheet: [Dynamic Programming](../../../01-patterns/dynamic-programming.md)
- Related questions: `word-break`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

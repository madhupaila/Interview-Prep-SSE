# Palindrome Partitioning  ·  LeetCode #131

**Pattern:** Backtracking
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **All partitions into palindromes → backtrack on cut positions**

---

## Problem

Return all ways to partition `s` so every substring is a palindrome.

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

Cue maps to **Backtracking** — see [pattern sheet](../../../01-patterns/backtracking.md).

---

## Solution (Python)

```python
def partition(s: str) -> list[list[str]]:
    res = []
    def is_pal(sub):
        return sub == sub[::-1]
    def dfs(start, path):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if is_pal(piece):
                path.append(piece)
                dfs(end, path)
                path.pop()
    dfs(0, [])
    return res
```

**Complexity:** Time O(N·2^N), Space O(N).

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

- Pattern sheet: [Backtracking](../../../01-patterns/backtracking.md)
- Related questions: `palindrome-partitioning-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

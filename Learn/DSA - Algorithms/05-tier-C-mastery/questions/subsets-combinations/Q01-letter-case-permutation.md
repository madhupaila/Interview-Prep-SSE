# Letter Case Permutation  ·  LeetCode #784

**Pattern:** Subsets & Combinations
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Toggle case of each letter → branch on letters**

---

## Problem

Return all strings from toggling the case of each letter in `s` (digits fixed).

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

Cue maps to **Subsets & Combinations** — see [pattern sheet](../../../01-patterns/subsets-combinations.md).

---

## Solution (Python)

```python
def letter_case_permutation(s: str) -> list[str]:
    res = []
    def dfs(i, path):
        if i == len(s):
            res.append("".join(path))
            return
        ch = s[i]
        if ch.isalpha():
            path.append(ch.lower()); dfs(i + 1, path); path.pop()
            path.append(ch.upper()); dfs(i + 1, path); path.pop()
        else:
            path.append(ch); dfs(i + 1, path); path.pop()
    dfs(0, [])
    return res
```

**Complexity:** Time O(2^L·L), Space O(L).

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

- Pattern sheet: [Subsets & Combinations](../../../01-patterns/subsets-combinations.md)
- Related questions: `subsets`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

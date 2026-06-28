# Group Anagrams  ·  LeetCode #49

**Pattern:** Arrays & Hashing
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Uber, Facebook

---

## Memory Hook (Recognition Cue)

> **Bucket strings by canonical key → hashmap of sorted-key → list**

---

## Problem

Group strings that are anagrams of each other.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Sort key | O(N·K log K) | O(N·K) | sorted string as key |
| Count key | O(N·K) | O(N·K) | 26-length count tuple as key |

---

## Pattern Identification

Cue maps to **Arrays & Hashing** — see [pattern sheet](../../../01-patterns/00-pattern-master-index.md).

---

## Solution (Python)

```python
from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))      # or a 26-length count tuple for O(K)
        groups[key].append(s)
    return list(groups.values())
```

**Complexity:** Time O(N·K log K), Space O(N·K).

---

## Edge Cases & Pitfalls

- Empty strings group together
- Single string

---

## Follow-Ups

1. Use count tuple to drop the log K
2. Stream of words?

---

## Related

- Pattern sheet: [Arrays & Hashing](../../../01-patterns/00-pattern-master-index.md)
- Related questions: `valid-anagram`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

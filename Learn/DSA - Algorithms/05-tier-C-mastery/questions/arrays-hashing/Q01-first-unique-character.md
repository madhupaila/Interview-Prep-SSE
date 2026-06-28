# First Unique Character in a String  ·  LeetCode #387

**Pattern:** Arrays & Hashing
**Tier:** C  ·  **Difficulty:** Easy
**Companies:** Amazon, Bloomberg, Goldman Sachs

---

## Memory Hook (Recognition Cue)

> **First non-repeating → frequency map then scan order**

---

## Problem

Return the index of the first non-repeating character in `s`, or -1.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Counter + scan | O(N) | O(1) | two passes |

---

## Pattern Identification

Cue maps to **Arrays & Hashing** — see [pattern sheet](../../../01-patterns/00-pattern-master-index.md).

---

## Solution (Python)

```python
from collections import Counter

def first_uniq_char(s: str) -> int:
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1
```

**Complexity:** Time O(N), Space O(1).

---

## Edge Cases & Pitfalls

- All repeating → -1
- Empty → -1

---

## Follow-Ups

1. Stream of characters (queue of candidates)

---

## Related

- Pattern sheet: [Arrays & Hashing](../../../01-patterns/00-pattern-master-index.md)
- Related questions: `valid-anagram`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

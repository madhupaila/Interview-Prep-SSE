# Median of Two Sorted Arrays  ·  LeetCode #4

**Pattern:** Binary Search
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, Microsoft, Adobe

---

## Memory Hook (Recognition Cue)

> **Median across two sorted arrays in O(log) → partition smaller array**

---

## Problem

Return the median of two sorted arrays in O(log(m+n)).

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

Binary search the partition of the smaller array so left halves of both ≤ right halves; median sits at the boundary.

---

## Solution (Python)

```python
def find_median_sorted_arrays(a: list[int], b: list[int]) -> float:
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    half = (m + n + 1) // 2
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2                       # cut in a
        j = half - i                             # cut in b
        a_left = a[i - 1] if i > 0 else float('-inf')
        a_right = a[i] if i < m else float('inf')
        b_left = b[j - 1] if j > 0 else float('-inf')
        b_right = b[j] if j < n else float('inf')
        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2:
                return max(a_left, b_left)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1
    return 0.0
```

**Complexity:** Time O(log min(M,N)), Space O(1).

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

- Pattern sheet: [Binary Search](../../../01-patterns/binary-search.md)
- Related questions: `kth-smallest-in-sorted-matrix`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

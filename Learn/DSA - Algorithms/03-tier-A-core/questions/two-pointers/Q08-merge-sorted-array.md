# Merge Sorted Array  ·  LeetCode #88

**Pattern:** Two Pointers
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Meta, Microsoft, Amazon

---

## Memory Hook (Recognition Cue)

> **Merge in place from the back → avoid overwriting**

---

## Problem

Merge `nums2` into `nums1` (which has trailing space) in sorted order, in place.

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

Cue maps to **Two Pointers** — see [pattern sheet](../../../01-patterns/two-pointers.md).

---

## Solution (Python)

```python
def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]; i -= 1
        else:
            nums1[k] = nums2[j]; j -= 1
        k -= 1
```

**Complexity:** Time O(M+N), Space O(1).

---

## Edge Cases & Pitfalls

- nums2 empty
- All nums2 smaller
- Fill from the end to avoid clobbering

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Two Pointers](../../../01-patterns/two-pointers.md)
- Related questions: `merge-two-sorted-lists`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

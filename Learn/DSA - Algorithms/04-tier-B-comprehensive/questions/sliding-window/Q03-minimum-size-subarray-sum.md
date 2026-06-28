# Minimum Size Subarray Sum  ·  LeetCode #209

**Pattern:** Sliding Window
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Facebook

---

## Memory Hook (Recognition Cue)

> **Shortest subarray with sum >= target (positives) → shrink while valid**

---

## Problem

Return the minimal length of a contiguous subarray whose sum ≥ `target`, or 0.

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

Cue maps to **Sliding Window** — see [pattern sheet](../../../01-patterns/sliding-window.md).

---

## Solution (Python)

```python
def min_subarray_len(target: int, nums: list[int]) -> int:
    left = 0
    total = 0
    best = float('inf')
    for right, n in enumerate(nums):
        total += n
        while total >= target:
            best = min(best, right - left + 1)
            total -= nums[left]
            left += 1
    return 0 if best == float('inf') else best
```

**Complexity:** Time O(N), Space O(1).

---

## Edge Cases & Pitfalls

- No valid subarray → 0
- Works only for non-negative values

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Sliding Window](../../../01-patterns/sliding-window.md)
- Related questions: `minimum-window-substring`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

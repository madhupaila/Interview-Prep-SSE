# Max Consecutive Ones III  ·  LeetCode #1004

**Pattern:** Sliding Window
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Facebook

---

## Memory Hook (Recognition Cue)

> **Longest window with at most k zeros → shrink when zeros > k**

---

## Problem

Return the longest subarray of 1s if you can flip at most `k` zeros.

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
def longest_ones(nums: list[int], k: int) -> int:
    left = zeros = best = 0
    for right, n in enumerate(nums):
        if n == 0:
            zeros += 1
        while zeros > k:
            if nums[left] == 0:
                zeros -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

**Complexity:** Time O(N), Space O(1).

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

- Pattern sheet: [Sliding Window](../../../01-patterns/sliding-window.md)
- Related questions: `longest-repeating-character-replacement`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

# Maximum Subarray (Greedy view)  ·  LeetCode #53

**Pattern:** Greedy
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Microsoft

---

## Memory Hook (Recognition Cue)

> **Drop prefix when running sum goes negative**

---

## Problem

Find the maximum contiguous subarray sum (greedy framing of Kadane).

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

Cue maps to **Greedy** — see [pattern sheet](../../../01-patterns/greedy.md).

---

## Solution (Python)

```python
def max_sub_array(nums: list[int]) -> int:
    best = cur = nums[0]
    for n in nums[1:]:
        if cur < 0:
            cur = 0                              # greedily drop negative prefix
        cur += n
        best = max(best, cur)
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

- Pattern sheet: [Greedy](../../../01-patterns/greedy.md)
- Related questions: `maximum-subarray`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

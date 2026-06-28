# Combination Sum IV  ·  LeetCode #377

**Pattern:** Dynamic Programming
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Count ordered ways to reach target → amount outer loop (permutations)**

---

## Problem

Count the number of ordered combinations summing to `target`.

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

Amount outer / numbers inner counts permutations — contrast with coin-change-ii (combinations).

---

## Solution (Python)

```python
def combination_sum4(nums: list[int], target: int) -> int:
    dp = [1] + [0] * target
    for a in range(1, target + 1):               # amount outer → counts orderings
        for n in nums:
            if n <= a:
                dp[a] += dp[a - n]
    return dp[target]
```

**Complexity:** Time O(target·N), Space O(target).

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
- Related questions: `coin-change-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

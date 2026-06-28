# Two Sum  ·  LeetCode #1

**Pattern:** Arrays & Hashing
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Google, Amazon, Meta, Microsoft, Apple

---

## Memory Hook (Recognition Cue)

> **Unsorted array + find a pair summing to target → hashmap complement**

---

## Problem

Given an array `nums` and an integer `target`, return indices of the two numbers that add up to `target`. Exactly one solution; no element reused.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Brute force | O(N^2) | O(1) | check all pairs |
| Hashmap (one pass) | O(N) | O(N) | store value→index, look up complement |

---

## Pattern Identification

We need a *pair* in an *unsorted* array with O(N). A hashmap turns the inner search into O(1) complement lookup.

---

## Solution (Python)

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}                       # value -> index
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []
```

**Complexity:** Time O(N), Space O(N).

---

## Edge Cases & Pitfalls

- No valid pair (return [])
- Duplicate values (store latest index)
- Negative numbers work fine

---

## Follow-Ups

1. What if the array is sorted? (two pointers, O(1) space)
2. Return all pairs?
3. 3Sum / 4Sum generalization

---

## Related

- Pattern sheet: [Arrays & Hashing](../../../01-patterns/00-pattern-master-index.md)
- Related questions: `two-sum-ii`, `3sum`, `two-sum-iv-bst`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

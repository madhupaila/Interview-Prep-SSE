# Longest Consecutive Sequence  ·  LeetCode #128

**Pattern:** Arrays & Hashing
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Google, Amazon, Meta

---

## Memory Hook (Recognition Cue)

> **Longest run of consecutive ints in O(N) → set + only start at sequence beginnings**

---

## Problem

Given an unsorted array, return the length of the longest run of consecutive integers. Must be O(N).

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Sort | O(N log N) | O(1) | violates O(N) requirement |
| Set + start check | O(N) | O(N) | extend only from numbers with no left neighbor |

---

## Pattern Identification

O(N) rules out sorting. A set gives O(1) membership; we extend a sequence only from its smallest element so each number is visited once.

---

## Solution (Python)

```python
def longest_consecutive(nums: list[int]) -> int:
    s = set(nums)
    best = 0
    for n in s:
        if n - 1 not in s:               # n is a sequence start
            length = 1
            while n + length in s:
                length += 1
            best = max(best, length)
    return best
```

**Complexity:** Time O(N), Space O(N).

---

## Edge Cases & Pitfalls

- Empty → 0
- Duplicates collapse in set
- Single element → 1

---

## Follow-Ups

1. Return the actual sequence?
2. Streaming numbers (Union-Find variant)

---

## Related

- Pattern sheet: [Arrays & Hashing](../../../01-patterns/00-pattern-master-index.md)
- Related questions: `contains-duplicate`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

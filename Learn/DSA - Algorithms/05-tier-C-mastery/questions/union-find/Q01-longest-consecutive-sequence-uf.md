# Longest Consecutive Sequence (Union-Find)  ·  LeetCode #128

**Pattern:** Union-Find
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Longest run via connectivity → union n with n+1**

---

## Problem

Find the longest consecutive run length using Union-Find.

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

Cue maps to **Union-Find** — see [pattern sheet](../../../01-patterns/union-find.md).

---

## Solution (Python)

```python
def longest_consecutive(nums: list[int]) -> int:
    parent = {n: n for n in nums}
    size = {n: 1 for n in nums}
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            size[rb] += size[ra]
    for n in nums:
        if n + 1 in parent:
            union(n, n + 1)
    return max(size[find(n)] for n in nums) if nums else 0
```

**Complexity:** Time O(N α), Space O(N).

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

- Pattern sheet: [Union-Find](../../../01-patterns/union-find.md)
- Related questions: `longest-consecutive-sequence`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

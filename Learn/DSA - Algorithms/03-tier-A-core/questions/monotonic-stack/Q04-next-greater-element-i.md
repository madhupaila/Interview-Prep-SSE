# Next Greater Element I  ·  LeetCode #496

**Pattern:** Monotonic Stack
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Bloomberg

---

## Memory Hook (Recognition Cue)

> **Next greater to the right, mapped across arrays → stack + hashmap**

---

## Problem

For each element of `nums1` (a subset of `nums2`), find its next greater element in `nums2`.

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

Cue maps to **Monotonic Stack** — see [pattern sheet](../../../01-patterns/monotonic-stack.md).

---

## Solution (Python)

```python
def next_greater_element(nums1: list[int], nums2: list[int]) -> list[int]:
    nxt = {}
    stack = []
    for n in nums2:
        while stack and stack[-1] < n:
            nxt[stack.pop()] = n
        stack.append(n)
    return [nxt.get(n, -1) for n in nums1]
```

**Complexity:** Time O(N+M), Space O(N).

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

- Pattern sheet: [Monotonic Stack](../../../01-patterns/monotonic-stack.md)
- Related questions: `daily-temperatures`, `next-greater-element-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

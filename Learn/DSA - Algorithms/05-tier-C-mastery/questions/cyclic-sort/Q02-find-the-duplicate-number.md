# Find the Duplicate Number  ·  LeetCode #287

**Pattern:** Cyclic Sort
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Microsoft

---

## Memory Hook (Recognition Cue)

> **One duplicate in 1..n, no mutation → Floyd cycle on value-as-pointer**

---

## Problem

Find the single duplicate in `nums` (values in [1, n]) without modifying it, O(1) space.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Sort/set | O(N) | O(N) | mutates or extra space |
| Floyd cycle | O(N) | O(1) | treat values as next pointers |

---

## Pattern Identification

Indices→values form a functional graph; a repeated value creates a cycle whose entrance is the duplicate (Floyd).

---

## Solution (Python)

```python
def find_duplicate(nums: list[int]) -> int:
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow
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

- Pattern sheet: [Cyclic Sort](../../../01-patterns/cyclic-sort.md)
- Related questions: `linked-list-cycle-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

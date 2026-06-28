# Jump Game II  ·  LeetCode #45

**Pattern:** Greedy
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Min jumps to end → BFS-like greedy on current reach window**

---

## Problem

Return the minimum number of jumps to reach the last index (always reachable).

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
def jump(nums: list[int]) -> int:
    jumps = 0
    cur_end = farthest = 0
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = farthest
    return jumps
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
- Related questions: `jump-game`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

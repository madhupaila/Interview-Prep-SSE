# Contains Duplicate  ·  LeetCode #217

**Pattern:** Arrays & Hashing
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google, Adobe

---

## Memory Hook (Recognition Cue)

> **Any duplicate exists? → set membership**

---

## Problem

Return `True` if any value appears at least twice in `nums`, else `False`.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Sort + scan | O(N log N) | O(1) | adjacent equal |
| Hash set | O(N) | O(N) | seen before? |

---

## Pattern Identification

Cue maps to **Arrays & Hashing** — see [pattern sheet](../../../01-patterns/00-pattern-master-index.md).

---

## Solution (Python)

```python
def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False
```

**Complexity:** Time O(N), Space O(N).

---

## Edge Cases & Pitfalls

- Empty array → False
- All unique → False

---

## Follow-Ups

1. Contains Duplicate II (within k indices)
2. Contains Duplicate III (value window)

---

## Related

- Pattern sheet: [Arrays & Hashing](../../../01-patterns/00-pattern-master-index.md)
- Related questions: `contains-duplicate-ii`, `longest-consecutive-sequence`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

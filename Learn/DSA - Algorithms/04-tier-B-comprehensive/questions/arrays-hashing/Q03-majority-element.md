# Majority Element  ·  LeetCode #169

**Pattern:** Arrays & Hashing
**Tier:** B  ·  **Difficulty:** Easy
**Companies:** Amazon, Google, Adobe

---

## Memory Hook (Recognition Cue)

> **Element appearing > N/2 times → Boyer-Moore voting (O(1) space)**

---

## Problem

Return the element appearing more than ⌊N/2⌋ times (guaranteed to exist).

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Counter | O(N) | O(N) | most_common |
| Boyer-Moore voting | O(N) | O(1) | candidate + count |

---

## Pattern Identification

Cue maps to **Arrays & Hashing** — see [pattern sheet](../../../01-patterns/00-pattern-master-index.md).

---

## Solution (Python)

```python
def majority_element(nums: list[int]) -> int:
    count = 0
    candidate = None
    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if n == candidate else -1
    return candidate
```

**Complexity:** Time O(N), Space O(1).

---

## Edge Cases & Pitfalls

- Single element
- Majority guaranteed by problem

---

## Follow-Ups

1. Majority Element II (> N/3, up to 2 answers)

---

## Related

- Pattern sheet: [Arrays & Hashing](../../../01-patterns/00-pattern-master-index.md)
- Related questions: `majority-element-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

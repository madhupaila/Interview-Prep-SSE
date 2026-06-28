# Find the Celebrity  ·  LeetCode #277

**Pattern:** Two Pointers
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Find node known by all but knows none → eliminate candidates linearly**

---

## Problem

Find the celebrity (known by everyone, knows no one) using the `knows(a,b)` API.

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

One pass narrows to a single candidate (if A knows B, A is out); a second pass verifies it.

---

## Solution (Python)

```python
def knows(a: int, b: int) -> bool:
    ...                                            # provided API stub

def find_celebrity(n: int) -> int:
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i                          # candidate can't be celebrity
    for i in range(n):
        if i != candidate and (knows(candidate, i) or not knows(i, candidate)):
            return -1
    return candidate
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

- Pattern sheet: [Two Pointers](../../../01-patterns/two-pointers.md)
- Related questions: `majority-element`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

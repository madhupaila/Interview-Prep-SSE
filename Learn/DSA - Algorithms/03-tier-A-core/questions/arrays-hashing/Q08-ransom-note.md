# Ransom Note  ·  LeetCode #383

**Pattern:** Arrays & Hashing
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Can build note from magazine letters → frequency subset**

---

## Problem

Return True if `ransomNote` can be built from `magazine` letters.

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

Cue maps to **Arrays & Hashing** — see [pattern sheet](../../../01-patterns/00-pattern-master-index.md).

---

## Solution (Python)

```python
from collections import Counter

def can_construct(ransom_note: str, magazine: str) -> bool:
    return not (Counter(ransom_note) - Counter(magazine))
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

- Pattern sheet: [Arrays & Hashing](../../../01-patterns/00-pattern-master-index.md)
- Related questions: `valid-anagram`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

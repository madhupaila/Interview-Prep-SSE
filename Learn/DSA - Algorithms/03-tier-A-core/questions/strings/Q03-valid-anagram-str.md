# Valid Anagram  ·  LeetCode #242

**Pattern:** Strings
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Bloomberg

---

## Memory Hook (Recognition Cue)

> **Same multiset of chars → Counter compare**

---

## Problem

Return True if `t` is an anagram of `s`.

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

Cue maps to **Strings** — see [pattern sheet](../../../02-data-structures/strings.md).

---

## Solution (Python)

```python
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)
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

- Pattern sheet: [Strings](../../../02-data-structures/strings.md)
- Related questions: `group-anagrams`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

# Valid Anagram  ·  LeetCode #242

**Pattern:** Arrays & Hashing
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Bloomberg, Uber

---

## Memory Hook (Recognition Cue)

> **Same characters, same counts → frequency map**

---

## Problem

Given `s` and `t`, return `True` if `t` is an anagram of `s`.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Sort both | O(N log N) | O(N) | compare sorted |
| Counter | O(N) | O(1) | 26 letters bounded |

---

## Pattern Identification

Cue maps to **Arrays & Hashing** — see [pattern sheet](../../../01-patterns/00-pattern-master-index.md).

---

## Solution (Python)

```python
from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)
```

**Complexity:** Time O(N), Space O(1).

---

## Edge Cases & Pitfalls

- Different lengths → False
- Unicode (Counter handles)

---

## Follow-Ups

1. Unicode beyond a–z?
2. Group anagrams

---

## Related

- Pattern sheet: [Arrays & Hashing](../../../01-patterns/00-pattern-master-index.md)
- Related questions: `group-anagrams`, `find-all-anagrams-in-a-string`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

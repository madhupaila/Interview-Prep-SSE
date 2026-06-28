# Word Pattern  ·  LeetCode #290

**Pattern:** Arrays & Hashing
**Tier:** B  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Bijection pattern↔words → two-way map**

---

## Problem

Return True if `s` follows the same pattern as `pattern`.

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
def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    if len(pattern) != len(words):
        return False
    p_to_w, w_to_p = {}, {}
    for p, w in zip(pattern, words):
        if p_to_w.setdefault(p, w) != w or w_to_p.setdefault(w, p) != p:
            return False
    return True
```

**Complexity:** Time O(N), Space O(N).

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
- Related questions: `isomorphic-strings`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

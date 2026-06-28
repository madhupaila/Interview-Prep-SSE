# Isomorphic Strings  ·  LeetCode #205

**Pattern:** Arrays & Hashing
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Consistent char mapping both ways → two dicts**

---

## Problem

Return True if `s` and `t` are isomorphic (consistent character mapping).

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
def is_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    s_to_t, t_to_s = {}, {}
    for a, b in zip(s, t):
        if s_to_t.setdefault(a, b) != b or t_to_s.setdefault(b, a) != a:
            return False
    return True
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
- Related questions: `word-pattern`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

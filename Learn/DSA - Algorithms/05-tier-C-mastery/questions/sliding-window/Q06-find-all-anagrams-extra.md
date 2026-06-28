# Permutation in String (Window)  ·  LeetCode #567

**Pattern:** Sliding Window
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Microsoft, Amazon

---

## Memory Hook (Recognition Cue)

> **Fixed window frequency match → match-count optimization**

---

## Problem

Return True if s2 contains a permutation of s1 (window match-count variant).

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

Cue maps to **Sliding Window** — see [pattern sheet](../../../01-patterns/sliding-window.md).

---

## Solution (Python)

```python
def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    need = [0] * 26
    window = [0] * 26
    for ch in s1:
        need[ord(ch) - 97] += 1
    for i, ch in enumerate(s2):
        window[ord(ch) - 97] += 1
        if i >= len(s1):
            window[ord(s2[i - len(s1)]) - 97] -= 1
        if window == need:
            return True
    return False
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

- Pattern sheet: [Sliding Window](../../../01-patterns/sliding-window.md)
- Related questions: `permutation-in-string`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

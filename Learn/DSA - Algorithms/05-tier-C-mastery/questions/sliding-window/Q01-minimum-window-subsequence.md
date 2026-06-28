# Minimum Window Subsequence  ·  LeetCode #727

**Pattern:** Sliding Window
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Google, Amazon

---

## Memory Hook (Recognition Cue)

> **Smallest window of s containing t as subsequence → forward match then shrink backward**

---

## Problem

Return the minimum window of `s` that contains `t` as a subsequence.

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
def min_window(s: str, t: str) -> str:
    best = ""
    i = 0
    while i < len(s):
        j = 0
        if s[i] == t[0]:
            start = i
            while i < len(s):
                if s[i] == t[j]:
                    j += 1
                    if j == len(t):
                        break
                i += 1
            if j == len(t):
                end = i
                while j > 0:                      # shrink backward
                    if s[i] == t[j - 1]:
                        j -= 1
                    i -= 1
                i += 1
                if not best or end - i + 1 < len(best):
                    best = s[i:end + 1]
        i += 1
    return best
```

**Complexity:** Time O(N·M), Space O(1).

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
- Related questions: `minimum-window-substring`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

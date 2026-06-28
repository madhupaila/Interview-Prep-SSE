# Backspace String Compare  ·  LeetCode #844

**Pattern:** Two Pointers
**Tier:** B  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Compare after backspaces → scan from the end skipping deletes**

---

## Problem

Return True if two strings are equal after processing backspace `#` characters.

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

Cue maps to **Two Pointers** — see [pattern sheet](../../../01-patterns/two-pointers.md).

---

## Solution (Python)

```python
def backspace_compare(s: str, t: str) -> bool:
    def nxt(string, i):
        skip = 0
        while i >= 0:
            if string[i] == '#':
                skip += 1
            elif skip:
                skip -= 1
            else:
                break
            i -= 1
        return i
    i, j = len(s) - 1, len(t) - 1
    while i >= 0 or j >= 0:
        i = nxt(s, i)
        j = nxt(t, j)
        if i >= 0 and j >= 0 and s[i] != t[j]:
            return False
        if (i >= 0) != (j >= 0):
            return False
        i -= 1; j -= 1
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

- Pattern sheet: [Two Pointers](../../../01-patterns/two-pointers.md)
- Related questions: `valid-palindrome`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

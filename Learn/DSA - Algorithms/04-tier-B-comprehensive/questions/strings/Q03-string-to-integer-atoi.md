# String to Integer (atoi)  ·  LeetCode #8

**Pattern:** Strings
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Microsoft

---

## Memory Hook (Recognition Cue)

> **Parse int with rules → strip, sign, digits, clamp**

---

## Problem

Implement atoi: parse leading optional sign and digits, clamp to 32-bit range.

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
def my_atoi(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0
    sign = 1
    i = 0
    if s[0] in "+-":
        sign = -1 if s[0] == '-' else 1
        i = 1
    num = 0
    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1
    num *= sign
    return max(-2**31, min(2**31 - 1, num))
```

**Complexity:** Time O(N), Space O(1).

---

## Edge Cases & Pitfalls

- Leading spaces
- No digits → 0
- Overflow clamps

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Strings](../../../02-data-structures/strings.md)
- Related questions: `reverse-integer`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

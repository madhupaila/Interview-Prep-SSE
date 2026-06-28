# Minimum Remove to Make Valid Parentheses  ·  LeetCode #1249

**Pattern:** Monotonic Stack
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Meta, Amazon

---

## Memory Hook (Recognition Cue)

> **Remove minimal invalid parens → stack of indices**

---

## Problem

Remove the minimum number of parentheses to make the string valid.

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

Cue maps to **Monotonic Stack** — see [pattern sheet](../../../01-patterns/monotonic-stack.md).

---

## Solution (Python)

```python
def min_remove_to_make_valid(s: str) -> str:
    s = list(s)
    stack = []
    for i, ch in enumerate(s):
        if ch == '(':
            stack.append(i)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    for i in stack:
        s[i] = ''
    return "".join(s)
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

- Pattern sheet: [Monotonic Stack](../../../01-patterns/monotonic-stack.md)
- Related questions: `valid-parentheses`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

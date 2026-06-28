# Valid Parentheses  ·  LeetCode #20

**Pattern:** Monotonic Stack
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Meta, Google, Microsoft

---

## Memory Hook (Recognition Cue)

> **Matching nested brackets → stack of opens**

---

## Problem

Return True if the string of brackets `()[]{}` is validly matched and nested.

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
def is_valid(s: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack = []
    for ch in s:
        if ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:
            stack.append(ch)
    return not stack
```

**Complexity:** Time O(N), Space O(N).

---

## Edge Cases & Pitfalls

- Odd length → False
- Empty → True
- Closing first → False

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Monotonic Stack](../../../01-patterns/monotonic-stack.md)
- Related questions: `min-stack`, `generate-parentheses`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

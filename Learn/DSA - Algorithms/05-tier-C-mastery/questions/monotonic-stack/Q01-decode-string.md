# Decode String  ·  LeetCode #394

**Pattern:** Monotonic Stack
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **Nested k[encoded] → stack of (count, prefix)**

---

## Problem

Decode strings like `3[a2[c]]` → `accaccacc`.

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
def decode_string(s: str) -> str:
    stack = []
    cur = ""
    num = 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == '[':
            stack.append((cur, num))
            cur, num = "", 0
        elif ch == ']':
            prev, k = stack.pop()
            cur = prev + cur * k
        else:
            cur += ch
    return cur
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
- Related questions: `basic-calculator-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

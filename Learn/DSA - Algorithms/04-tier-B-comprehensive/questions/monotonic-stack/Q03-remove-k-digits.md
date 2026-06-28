# Remove K Digits  ·  LeetCode #402

**Pattern:** Monotonic Stack
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Uber

---

## Memory Hook (Recognition Cue)

> **Smallest number after removing k digits → monotonic increasing stack**

---

## Problem

Remove `k` digits from `num` to form the smallest possible number.

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
def remove_k_digits(num: str, k: int) -> str:
    stack = []
    for d in num:
        while k and stack and stack[-1] > d:
            stack.pop()
            k -= 1
        stack.append(d)
    stack = stack[:len(stack) - k] if k else stack    # remove remaining from end
    return "".join(stack).lstrip("0") or "0"
```

**Complexity:** Time O(N), Space O(N).

---

## Edge Cases & Pitfalls

- Leading zeros stripped
- Remove all → '0'
- k remaining trimmed from end

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Monotonic Stack](../../../01-patterns/monotonic-stack.md)
- Related questions: `next-greater-element-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

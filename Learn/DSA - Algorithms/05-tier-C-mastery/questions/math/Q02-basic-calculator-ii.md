# Basic Calculator II  ·  LeetCode #227

**Pattern:** Interview Math
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Evaluate +-*/ expression → stack, apply */ immediately**

---

## Problem

Evaluate a string expression with `+ - * /` and non-negative integers (integer division truncates toward zero).

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

Cue maps to **Interview Math** — see [pattern sheet](../../../01-patterns/math-tricks.md).

---

## Solution (Python)

```python
def calculate(s: str) -> int:
    stack = []
    num = 0
    op = '+'
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        if ch in "+-*/" or i == len(s) - 1:
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            op = ch
            num = 0
    return sum(stack)
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

- Pattern sheet: [Interview Math](../../../01-patterns/math-tricks.md)
- Related questions: `basic-calculator`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

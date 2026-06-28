# Evaluate Reverse Polish Notation  ·  LeetCode #150

**Pattern:** Monotonic Stack
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Evaluate postfix → stack of operands**

---

## Problem

Evaluate an arithmetic expression in Reverse Polish Notation.

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
def eval_rpn(tokens: list[str]) -> int:
    stack = []
    ops = {'+', '-', '*', '/'}
    for t in tokens:
        if t in ops:
            b = stack.pop()
            a = stack.pop()
            if t == '+':
                stack.append(a + b)
            elif t == '-':
                stack.append(a - b)
            elif t == '*':
                stack.append(a * b)
            else:
                stack.append(int(a / b))           # truncate toward zero
        else:
            stack.append(int(t))
    return stack[0]
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

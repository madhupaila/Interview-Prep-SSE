# Generate Parentheses  ·  LeetCode #22

**Pattern:** Backtracking
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google, Uber

---

## Memory Hook (Recognition Cue)

> **Valid bracket combos → track open/close counts as constraints**

---

## Problem

Generate all combinations of `n` well-formed parentheses.

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

Cue maps to **Backtracking** — see [pattern sheet](../../../01-patterns/backtracking.md).

---

## Solution (Python)

```python
def generate_parenthesis(n: int) -> list[str]:
    res = []
    def dfs(path, open_count, close_count):
        if len(path) == 2 * n:
            res.append("".join(path))
            return
        if open_count < n:
            path.append('(')
            dfs(path, open_count + 1, close_count)
            path.pop()
        if close_count < open_count:
            path.append(')')
            dfs(path, open_count, close_count + 1)
            path.pop()
    dfs([], 0, 0)
    return res
```

**Complexity:** Time O(4^N / sqrt(N)), Space O(N).

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

- Pattern sheet: [Backtracking](../../../01-patterns/backtracking.md)
- Related questions: `letter-combinations-phone`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

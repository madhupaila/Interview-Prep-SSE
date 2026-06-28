# Maximal Rectangle  ·  LeetCode #85

**Pattern:** Monotonic Stack
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Largest all-1s rectangle in binary matrix → histogram per row + largest rectangle**

---

## Problem

Return the area of the largest rectangle of 1s in a binary matrix.

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
def maximal_rectangle(matrix: list[list[str]]) -> int:
    if not matrix:
        return 0
    cols = len(matrix[0])
    heights = [0] * cols
    best = 0

    def largest(hs):
        stack = []
        area = 0
        for i, h in enumerate(hs + [0]):
            while stack and hs[stack[-1]] > h:
                height = hs[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                area = max(area, height * width)
            stack.append(i)
        return area

    for row in matrix:
        for c in range(cols):
            heights[c] = heights[c] + 1 if row[c] == '1' else 0
        best = max(best, largest(heights))
    return best
```

**Complexity:** Time O(R·C), Space O(C).

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
- Related questions: `largest-rectangle-in-histogram`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

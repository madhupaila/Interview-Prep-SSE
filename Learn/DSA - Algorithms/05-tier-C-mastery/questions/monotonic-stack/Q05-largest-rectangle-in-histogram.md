# Largest Rectangle in Histogram  ·  LeetCode #84

**Pattern:** Monotonic Stack
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **Max area under bars → increasing stack; pop resolves width**

---

## Problem

Given bar heights, return the area of the largest rectangle in the histogram.

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

When a shorter bar arrives, every taller bar on the stack can no longer extend — pop and compute its maximal width.

---

## Solution (Python)

```python
def largest_rectangle_area(heights: list[int]) -> int:
    stack = []                                  # indices, increasing heights
    best = 0
    for i, h in enumerate(heights + [0]):       # sentinel flushes stack
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            best = max(best, height * width)
        stack.append(i)
    return best
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
- Related questions: `maximal-rectangle`, `trapping-rain-water-2p`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

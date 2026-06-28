# Max Points on a Line  ·  LeetCode #149

**Pattern:** Interview Math
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Google, LinkedIn

---

## Memory Hook (Recognition Cue)

> **Most collinear points → group by slope per anchor point**

---

## Problem

Return the maximum number of points that lie on the same straight line.

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

Fix each point as an anchor and bucket the others by reduced slope; the largest bucket + the anchor is the answer.

---

## Solution (Python)

```python
from collections import defaultdict
from math import gcd

def max_points(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 2:
        return n
    best = 0
    for i in range(n):
        slopes = defaultdict(int)
        for j in range(n):
            if i == j:
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            g = gcd(dx, dy) or 1
            slope = (dx // g, dy // g)
            slopes[slope] += 1
        best = max(best, max(slopes.values()) + 1)
    return best
```

**Complexity:** Time O(N^2), Space O(N).

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
- Related questions: `pow-x-n`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

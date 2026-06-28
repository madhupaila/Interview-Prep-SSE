# Find the Town Judge  ·  LeetCode #997

**Pattern:** Graph BFS/DFS
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Node trusted by all, trusts none → in/out degree counts**

---

## Problem

Find the town judge: trusted by everyone else and trusts no one.

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

Cue maps to **Graph BFS/DFS** — see [pattern sheet](../../../01-patterns/graph-traversal.md).

---

## Solution (Python)

```python
def find_judge(n: int, trust: list[list[int]]) -> int:
    score = [0] * (n + 1)
    for a, b in trust:
        score[a] -= 1
        score[b] += 1
    for i in range(1, n + 1):
        if score[i] == n - 1:
            return i
    return -1
```

**Complexity:** Time O(E), Space O(N).

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

- Pattern sheet: [Graph BFS/DFS](../../../01-patterns/graph-traversal.md)
- Related questions: `find-celebrity`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

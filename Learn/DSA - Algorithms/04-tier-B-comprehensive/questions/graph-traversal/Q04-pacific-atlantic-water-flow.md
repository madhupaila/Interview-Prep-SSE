# Pacific Atlantic Water Flow  ·  LeetCode #417

**Pattern:** Graph BFS/DFS
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Meta

---

## Memory Hook (Recognition Cue)

> **Cells reaching both oceans → DFS inward from each ocean border**

---

## Problem

Return cells from which water can flow to both the Pacific and Atlantic oceans.

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
def pacific_atlantic(heights: list[list[int]]) -> list[list[int]]:
    if not heights:
        return []
    rows, cols = len(heights), len(heights[0])
    pac, atl = set(), set()
    def dfs(r, c, seen, prev):
        if ((r, c) in seen or not (0 <= r < rows and 0 <= c < cols)
                or heights[r][c] < prev):
            return
        seen.add((r, c))
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            dfs(r+dr, c+dc, seen, heights[r][c])
    for c in range(cols):
        dfs(0, c, pac, 0)
        dfs(rows-1, c, atl, 0)
    for r in range(rows):
        dfs(r, 0, pac, 0)
        dfs(r, cols-1, atl, 0)
    return [[r, c] for r, c in pac & atl]
```

**Complexity:** Time O(R·C), Space O(R·C).

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
- Related questions: `number-of-islands`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

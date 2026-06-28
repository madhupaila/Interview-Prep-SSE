# Alien Dictionary  ·  LeetCode #269

**Pattern:** Topological Sort
**Tier:** C  ·  **Difficulty:** Hard
**Companies:** Amazon, Meta, Google, Airbnb

---

## Memory Hook (Recognition Cue)

> **Derive char order from sorted words → build edges, topo sort**

---

## Problem

Given words sorted in an alien language, return a valid character order (or '').

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

Cue maps to **Topological Sort** — see [pattern sheet](../../../01-patterns/topological-sort.md).

---

## Solution (Python)

```python
from collections import defaultdict, deque

def alien_order(words: list[str]) -> str:
    graph = defaultdict(set)
    indeg = {c: 0 for w in words for c in w}
    for a, b in zip(words, words[1:]):
        for x, y in zip(a, b):
            if x != y:
                if y not in graph[x]:
                    graph[x].add(y)
                    indeg[y] += 1
                break
        else:
            if len(a) > len(b):
                return ""                        # prefix violation
    q = deque(c for c in indeg if indeg[c] == 0)
    order = []
    while q:
        c = q.popleft()
        order.append(c)
        for nb in graph[c]:
            indeg[nb] -= 1
            if indeg[nb] == 0:
                q.append(nb)
    return "".join(order) if len(order) == len(indeg) else ""
```

**Complexity:** Time O(C), Space O(1).

---

## Edge Cases & Pitfalls

- Invalid prefix ordering → ''
- Cycle → ''

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Topological Sort](../../../01-patterns/topological-sort.md)
- Related questions: `course-schedule-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

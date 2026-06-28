# Word Ladder  ·  LeetCode #127

**Pattern:** Graph BFS/DFS
**Tier:** B  ·  **Difficulty:** Hard
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Shortest transformation sequence → BFS over word graph**

---

## Problem

Return the length of the shortest transformation from `beginWord` to `endWord` changing one letter at a time within `wordList`.

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
from collections import deque, defaultdict

def ladder_length(begin: str, end: str, word_list: list[str]) -> int:
    words = set(word_list)
    if end not in words:
        return 0
    q = deque([(begin, 1)])
    while q:
        word, steps = q.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nxt = word[:i] + ch + word[i+1:]
                if nxt in words:
                    words.remove(nxt)
                    q.append((nxt, steps + 1))
    return 0
```

**Complexity:** Time O(N·L·26), Space O(N·L).

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
- Related questions: `word-ladder-ii`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

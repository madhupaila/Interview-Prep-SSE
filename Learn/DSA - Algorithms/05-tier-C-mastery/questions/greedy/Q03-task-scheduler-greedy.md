# Reorganize String / Scheduling (Greedy)  ·  LeetCode #767

**Pattern:** Greedy
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta

---

## Memory Hook (Recognition Cue)

> **Arrange so no two adjacent equal → place most frequent first with a gap**

---

## Problem

Rearrange characters so no two identical are adjacent (greedy on frequency).

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

Cue maps to **Greedy** — see [pattern sheet](../../../01-patterns/greedy.md).

---

## Solution (Python)

```python
from collections import Counter

def reorganize_string(s: str) -> str:
    freq = Counter(s)
    n = len(s)
    if max(freq.values()) > (n + 1) // 2:
        return ""
    res = [''] * n
    i = 0
    for ch, _ in freq.most_common():
        for _ in range(freq[ch]):
            res[i] = ch
            i += 2
            if i >= n:
                i = 1                            # fill odd slots next
    return "".join(res)
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

- Pattern sheet: [Greedy](../../../01-patterns/greedy.md)
- Related questions: `reorganize-string`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

# Time Based Key-Value Store  ·  LeetCode #981

**Pattern:** Binary Search
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Uber

---

## Memory Hook (Recognition Cue)

> **Latest value at or before a timestamp → binary search on sorted timestamps**

---

## Problem

Design a store with `set(key, value, ts)` and `get(key, ts)` returning the value with the largest ts ≤ query.

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

Cue maps to **Binary Search** — see [pattern sheet](../../../01-patterns/binary-search.md).

---

## Solution (Python)

```python
from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)          # key -> [(ts, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        i = bisect.bisect_right(arr, (timestamp, chr(127)))
        return arr[i - 1][1] if i else ""
```

**Complexity:** Time O(log N) get, Space O(N).

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

- Pattern sheet: [Binary Search](../../../01-patterns/binary-search.md)
- Related questions: `search-insert-position`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

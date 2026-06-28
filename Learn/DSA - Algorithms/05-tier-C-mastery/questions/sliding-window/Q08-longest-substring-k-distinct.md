# Longest Substring with At Most K Distinct Characters  ·  LeetCode #340

**Pattern:** Sliding Window
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Google, Amazon, Facebook

---

## Memory Hook (Recognition Cue)

> **At most K distinct → variable window + frequency map sized K**

---

## Problem

Return the length of the longest substring with at most `k` distinct characters.

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

Cue maps to **Sliding Window** — see [pattern sheet](../../../01-patterns/sliding-window.md).

---

## Solution (Python)

```python
from collections import defaultdict

def length_of_longest_substring_k_distinct(s: str, k: int) -> int:
    if k == 0:
        return 0
    count = defaultdict(int)
    left = best = 0
    for right, ch in enumerate(s):
        count[ch] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
```

**Complexity:** Time O(N), Space O(k).

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

- Pattern sheet: [Sliding Window](../../../01-patterns/sliding-window.md)
- Related questions: `fruit-into-baskets`, `longest-substring-without-repeating`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

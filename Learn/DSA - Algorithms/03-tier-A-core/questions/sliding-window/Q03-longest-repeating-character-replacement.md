# Longest Repeating Character Replacement  ·  LeetCode #424

**Pattern:** Sliding Window
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Google, Amazon, Meta

---

## Memory Hook (Recognition Cue)

> **Window valid if (size - maxFreq) <= k → expand/shrink**

---

## Problem

You may replace at most `k` characters. Return the length of the longest substring of one repeating letter achievable.

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

A window is valid when the characters we must replace (window size minus the most frequent char) is ≤ k.

---

## Solution (Python)

```python
from collections import defaultdict

def character_replacement(s: str, k: int) -> int:
    count = defaultdict(int)
    left = best = max_freq = 0
    for right, ch in enumerate(s):
        count[ch] += 1
        max_freq = max(max_freq, count[ch])
        while (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best
```

**Complexity:** Time O(N), Space O(1).

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
- Related questions: `longest-substring-without-repeating`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

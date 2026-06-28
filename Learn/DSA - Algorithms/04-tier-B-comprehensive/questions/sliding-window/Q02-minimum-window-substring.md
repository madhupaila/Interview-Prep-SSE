# Minimum Window Substring  ·  LeetCode #76

**Pattern:** Sliding Window
**Tier:** B  ·  **Difficulty:** Hard
**Companies:** Meta, Amazon, Google, Uber

---

## Memory Hook (Recognition Cue)

> **Smallest window covering all required chars → expand then shrink while valid**

---

## Problem

Return the minimum window in `s` containing all characters of `t` (with multiplicity).

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Sliding window | O(N) | O(charset) | have/need counter, shrink while valid |

---

## Pattern Identification

Minimum-length valid window: grow right until valid, then shrink left while still valid, recording the best.

---

## Solution (Python)

```python
from collections import Counter

def min_window(s: str, t: str) -> str:
    if not s or not t:
        return ""
    need = Counter(t)
    missing = len(t)
    left = 0
    best = (float('inf'), 0, 0)
    for right, ch in enumerate(s):
        if need[ch] > 0:
            missing -= 1
        need[ch] -= 1
        while missing == 0:                    # window valid → shrink
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right)
            need[s[left]] += 1
            if need[s[left]] > 0:
                missing += 1
            left += 1
    return "" if best[0] == float('inf') else s[best[1]: best[2] + 1]
```

**Complexity:** Time O(N), Space O(charset).

---

## Edge Cases & Pitfalls

- t longer than s → ''
- No valid window → ''
- Duplicates in t

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Sliding Window](../../../01-patterns/sliding-window.md)
- Related questions: `longest-substring-without-repeating`, `minimum-size-subarray-sum`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

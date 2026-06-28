# Longest Substring Without Repeating Characters  ·  LeetCode #3

**Pattern:** Sliding Window
**Tier:** A  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Bloomberg, Adobe

---

## Memory Hook (Recognition Cue)

> **Longest substring with a constraint → variable window + last-seen map**

---

## Problem

Return the length of the longest substring without repeating characters.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Brute force | O(N^2) | O(N) | check all substrings |
| Sliding window | O(N) | O(min(N,charset)) | jump left past last dup |

---

## Pattern Identification

Contiguous substring + 'longest valid' is the textbook variable sliding-window; a map of last index lets left jump in O(1).

---

## Solution (Python)

```python
def length_of_longest_substring(s: str) -> int:
    last = {}
    left = best = 0
    for right, ch in enumerate(s):
        if ch in last and last[ch] >= left:
            left = last[ch] + 1
        last[ch] = right
        best = max(best, right - left + 1)
    return best
```

**Complexity:** Time O(N), Space O(min(N, charset)).

---

## Edge Cases & Pitfalls

- Empty → 0
- All same char → 1
- All unique → len(s)

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Sliding Window](../../../01-patterns/sliding-window.md)
- Related questions: `longest-repeating-character-replacement`, `minimum-window-substring`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

# Reverse Words in a String  ·  LeetCode #151

**Pattern:** Strings
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Microsoft, Bloomberg

---

## Memory Hook (Recognition Cue)

> **Reverse word order, trim spaces → split + reverse + join**

---

## Problem

Reverse the order of words, collapsing multiple spaces.

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

Cue maps to **Strings** — see [pattern sheet](../../../02-data-structures/strings.md).

---

## Solution (Python)

```python
def reverse_words(s: str) -> str:
    return " ".join(reversed(s.split()))
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

- Pattern sheet: [Strings](../../../02-data-structures/strings.md)
- Related questions: `reverse-string`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

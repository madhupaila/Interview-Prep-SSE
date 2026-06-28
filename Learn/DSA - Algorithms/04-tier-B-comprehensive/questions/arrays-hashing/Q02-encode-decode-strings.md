# Encode and Decode Strings  ·  LeetCode #271

**Pattern:** Arrays & Hashing
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Google, Meta, Amazon

---

## Memory Hook (Recognition Cue)

> **Serialize a list of arbitrary strings → length-prefix framing**

---

## Problem

Design `encode(list[str]) -> str` and `decode(str) -> list[str]` that round-trip any strings (including delimiters).

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

| Approach | Time | Space | Note |
|----------|------|-------|------|
| Length-prefix | O(N) | O(N) | len + '#' + s avoids delimiter collisions |

---

## Pattern Identification

Cue maps to **Arrays & Hashing** — see [pattern sheet](../../../01-patterns/00-pattern-master-index.md).

---

## Solution (Python)

```python
def encode(strs: list[str]) -> str:
    return "".join(f"{len(s)}#{s}" for s in strs)

def decode(s: str) -> list[str]:
    res, i = [], 0
    while i < len(s):
        j = s.index("#", i)
        length = int(s[i:j])
        res.append(s[j + 1: j + 1 + length])
        i = j + 1 + length
    return res
```

**Complexity:** Time O(N), Space O(N).

---

## Edge Cases & Pitfalls

- Empty list
- Strings containing '#' or digits (length-prefix is safe)

---

## Follow-Ups

1. Unicode lengths (use byte length)
2. Streaming decode

---

## Related

- Pattern sheet: [Arrays & Hashing](../../../01-patterns/00-pattern-master-index.md)
- Related questions: `serialize-deserialize-binary-tree`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

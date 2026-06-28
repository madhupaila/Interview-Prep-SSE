# Lemonade Change  ·  LeetCode #860

**Pattern:** Greedy
**Tier:** A  ·  **Difficulty:** Easy
**Companies:** Amazon, Google

---

## Memory Hook (Recognition Cue)

> **Give change greedily → prefer using larger bills first**

---

## Problem

Return True if you can give correct change to every customer (bills 5/10/20).

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
def lemonade_change(bills: list[int]) -> bool:
    five = ten = 0
    for b in bills:
        if b == 5:
            five += 1
        elif b == 10:
            if not five:
                return False
            five -= 1; ten += 1
        else:
            if ten and five:
                ten -= 1; five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True
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

- Pattern sheet: [Greedy](../../../01-patterns/greedy.md)
- Related questions: `gas-station`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

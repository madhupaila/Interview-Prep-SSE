# Count Primes  ·  LeetCode #204

**Pattern:** Interview Math
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Google, Microsoft

---

## Memory Hook (Recognition Cue)

> **Count primes below n → Sieve of Eratosthenes**

---

## Problem

Count the number of primes strictly less than `n`.

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

Cue maps to **Interview Math** — see [pattern sheet](../../../01-patterns/math-tricks.md).

---

## Solution (Python)

```python
def count_primes(n: int) -> int:
    if n < 3:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return sum(is_prime)
```

**Complexity:** Time O(N log log N), Space O(N).

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

- Pattern sheet: [Interview Math](../../../01-patterns/math-tricks.md)
- Related questions: `pow-x-n`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

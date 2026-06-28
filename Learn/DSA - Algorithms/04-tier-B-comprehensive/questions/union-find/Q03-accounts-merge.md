# Accounts Merge  ·  LeetCode #721

**Pattern:** Union-Find
**Tier:** B  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Google

---

## Memory Hook (Recognition Cue)

> **Merge accounts sharing emails → union by email owner**

---

## Problem

Merge accounts that share any email; return merged accounts with sorted emails.

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

Cue maps to **Union-Find** — see [pattern sheet](../../../01-patterns/union-find.md).

---

## Solution (Python)

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        self.count -= 1
        return True

from collections import defaultdict

def accounts_merge(accounts: list[list[str]]) -> list[list[str]]:
    dsu = DSU(len(accounts))
    email_to_id = {}
    for i, acc in enumerate(accounts):
        for email in acc[1:]:
            if email in email_to_id:
                dsu.union(i, email_to_id[email])
            else:
                email_to_id[email] = i
    groups = defaultdict(set)
    for email, i in email_to_id.items():
        groups[dsu.find(i)].add(email)
    return [[accounts[root][0]] + sorted(emails) for root, emails in groups.items()]
```

**Complexity:** Time O(N·K log K), Space O(N·K).

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

- Pattern sheet: [Union-Find](../../../01-patterns/union-find.md)
- Related questions: `number-of-provinces`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

# Arrays & Hashing

The most common interview data structures. Master the operations and the hashing tricks.

---

## Arrays (Python `list`)

| Operation | Complexity | Note |
|-----------|-----------|------|
| Index access `a[i]` | O(1) | |
| Append / pop end | O(1) amortized | |
| Insert / pop middle | O(N) | shifts elements |
| Search by value | O(N) | unsorted |
| Sort | O(N log N) | Timsort |

```python
a = [3, 1, 2]
a.append(4)          # [3,1,2,4]
a.pop()              # 4 -> [3,1,2]
a.sort()             # [1,2,3]
a[1:3]               # slice [2,3] (O(k) copy)
a.index(2)           # 1 (O(N))
```

---

## Hash Map / Set (`dict`, `set`)

O(1) average insert/lookup/delete. The single most useful interview tool — converts O(N^2) scans into O(N).

```python
seen = {}
seen[key] = value
if key in seen: ...          # O(1) avg

unique = set(nums)           # dedupe
from collections import Counter, defaultdict
freq = Counter(nums)         # frequency map
adj = defaultdict(list)      # auto-init lists
```

### Classic hashing tricks

```python
# Two Sum — complement lookup
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i

# Group anagrams — sorted tuple key
def group_anagrams(strs):
    groups = defaultdict(list)
    for s in strs:
        groups[tuple(sorted(s))].append(s)
    return list(groups.values())

# Frequency-based logic
def first_unique(s):
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1
```

---

## When to Reach for Hashing

| Need | Use |
|------|-----|
| O(1) membership / complement | set / dict |
| Count occurrences | Counter |
| Group by key | defaultdict(list) |
| Detect duplicate | set |
| Index lookup by value | dict value→index |

---

## Pitfalls

- Worst-case O(N) on adversarial hash collisions (rare in practice).
- `[[0]*c]*r` aliases rows — use comprehension.
- Sets/dicts are unordered by value (dicts keep insertion order).

---

## Related Patterns

- [Two Pointers](../01-patterns/two-pointers.md), [Sliding Window](../01-patterns/sliding-window.md), [Prefix Sum](../01-patterns/prefix-sum.md)
- [Python for Interviews](../00-foundations/03-python-for-interviews.md)

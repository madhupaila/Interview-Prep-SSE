# Pattern: Subsets & Combinations

## Recognition Cues

- "All **subsets** / power set"
- "All **combinations** of size k", "all **permutations**"
- "Combinations that sum to target"
- Enumerate selections where order does/doesn't matter

## Core Idea

A specialized backtracking family. Subsets: at each element choose include/exclude. Combinations: advance a `start` index to avoid reusing earlier elements. Permutations: track a `used` set since order matters.

---

## Templates

### Subsets (power set)

```python
def subsets(nums: list[int]) -> list[list[int]]:
    res = []
    def dfs(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()
    dfs(0, [])
    return res
```

### Permutations

```python
def permute(nums: list[int]) -> list[list[int]]:
    res = []
    def dfs(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i, n in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(n)
            dfs(path, used)
            path.pop()
            used[i] = False
    dfs([], [False] * len(nums))
    return res
```

### Iterative subsets (bitmask)

```python
def subsets_bitmask(nums):
    n = len(nums)
    res = []
    for mask in range(1 << n):
        res.append([nums[i] for i in range(n) if mask & (1 << i)])
    return res
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Enumerate all selections/orderings | Only need count → combinatorics/DP |
| N small (≤ ~20) | Large N → exponential blowup |

## Complexity

- Subsets: **O(N·2^N)**. Permutations: **O(N·N!)**. Space: O(N) recursion.

## Variants & Pitfalls

- **Subsets II / Combination Sum II** (sort + skip duplicates), **Permutations II**, **Combinations (n choose k)**.
- Pitfall: dedupe by sorting and skipping `i > start and nums[i] == nums[i-1]`.

## Linked Questions

- Tier A: Subsets, Permutations, Combinations, Combination Sum
- Tier B: Subsets II, Permutations II, Combination Sum II, Letter Case Permutation
- Tier C: Palindrome Partitioning, Beautiful Arrangement

## Related

- [Backtracking](backtracking.md) · [Bit Manipulation](bit-manipulation.md)

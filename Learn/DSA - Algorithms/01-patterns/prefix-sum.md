# Pattern: Prefix Sum

## Recognition Cues

- "**Subarray sum** equals K", "count subarrays with sum/property"
- "Range sum queries" (immutable array, many queries)
- Negatives present (rules out sliding window for sums)
- 2D "submatrix sum"

## Core Idea

Precompute cumulative sums so any range sum is an O(1) subtraction: `sum(i..j) = prefix[j+1] - prefix[i]`. Combine with a **hashmap of seen prefix sums** to count/locate subarrays in one pass.

---

## Templates

### Range sum (immutable)

```python
class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for n in nums:
            self.prefix.append(self.prefix[-1] + n)
    def range_sum(self, i, j):           # inclusive
        return self.prefix[j + 1] - self.prefix[i]
```

### Subarray sum equals K (with hashmap)

```python
from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    seen = defaultdict(int)
    seen[0] = 1
    prefix = count = 0
    for n in nums:
        prefix += n
        count += seen[prefix - k]
        seen[prefix] += 1
    return count
```

### 2D prefix sum (submatrix)

```python
def build_2d(matrix):
    R, C = len(matrix), len(matrix[0])
    P = [[0] * (C + 1) for _ in range(R + 1)]
    for r in range(R):
        for c in range(C):
            P[r+1][c+1] = matrix[r][c] + P[r][c+1] + P[r+1][c] - P[r][c]
    return P
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Many range-sum queries | Single query → just sum once |
| Subarray sum/count with negatives | All positive + contiguous max → sliding window |

## Complexity

- Build: **O(N)**; query: **O(1)**. Hashmap variant: **O(N)** time/space.

## Variants & Pitfalls

- **Subarray Sum Equals K**, **Contiguous Array** (map 0→-1), **Range Sum Query**, **Product of Array Except Self** (prefix/suffix products), **Subarray Sums Divisible by K** (mod buckets).
- Pitfall: seed `seen[0] = 1` to count subarrays starting at index 0.

## Linked Questions

- Tier A: Range Sum Query Immutable, Product of Array Except Self, Subarray Sum Equals K
- Tier B: Contiguous Array, Subarray Sums Divisible by K, Range Sum Query 2D
- Tier C: Maximum Size Subarray Sum Equals K, Count Number of Nice Subarrays

## Related

- [Sliding Window](sliding-window.md) · [Arrays & Hashing](../02-data-structures/arrays-hashing.md)

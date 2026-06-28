# Pattern: Binary Search

## Recognition Cues

- Array is **sorted** (or rotated-sorted)
- "Find target / first / last / insertion point"
- **"Minimize the maximum"** or **"maximize the minimum"** → binary search on the **answer**
- Monotonic predicate: `feasible(x)` is False…False, True…True

## Core Idea

Halve the search space each step using a monotonic property. Beyond sorted arrays, search over the **answer space** when a candidate value can be validated in O(N).

---

## Templates

### Classic (find target)

```python
def binary_search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

### Leftmost boundary (bisect_left style)

```python
def lower_bound(nums, target):
    lo, hi = 0, len(nums)            # note: hi = len
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo                        # first index >= target
```

### Binary search on the answer

```python
def min_feasible(lo, hi, feasible):
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid                 # mid works, try smaller
        else:
            lo = mid + 1
    return lo
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Sorted data or monotonic predicate | Unsorted with no monotonic property |
| "minimize max / maximize min / kth" | Need all elements (O(N) anyway) |

## Complexity

- Time: **O(log N)** (classic) or **O(N log(range))** for answer-space search.
- Space: **O(1)**.

## Variants & Pitfalls

- **Rotated sorted array:** decide which half is sorted, search accordingly.
- **Find min in rotated**, **search range**, **median of two sorted arrays**.
- **Answer-space:** Koko eating bananas, ship within D days, split array largest sum.
- Pitfalls: `mid = (lo+hi)//2` overflow is fine in Python; pick `<=` vs `<` consistently; ensure the loop shrinks.

## Linked Questions

- Tier A: Binary Search, Search Insert Position, Search a 2D Matrix, Find Min in Rotated Sorted Array
- Tier B: Search in Rotated Sorted Array, Koko Eating Bananas, Find First/Last Position, Time Based Key-Value Store
- Tier C: Median of Two Sorted Arrays, Split Array Largest Sum, Capacity to Ship Packages

## Related

- [bisect usage](../00-foundations/03-python-for-interviews.md) · [Two Pointers](two-pointers.md)

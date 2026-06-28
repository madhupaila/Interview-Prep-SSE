# Pattern: Two Pointers

## Recognition Cues (when you see this → reach for two pointers)

- **Sorted** array and you need a **pair / triplet** summing to a target
- Find/remove elements **in place** (no extra array)
- Compare elements from **both ends** (palindrome, container)
- "Without using extra space" on a sorted/linear structure
- Partition / dedupe a sorted array

## Core Idea

Use two indices that move toward each other (opposite ends) or in the same direction (slow/fast) to avoid an O(N^2) nested loop. Sortedness lets you decide which pointer to move.

---

## Templates

### Opposite ends (sorted pair sum)

```python
def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        cur = nums[left] + nums[right]
        if cur == target:
            return [left, right]
        if cur < target:
            left += 1          # need bigger → move left up
        else:
            right -= 1         # need smaller → move right down
    return [-1, -1]
```

### Same direction (in-place write pointer)

```python
def remove_duplicates(nums: list[int]) -> int:
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1
    return write   # new length
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Array is sorted (or you can sort) | Need contiguous-window aggregate → sliding window |
| Pair/triplet/partition problems | Unsorted + need order preserved + O(N) → hashing |
| In-place O(1) space required | Random access by value → hashmap |

## Complexity

- Time: **O(N)** (or O(N log N) if you sort first).
- Space: **O(1)**.

## Variants & Pitfalls

- **3Sum / 4Sum:** fix one index, two-pointer the rest; skip duplicates to avoid repeats.
- **Container With Most Water:** move the pointer at the shorter line.
- Pitfall: forgetting `left < right` (vs `<=`) causes double-counting or self-pairing.

## Linked Questions

- Tier A: Two Sum II, Valid Palindrome, 3Sum, Container With Most Water, Remove Duplicates
- Tier B: 3Sum Closest, 4Sum, Sort Colors, Trapping Rain Water (two-pointer variant)
- Tier C: 4Sum II, Boats to Save People

## Related

- [Sliding Window](sliding-window.md) · [Binary Search](binary-search.md) · [Cue Dictionary](02-cue-dictionary.md)

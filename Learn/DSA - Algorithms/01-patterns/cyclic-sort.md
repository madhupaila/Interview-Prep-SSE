# Pattern: Cyclic Sort

## Recognition Cues

- Array contains numbers in a **known range [1..n]** (or [0..n-1])
- "Find the missing number / duplicate / all missing"
- "First missing positive"
- O(1) extra space expected, input mutable

## Core Idea

Each number `v` belongs at index `v-1` (for 1..n). Repeatedly swap a number to its correct index until every slot holds the right value. Then a single scan reveals missing/duplicate.

---

## Template

```python
def cyclic_sort(nums: list[int]) -> None:
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1                 # for range 1..n
        if 0 <= correct < n and nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1

def find_missing(nums: list[int]) -> int:
    cyclic_sort(nums)
    for i, v in enumerate(nums):
        if v != i + 1:
            return i + 1
    return len(nums) + 1
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Values are a permutation of a known range | Arbitrary unbounded values → hashing |
| In-place O(1) space wanted | Can't mutate input |

## Complexity

- Time: **O(N)** — each swap places one element permanently.
- Space: **O(1)**.

## Variants & Pitfalls

- **First Missing Positive:** ignore values outside [1..n]; place valid ones; scan.
- **Find All Duplicates / Disappeared:** use sign-marking as an alternative.
- Pitfall: swap while `nums[i] != nums[correct]` (compare *values*, not indices) to avoid infinite loops with duplicates.

## Linked Questions

- Tier A: Missing Number, Find All Numbers Disappeared in an Array
- Tier B: Find the Duplicate Number, Find All Duplicates
- Tier C: First Missing Positive, Set Mismatch

## Related

- [Fast & Slow Pointers](fast-slow-pointers.md) · [Arrays & Hashing](../02-data-structures/arrays-hashing.md)

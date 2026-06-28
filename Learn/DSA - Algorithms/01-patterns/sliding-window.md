# Pattern: Sliding Window

## Recognition Cues

- **Contiguous** subarray / substring
- "longest / shortest / max / min / count of" a window satisfying a condition
- Fixed window size **k**, or a variable window with a constraint
- All-positive numbers (for sum windows) — negatives usually break it

## Core Idea

Maintain a window `[left, right]`. Expand `right` to include elements; shrink `left` when the window violates the constraint. Each element enters and leaves once → **O(N)**.

---

## Templates

### Fixed-size window

```python
def max_sum_subarray_k(nums: list[int], k: int) -> int:
    window = sum(nums[:k])
    best = window
    for right in range(k, len(nums)):
        window += nums[right] - nums[right - k]   # slide
        best = max(best, window)
    return best
```

### Variable-size window (longest valid)

```python
from collections import defaultdict

def longest_substring_k_distinct(s: str, k: int) -> int:
    count = defaultdict(int)
    left = best = 0
    for right, ch in enumerate(s):
        count[ch] += 1
        while len(count) > k:               # shrink until valid
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Contiguous window + aggregate/condition | Need non-contiguous subset → DP/backtracking |
| Monotonic effect of adding/removing | Negatives break sum-window monotonicity → prefix sum + hashmap |
| Strings: distinct chars, anagrams | Pair across whole array → two pointers/hashing |

## Complexity

- Time: **O(N)** (each index moves forward only).
- Space: **O(K)** for the window's frequency map.

## Variants & Pitfalls

- **Minimum window** (shrink while valid, record min) vs **maximum window** (shrink while invalid).
- **Anagram / permutation in string:** fixed window + frequency match.
- Pitfall: deleting zero-count keys so `len(count)` reflects distinct elements.

## Linked Questions

- Tier A: Best Time to Buy/Sell Stock, Longest Substring Without Repeating, Longest Repeating Char Replacement, Permutation in String
- Tier B: Minimum Window Substring, Fruit Into Baskets, Max Consecutive Ones III
- Tier C: Sliding Window Maximum (monotonic deque), Substring with Concatenation of All Words

## Related

- [Two Pointers](two-pointers.md) · [Prefix Sum](prefix-sum.md) · [Monotonic Stack](monotonic-stack.md)

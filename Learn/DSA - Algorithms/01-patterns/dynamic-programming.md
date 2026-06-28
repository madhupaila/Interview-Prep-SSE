# Pattern: Dynamic Programming

## Recognition Cues

- "**Number of ways**", "min/max cost", "longest/shortest …"
- **Overlapping subproblems** + **optimal substructure**
- "Can you reach / partition / make change"
- Naive recursion recomputes the same state → memoize

## Core Idea

Define a **state** that captures a subproblem, write a **recurrence** relating it to smaller states, then either memoize (top-down) or fill a table (bottom-up). The art is choosing the state.

---

## Sub-families & Templates

### Top-down memoization (general)

```python
from functools import cache

def solve(n):
    @cache
    def dp(i):
        if i <= 1:
            return base_value
        return combine(dp(i - 1), dp(i - 2))   # recurrence
    return dp(n)
```

### 1D — Climbing Stairs / House Robber

```python
def rob(nums: list[int]) -> int:
    prev = cur = 0
    for n in nums:
        prev, cur = cur, max(cur, prev + n)
    return cur
```

### 0/1 Knapsack (2D → 1D)

```python
def knapsack(weights, values, cap):
    dp = [0] * (cap + 1)
    for w, v in zip(weights, values):
        for c in range(cap, w - 1, -1):        # reverse → each item once
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[cap]
```

### 2D grid / strings (edit distance, LCS)

```python
def longest_common_subsequence(a: str, b: str) -> int:
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[-1][-1]
```

### LIS (patience / binary search, O(N log N))

```python
import bisect

def length_of_lis(nums):
    tails = []
    for n in nums:
        i = bisect.bisect_left(tails, n)
        if i == len(tails):
            tails.append(n)
        else:
            tails[i] = n
    return len(tails)
```

---

## DP Recipe (say this in interview)

1. **State:** what does `dp[i]` / `dp[i][j]` mean?
2. **Recurrence:** how does it build from smaller states?
3. **Base cases.**
4. **Order** of computation (or memoize).
5. **Answer** location + **space optimization** (rolling array).

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Overlapping subproblems + optimal substructure | Greedy choice provably works → greedy |
| Count/optimize over choices | Need all configurations → backtracking |

## Complexity

- Usually **states × transition cost**: O(N), O(N·K), O(N·M), O(N^2).

## Variants & Pitfalls

- 1D (stairs, rob, decode ways), knapsack (coin change, partition), 2D strings (edit distance, LCS, distinct subsequences), intervals (burst balloons, MCM), grid (unique paths, min path sum), LIS.
- Pitfall: knapsack inner loop reversed for 0/1; forward for unbounded.

## Linked Questions

- Tier A: Climbing Stairs, House Robber, Coin Change, Longest Increasing Subsequence, Unique Paths, Word Break
- Tier B: House Robber II, Decode Ways, Partition Equal Subset Sum, LCS, Edit Distance, Maximal Square
- Tier C: Burst Balloons, Regular Expression Matching, Distinct Subsequences, Best Time to Buy/Sell with Cooldown

## Related

- [Greedy](greedy.md) · [Backtracking](backtracking.md) · [memoization with @cache](../00-foundations/03-python-for-interviews.md)

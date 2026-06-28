# Pattern: Greedy

## Recognition Cues

- "Maximum/minimum number of …" where a **local** best seems to lead to global best
- "Sort, then pick"
- Scheduling, intervals, jumps, assigning resources
- You can prove an **exchange argument** (swapping to greedy choice never hurts)

## Core Idea

Make the locally optimal choice at each step, hoping it yields a global optimum. Works **only** when the problem has the greedy-choice property — otherwise use DP. Often paired with sorting.

---

## Templates

### Jump Game (reach end)

```python
def can_jump(nums: list[int]) -> bool:
    reach = 0
    for i, n in enumerate(nums):
        if i > reach:
            return False
        reach = max(reach, i + n)
    return True
```

### Interval scheduling (max non-overlapping)

```python
def max_non_overlapping(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])     # earliest end first
    count, end = 0, float('-inf')
    for s, e in intervals:
        if s >= end:
            count += 1
            end = e
    return count
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Greedy-choice property holds (provable) | Counterexample exists → DP |
| Sort then linear pick | Need to consider combinations → backtracking/DP |

## Complexity

- Usually **O(N log N)** (sort) + O(N) scan. Space O(1)–O(N).

## Variants & Pitfalls

- **Jump Game I/II**, **Gas Station**, **Task Scheduler**, **Partition Labels**, **Non-overlapping Intervals**, **Merge to fewest arrows**.
- Pitfall: greedy is **tempting but wrong** for many problems (e.g., coin change with arbitrary coins) — verify with a counterexample or fall back to DP.

## Linked Questions

- Tier A: Jump Game, Maximum Subarray (Kadane), Gas Station
- Tier B: Jump Game II, Partition Labels, Task Scheduler, Non-overlapping Intervals
- Tier C: Candy, Minimum Number of Refueling Stops, Course Schedule III

## Related

- [Dynamic Programming](dynamic-programming.md) · [Merge Intervals](merge-intervals.md)

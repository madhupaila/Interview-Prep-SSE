# Pattern: Monotonic Stack

## Recognition Cues

- "**Next greater / next smaller** element"
- "**Previous** greater/smaller", "days until warmer"
- Histogram / "largest rectangle", "trapping rain water"
- Need nearest boundary where some comparison flips

## Core Idea

Keep a stack whose values are **monotonic** (increasing or decreasing). When the incoming element breaks the order, pop — each popped element has just found its "next greater/smaller". Each element is pushed and popped once → O(N).

---

## Templates

### Next greater element (to the right)

```python
def next_greater(nums: list[int]) -> list[int]:
    res = [-1] * len(nums)
    stack = []                       # holds indices, values decreasing
    for i, n in enumerate(nums):
        while stack and nums[stack[-1]] < n:
            res[stack.pop()] = n     # n is the next greater for that index
        stack.append(i)
    return res
```

### Largest rectangle in histogram

```python
def largest_rectangle(heights: list[int]) -> int:
    stack = []                       # increasing heights (indices)
    best = 0
    heights.append(0)                # sentinel flushes the stack
    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            best = max(best, height * width)
        stack.append(i)
    return best
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Nearest greater/smaller boundary | Aggregate over fixed window → sliding window |
| Histogram/area, temperatures | No comparison-boundary structure |

## Complexity

- Time: **O(N)** (amortized — each index pushed/popped once).
- Space: **O(N)** stack.

## Variants & Pitfalls

- **Daily Temperatures**, **Next Greater Element I/II (circular)**, **Trapping Rain Water**, **Largest Rectangle**, **Remove K Digits / Build min number**.
- Pitfall: decide increasing vs decreasing stack based on whether you want next-greater or next-smaller; store **indices** when you need distances.

## Linked Questions

- Tier A: Daily Temperatures, Next Greater Element I, Valid Parentheses (stack)
- Tier B: Next Greater Element II, Online Stock Span, Remove K Digits
- Tier C: Largest Rectangle in Histogram, Maximal Rectangle, Trapping Rain Water

## Related

- [Stack & Queue DS](../02-data-structures/stack-queue.md) · [Sliding Window](sliding-window.md)

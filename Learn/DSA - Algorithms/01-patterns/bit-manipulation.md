# Pattern: Bit Manipulation

## Recognition Cues

- "Single number", "appears once/twice/thrice"
- "Count set bits", "power of two", "missing number"
- Subsets via bitmask, state compression in DP
- Constant-space tricks with XOR/AND/OR

## Core Idea

Use bitwise operators to encode sets, toggle/test bits, and exploit XOR's self-cancellation (`x ^ x = 0`, `x ^ 0 = x`).

---

## Essential Tricks

```python
x & 1                      # is odd / lowest bit
x >> 1                     # divide by 2
x << 1                     # multiply by 2
x & (x - 1)                # clears lowest set bit
x & (-x)                   # isolates lowest set bit
bin(x).count('1')          # popcount (or x.bit_count() in 3.10+)
x | (1 << i)               # set bit i
x & ~(1 << i)              # clear bit i
x ^ (1 << i)               # toggle bit i
(x >> i) & 1               # test bit i
```

### Single number (XOR)

```python
def single_number(nums: list[int]) -> int:
    res = 0
    for n in nums:
        res ^= n            # pairs cancel, the unique remains
    return res
```

### Missing number (XOR all indices and values)

```python
def missing_number(nums):
    res = len(nums)
    for i, n in enumerate(nums):
        res ^= i ^ n
    return res
```

### Iterate all subsets via bitmask

```python
for mask in range(1 << n):
    subset = [a[i] for i in range(n) if mask & (1 << i)]
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Set membership in small universe (≤ ~20–30) | Large universe → use a set |
| XOR cancellation, counting bits | Readability matters more than micro-opt |

## Complexity

- Most ops **O(1)**; iterating subsets **O(2^N)**.

## Variants & Pitfalls

- **Single Number I/II/III**, **Number of 1 Bits**, **Counting Bits**, **Power of Two**, **Sum of Two Integers** (no `+`), **Bitmask DP** (TSP, assign tasks).
- Pitfall: Python ints are unbounded — for fixed-width simulation mask with `& 0xFFFFFFFF`.

## Linked Questions

- Tier A: Single Number, Number of 1 Bits, Counting Bits, Missing Number, Reverse Bits
- Tier B: Single Number II, Sum of Two Integers, Power of Two
- Tier C: Single Number III, Maximum XOR of Two Numbers, Bitmask DP problems

## Related

- [Subsets & Combinations](subsets-combinations.md) · [Math Tricks](math-tricks.md)

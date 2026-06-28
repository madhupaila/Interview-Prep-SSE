# -*- coding: utf-8 -*-
"""Bit Manipulation questions."""

QUESTIONS = [
    {
        "slug": "single-number", "title": "Single Number", "pattern": "bit-manipulation", "tier": "A",
        "companies": "Amazon, Google, Meta", "difficulty": "Easy", "leetcode": 136,
        "cue": "Every element twice except one → XOR all (pairs cancel)",
        "problem": "Every element appears twice except one. Find it in O(N)/O(1).",
        "solution": '''def single_number(nums: list[int]) -> int:
    res = 0
    for n in nums:
        res ^= n
    return res''',
        "time": "O(N)", "space": "O(1)",
        "related": ["single-number-ii", "single-number-iii"],
    },
    {
        "slug": "number-of-1-bits", "title": "Number of 1 Bits", "pattern": "bit-manipulation", "tier": "A",
        "companies": "Amazon, Apple, Microsoft", "difficulty": "Easy", "leetcode": 191,
        "cue": "Count set bits → x & (x-1) clears lowest set bit",
        "problem": "Return the number of 1 bits (Hamming weight) of an integer.",
        "solution": '''def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1                               # drop lowest set bit
        count += 1
    return count''',
        "time": "O(set bits)", "space": "O(1)",
        "related": ["counting-bits"],
    },
    {
        "slug": "counting-bits", "title": "Counting Bits", "pattern": "bit-manipulation", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 338,
        "cue": "Bits for 0..n → dp[i] = dp[i>>1] + (i&1)",
        "problem": "Return an array where `ans[i]` is the number of 1 bits in `i`, for `0..n`.",
        "solution": '''def count_bits(n: int) -> list[int]:
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i >> 1] + (i & 1)
    return dp''',
        "time": "O(N)", "space": "O(N)",
        "related": ["number-of-1-bits"],
    },
    {
        "slug": "missing-number-xor", "title": "Missing Number (XOR)", "pattern": "bit-manipulation", "tier": "A",
        "companies": "Amazon, Microsoft", "difficulty": "Easy", "leetcode": 268,
        "cue": "Missing in 0..n → XOR indices with values",
        "problem": "Find the missing number in [0, n] using XOR.",
        "solution": '''def missing_number(nums: list[int]) -> int:
    res = len(nums)
    for i, n in enumerate(nums):
        res ^= i ^ n
    return res''',
        "time": "O(N)", "space": "O(1)",
        "related": ["single-number", "missing-number"],
    },
    {
        "slug": "reverse-bits", "title": "Reverse Bits", "pattern": "bit-manipulation", "tier": "A",
        "companies": "Amazon, Apple", "difficulty": "Easy", "leetcode": 190,
        "cue": "Reverse 32-bit integer → shift result, pull lowest bit",
        "problem": "Reverse the bits of a 32-bit unsigned integer.",
        "solution": '''def reverse_bits(n: int) -> int:
    res = 0
    for _ in range(32):
        res = (res << 1) | (n & 1)
        n >>= 1
    return res''',
        "time": "O(1)", "space": "O(1)",
        "related": ["number-of-1-bits"],
    },
    {
        "slug": "sum-of-two-integers", "title": "Sum of Two Integers", "pattern": "bit-manipulation", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 371,
        "cue": "Add without + → XOR sum, AND<<1 carry, mask 32-bit",
        "problem": "Compute `a + b` without using `+` or `-`.",
        "solution": '''def get_sum(a: int, b: int) -> int:
    mask = 0xFFFFFFFF
    while b & mask:
        carry = (a & b) << 1
        a = a ^ b
        b = carry
    a &= mask
    # handle negative (two's complement) for 32-bit
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)''',
        "time": "O(1)", "space": "O(1)",
        "related": ["single-number"],
    },
    {
        "slug": "single-number-ii", "title": "Single Number II", "pattern": "bit-manipulation", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 137,
        "cue": "All thrice except one → count bits mod 3 (or two-state machine)",
        "problem": "Every element appears three times except one. Find it in O(N)/O(1).",
        "solution": '''def single_number(nums: list[int]) -> int:
    ones = twos = 0
    for n in nums:
        ones = (ones ^ n) & ~twos
        twos = (twos ^ n) & ~ones
    return ones''',
        "time": "O(N)", "space": "O(1)",
        "related": ["single-number", "single-number-iii"],
    },
    {
        "slug": "power-of-two", "title": "Power of Two", "pattern": "bit-manipulation", "tier": "B",
        "companies": "Amazon, Apple", "difficulty": "Easy", "leetcode": 231,
        "cue": "Is power of two → exactly one set bit: n & (n-1) == 0",
        "problem": "Return True if `n` is a power of two.",
        "solution": '''def is_power_of_two(n: int) -> bool:
    return n > 0 and (n & (n - 1)) == 0''',
        "time": "O(1)", "space": "O(1)",
        "related": ["number-of-1-bits"],
    },
    {
        "slug": "single-number-iii", "title": "Single Number III", "pattern": "bit-manipulation", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 260,
        "cue": "Two uniques among pairs → XOR all, split by a differing bit",
        "problem": "Exactly two elements appear once (rest twice). Return both.",
        "solution": '''def single_number(nums: list[int]) -> list[int]:
    xor = 0
    for n in nums:
        xor ^= n
    diff = xor & (-xor)                          # lowest set bit where they differ
    a = b = 0
    for n in nums:
        if n & diff:
            a ^= n
        else:
            b ^= n
    return [a, b]''',
        "time": "O(N)", "space": "O(1)",
        "identify": "XOR of all leaves a^b; a set bit in it differs between the two — partition numbers by that bit and XOR each group.",
        "related": ["single-number", "single-number-ii"],
    },
    {
        "slug": "maximum-xor-of-two-numbers", "title": "Maximum XOR of Two Numbers in an Array", "pattern": "bit-manipulation", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 421,
        "cue": "Max pairwise XOR → build prefix greedily bit by bit",
        "problem": "Return the maximum XOR of any two numbers in the array.",
        "solution": '''def find_maximum_xor(nums: list[int]) -> int:
    max_xor = 0
    mask = 0
    for i in range(31, -1, -1):
        mask |= (1 << i)
        prefixes = {n & mask for n in nums}
        candidate = max_xor | (1 << i)
        if any(candidate ^ p in prefixes for p in prefixes):
            max_xor = candidate
    return max_xor''',
        "time": "O(32·N)", "space": "O(N)",
        "related": ["single-number-iii"],
    },
]

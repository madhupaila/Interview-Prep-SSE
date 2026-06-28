# -*- coding: utf-8 -*-
"""Prefix Sum questions."""

QUESTIONS = [
    {
        "slug": "range-sum-query-immutable", "title": "Range Sum Query - Immutable", "pattern": "prefix-sum", "tier": "A",
        "companies": "Amazon, Facebook", "difficulty": "Easy", "leetcode": 303,
        "cue": "Many range-sum queries, no updates → precompute prefix sums",
        "problem": "Implement `sumRange(i, j)` over an immutable array with O(1) per query.",
        "solution": '''class NumArray:
    def __init__(self, nums: list[int]):
        self.prefix = [0]
        for n in nums:
            self.prefix.append(self.prefix[-1] + n)

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix[j + 1] - self.prefix[i]''',
        "time": "O(1) query, O(N) build", "space": "O(N)",
        "related": ["range-sum-query-2d-immutable", "subarray-sum-equals-k"],
    },
    {
        "slug": "product-of-array-except-self", "title": "Product of Array Except Self", "pattern": "prefix-sum", "tier": "A",
        "companies": "Amazon, Meta, Microsoft, Apple", "difficulty": "Medium", "leetcode": 238,
        "cue": "Each index = product of others → prefix product × suffix product",
        "problem": "Return an array where `out[i]` is the product of all elements except `nums[i]`, without division, O(N).",
        "approaches": [("Division", "O(N)", "O(1)", "fails on zeros / disallowed"), ("Prefix × suffix", "O(N)", "O(1) extra", "two passes")],
        "solution": '''def product_except_self(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
    suffix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= suffix
        suffix *= nums[i]
    return res''',
        "time": "O(N)", "space": "O(1) extra",
        "edges": ["Contains zero(s)", "Single element"],
        "related": ["range-sum-query-immutable"],
    },
    {
        "slug": "subarray-sum-equals-k", "title": "Subarray Sum Equals K", "pattern": "prefix-sum", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 560,
        "cue": "Count subarrays summing to K (negatives!) → prefix sum + hashmap of counts",
        "problem": "Return the number of contiguous subarrays whose sum equals `k`.",
        "approaches": [("Brute force", "O(N^2)", "O(1)", "all subarrays"), ("Prefix + hashmap", "O(N)", "O(N)", "count[prefix-k]")],
        "identify": "Negatives rule out sliding window. prefix[j]-prefix[i]=k ⇒ for each j add the count of prefix value (prefix-k) seen so far.",
        "solution": '''from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    seen = defaultdict(int)
    seen[0] = 1
    prefix = count = 0
    for n in nums:
        prefix += n
        count += seen[prefix - k]
        seen[prefix] += 1
    return count''',
        "time": "O(N)", "space": "O(N)",
        "edges": ["Negative numbers", "k = 0", "Seed seen[0]=1 for prefixes from index 0"],
        "related": ["contiguous-array", "subarray-sums-divisible-by-k"],
    },
    {
        "slug": "find-pivot-index", "title": "Find Pivot Index", "pattern": "prefix-sum", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 724,
        "cue": "Left sum == right sum → total minus prefix",
        "problem": "Return the leftmost index where the sum to the left equals the sum to the right.",
        "solution": '''def pivot_index(nums: list[int]) -> int:
    total = sum(nums)
    left = 0
    for i, n in enumerate(nums):
        if left == total - left - n:
            return i
        left += n
    return -1''',
        "time": "O(N)", "space": "O(1)",
        "related": ["range-sum-query-immutable"],
    },
    {
        "slug": "contiguous-array", "title": "Contiguous Array", "pattern": "prefix-sum", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 525,
        "cue": "Longest subarray equal #0s and #1s → map 0→-1, first index of each prefix",
        "problem": "Return the max length of a contiguous subarray with equal numbers of 0 and 1.",
        "solution": '''def find_max_length(nums: list[int]) -> int:
    first = {0: -1}
    prefix = best = 0
    for i, n in enumerate(nums):
        prefix += 1 if n == 1 else -1
        if prefix in first:
            best = max(best, i - first[prefix])
        else:
            first[prefix] = i
    return best''',
        "time": "O(N)", "space": "O(N)",
        "identify": "Map 0→-1 so 'equal counts' becomes 'subarray sum 0'; track the first index of each prefix to maximize length.",
        "related": ["subarray-sum-equals-k"],
    },
    {
        "slug": "subarray-sums-divisible-by-k", "title": "Subarray Sums Divisible by K", "pattern": "prefix-sum", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 974,
        "cue": "Count subarrays with sum % k == 0 → bucket prefix remainders",
        "problem": "Count contiguous subarrays whose sum is divisible by `k`.",
        "solution": '''from collections import defaultdict

def subarrays_div_by_k(nums: list[int], k: int) -> int:
    count = defaultdict(int)
    count[0] = 1
    prefix = res = 0
    for n in nums:
        prefix = (prefix + n) % k
        res += count[prefix]
        count[prefix] += 1
    return res''',
        "time": "O(N)", "space": "O(k)",
        "edges": ["Negative numbers (Python % is non-negative)", "Equal remainders form valid subarrays"],
        "related": ["subarray-sum-equals-k"],
    },
    {
        "slug": "range-sum-query-2d-immutable", "title": "Range Sum Query 2D - Immutable", "pattern": "prefix-sum", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 304,
        "cue": "Submatrix sum queries → 2D prefix sums (inclusion-exclusion)",
        "problem": "Return the sum of a submatrix `(r1,c1)..(r2,c2)` in O(1) after preprocessing.",
        "solution": '''class NumMatrix:
    def __init__(self, matrix: list[list[int]]):
        R, C = len(matrix), len(matrix[0])
        self.P = [[0] * (C + 1) for _ in range(R + 1)]
        for r in range(R):
            for c in range(C):
                self.P[r+1][c+1] = (matrix[r][c] + self.P[r][c+1]
                                    + self.P[r+1][c] - self.P[r][c])

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        P = self.P
        return P[r2+1][c2+1] - P[r1][c2+1] - P[r2+1][c1] + P[r1][c1]''',
        "time": "O(1) query, O(R·C) build", "space": "O(R·C)",
        "related": ["range-sum-query-immutable"],
    },
    {
        "slug": "maximum-size-subarray-sum-equals-k", "title": "Maximum Size Subarray Sum Equals k", "pattern": "prefix-sum", "tier": "C",
        "companies": "Amazon, Facebook, Palantir", "difficulty": "Medium", "leetcode": 325,
        "cue": "Longest subarray with sum k (negatives) → first-seen prefix index map",
        "problem": "Return the maximum length of a subarray summing to `k`.",
        "solution": '''def max_subarray_len(nums: list[int], k: int) -> int:
    first = {0: -1}
    prefix = best = 0
    for i, n in enumerate(nums):
        prefix += n
        if prefix - k in first:
            best = max(best, i - first[prefix - k])
        if prefix not in first:
            first[prefix] = i
    return best''',
        "time": "O(N)", "space": "O(N)",
        "related": ["subarray-sum-equals-k", "contiguous-array"],
    },
    {
        "slug": "count-nice-subarrays", "title": "Count Number of Nice Subarrays", "pattern": "prefix-sum", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 1248,
        "cue": "Exactly k odd numbers → prefix count of odds + hashmap",
        "problem": "Count subarrays with exactly `k` odd numbers.",
        "solution": '''from collections import defaultdict

def number_of_subarrays(nums: list[int], k: int) -> int:
    count = defaultdict(int)
    count[0] = 1
    odds = res = 0
    for n in nums:
        odds += n & 1
        res += count[odds - k]
        count[odds] += 1
    return res''',
        "time": "O(N)", "space": "O(N)",
        "identify": "Replace 'sum' with 'count of odds'; it's Subarray Sum Equals K on parity.",
        "related": ["subarray-sum-equals-k"],
    },
]

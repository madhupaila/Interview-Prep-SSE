# -*- coding: utf-8 -*-
"""Binary Search questions."""

QUESTIONS = [
    {
        "slug": "binary-search", "title": "Binary Search", "pattern": "binary-search", "tier": "A",
        "companies": "Amazon, Google, Microsoft", "difficulty": "Easy", "leetcode": 704,
        "cue": "Sorted + find target → classic halving",
        "problem": "Return the index of `target` in a sorted array, or -1.",
        "solution": '''def search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1''',
        "time": "O(log N)", "space": "O(1)",
        "related": ["search-insert-position", "find-first-last-position"],
    },
    {
        "slug": "search-insert-position", "title": "Search Insert Position", "pattern": "binary-search", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 35,
        "cue": "Insertion index in sorted → lower bound",
        "problem": "Return the index where `target` is or would be inserted in sorted order.",
        "solution": '''def search_insert(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid
    return lo''',
        "time": "O(log N)", "space": "O(1)",
        "related": ["binary-search"],
    },
    {
        "slug": "search-2d-matrix", "title": "Search a 2D Matrix", "pattern": "binary-search", "tier": "A",
        "companies": "Amazon, Microsoft, Google", "difficulty": "Medium", "leetcode": 74,
        "cue": "Row-sorted matrix, globally sorted → binary search on flattened index",
        "problem": "Search a target in an `m×n` matrix sorted row-wise where each row's first > prev row's last.",
        "solution": '''def search_matrix(matrix: list[list[int]], target: int) -> bool:
    rows, cols = len(matrix), len(matrix[0])
    lo, hi = 0, rows * cols - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        val = matrix[mid // cols][mid % cols]
        if val == target:
            return True
        if val < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return False''',
        "time": "O(log(M·N))", "space": "O(1)",
        "related": ["search-2d-matrix-ii", "binary-search"],
    },
    {
        "slug": "find-min-rotated-sorted", "title": "Find Minimum in Rotated Sorted Array", "pattern": "binary-search", "tier": "A",
        "companies": "Amazon, Microsoft, Meta", "difficulty": "Medium", "leetcode": 153,
        "cue": "Rotated sorted → compare mid with right to find the pivot",
        "problem": "Return the minimum of a rotated ascending array with distinct values.",
        "solution": '''def find_min(nums: list[int]) -> int:
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1                        # min is to the right
        else:
            hi = mid                            # min is at mid or left
    return nums[lo]''',
        "time": "O(log N)", "space": "O(1)",
        "related": ["search-in-rotated-sorted"],
    },
    {
        "slug": "koko-eating-bananas", "title": "Koko Eating Bananas", "pattern": "binary-search", "tier": "A",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 875,
        "cue": "Minimize an eating speed that fits in h hours → binary search on the answer",
        "problem": "Find the minimum integer eating speed so all piles are eaten within `h` hours.",
        "approaches": [("Linear scan speed", "O(maxPile·N)", "O(1)", "too slow"), ("Binary search on answer", "O(N log maxPile)", "O(1)", "feasible(speed) monotonic")],
        "identify": "feasible(speed) is monotonic (faster speed never needs more hours) → binary search the smallest feasible speed.",
        "solution": '''import math

def min_eating_speed(piles: list[int], h: int) -> int:
    def hours(speed):
        return sum(math.ceil(p / speed) for p in piles)
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours(mid) <= h:
            hi = mid
        else:
            lo = mid + 1
    return lo''',
        "time": "O(N log maxPile)", "space": "O(1)",
        "related": ["capacity-to-ship-packages", "split-array-largest-sum"],
    },
    {
        "slug": "search-in-rotated-sorted", "title": "Search in Rotated Sorted Array", "pattern": "binary-search", "tier": "B",
        "companies": "Amazon, Meta, Microsoft, Bloomberg", "difficulty": "Medium", "leetcode": 33,
        "cue": "Rotated sorted + find target → identify the sorted half each step",
        "problem": "Search `target` in a rotated ascending array of distinct values; return index or -1.",
        "solution": '''def search(nums: list[int], target: int) -> int:
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:               # left half sorted
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:                                   # right half sorted
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1''',
        "time": "O(log N)", "space": "O(1)",
        "edges": ["No rotation", "Target absent", "Duplicates → O(N) worst (variant II)"],
        "related": ["find-min-rotated-sorted"],
    },
    {
        "slug": "find-first-last-position", "title": "Find First and Last Position of Element", "pattern": "binary-search", "tier": "B",
        "companies": "Amazon, Meta, LinkedIn", "difficulty": "Medium", "leetcode": 34,
        "cue": "Range of a value in sorted → two boundary searches",
        "problem": "Return the first and last index of `target` in a sorted array, or [-1, -1].",
        "solution": '''def search_range(nums: list[int], target: int) -> list[int]:
    def bound(is_left):
        lo, hi, res = 0, len(nums) - 1, -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                res = mid
                if is_left:
                    hi = mid - 1
                else:
                    lo = mid + 1
        return res
    return [bound(True), bound(False)]''',
        "time": "O(log N)", "space": "O(1)",
        "related": ["binary-search"],
    },
    {
        "slug": "time-based-key-value-store", "title": "Time Based Key-Value Store", "pattern": "binary-search", "tier": "B",
        "companies": "Amazon, Google, Uber", "difficulty": "Medium", "leetcode": 981,
        "cue": "Latest value at or before a timestamp → binary search on sorted timestamps",
        "problem": "Design a store with `set(key, value, ts)` and `get(key, ts)` returning the value with the largest ts ≤ query.",
        "solution": '''from collections import defaultdict
import bisect

class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)          # key -> [(ts, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.store[key]
        i = bisect.bisect_right(arr, (timestamp, chr(127)))
        return arr[i - 1][1] if i else ""''',
        "time": "O(log N) get", "space": "O(N)",
        "related": ["search-insert-position"],
    },
    {
        "slug": "capacity-to-ship-packages", "title": "Capacity To Ship Packages Within D Days", "pattern": "binary-search", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 1011,
        "cue": "Minimize capacity to ship within D days → binary search on capacity",
        "problem": "Find the least ship capacity to deliver all packages (in order) within `days`.",
        "solution": '''def ship_within_days(weights: list[int], days: int) -> int:
    def needed(cap):
        d, cur = 1, 0
        for w in weights:
            if cur + w > cap:
                d += 1
                cur = 0
            cur += w
        return d
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if needed(mid) <= days:
            hi = mid
        else:
            lo = mid + 1
    return lo''',
        "time": "O(N log sum)", "space": "O(1)",
        "related": ["koko-eating-bananas", "split-array-largest-sum"],
    },
    {
        "slug": "median-of-two-sorted-arrays", "title": "Median of Two Sorted Arrays", "pattern": "binary-search", "tier": "C",
        "companies": "Amazon, Google, Microsoft, Adobe", "difficulty": "Hard", "leetcode": 4,
        "cue": "Median across two sorted arrays in O(log) → partition smaller array",
        "problem": "Return the median of two sorted arrays in O(log(m+n)).",
        "identify": "Binary search the partition of the smaller array so left halves of both ≤ right halves; median sits at the boundary.",
        "solution": '''def find_median_sorted_arrays(a: list[int], b: list[int]) -> float:
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    half = (m + n + 1) // 2
    lo, hi = 0, m
    while lo <= hi:
        i = (lo + hi) // 2                       # cut in a
        j = half - i                             # cut in b
        a_left = a[i - 1] if i > 0 else float('-inf')
        a_right = a[i] if i < m else float('inf')
        b_left = b[j - 1] if j > 0 else float('-inf')
        b_right = b[j] if j < n else float('inf')
        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2:
                return max(a_left, b_left)
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1
    return 0.0''',
        "time": "O(log min(M,N))", "space": "O(1)",
        "related": ["kth-smallest-in-sorted-matrix"],
    },
    {
        "slug": "split-array-largest-sum", "title": "Split Array Largest Sum", "pattern": "binary-search", "tier": "C",
        "companies": "Amazon, Google, Meta", "difficulty": "Hard", "leetcode": 410,
        "cue": "Minimize the maximum subarray sum over k splits → binary search on the max",
        "problem": "Split `nums` into `k` non-empty contiguous subarrays minimizing the largest subarray sum.",
        "solution": '''def split_array(nums: list[int], k: int) -> int:
    def splits(cap):
        cnt, cur = 1, 0
        for n in nums:
            if cur + n > cap:
                cnt += 1
                cur = 0
            cur += n
        return cnt
    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if splits(mid) <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo''',
        "time": "O(N log sum)", "space": "O(1)",
        "related": ["capacity-to-ship-packages", "koko-eating-bananas"],
    },
]

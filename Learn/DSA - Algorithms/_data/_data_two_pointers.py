# -*- coding: utf-8 -*-
"""Two Pointers questions."""

QUESTIONS = [
    {
        "slug": "valid-palindrome", "title": "Valid Palindrome", "pattern": "two-pointers", "tier": "A",
        "companies": "Meta, Amazon, Microsoft", "difficulty": "Easy", "leetcode": 125,
        "cue": "Compare from both ends → two pointers inward",
        "problem": "Return True if `s` is a palindrome considering only alphanumeric characters, ignoring case.",
        "solution": '''def is_palindrome(s: str) -> bool:
    i, j = 0, len(s) - 1
    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False
        i += 1; j -= 1
    return True''',
        "time": "O(N)", "space": "O(1)",
        "edges": ["Empty string → True", "Only punctuation → True", "Mixed case"],
        "related": ["valid-palindrome-ii", "two-sum-ii"],
    },
    {
        "slug": "two-sum-ii", "title": "Two Sum II (Sorted Input)", "pattern": "two-pointers", "tier": "A",
        "companies": "Amazon, Google, Bloomberg", "difficulty": "Medium", "leetcode": 167,
        "cue": "Sorted + pair sum → move pointer by comparison (O(1) space)",
        "problem": "Given a 1-indexed sorted array, return indices of two numbers adding to `target`.",
        "approaches": [("Hashmap", "O(N)", "O(N)", "ignores sortedness"), ("Two pointers", "O(N)", "O(1)", "exploit sorted order")],
        "solution": '''def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    lo, hi = 0, len(numbers) - 1
    while lo < hi:
        s = numbers[lo] + numbers[hi]
        if s == target:
            return [lo + 1, hi + 1]
        if s < target:
            lo += 1
        else:
            hi -= 1
    return []''',
        "time": "O(N)", "space": "O(1)",
        "related": ["two-sum", "3sum"],
    },
    {
        "slug": "3sum", "title": "3Sum", "pattern": "two-pointers", "tier": "A",
        "companies": "Meta, Amazon, Microsoft, Adobe", "difficulty": "Medium", "leetcode": 15,
        "cue": "Triplets summing to 0 → sort + fix one + two-pointer the rest",
        "problem": "Return all unique triplets `[a,b,c]` with `a+b+c == 0`.",
        "approaches": [("Brute force", "O(N^3)", "O(1)", "all triplets"), ("Sort + two pointers", "O(N^2)", "O(1)", "fix i, scan pair; skip dups")],
        "identify": "Pair-sum-to-target with two pointers, wrapped in a loop fixing the first element. Sorting enables both the two-pointer scan and duplicate skipping.",
        "solution": '''def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue                          # skip duplicate anchors
        if nums[i] > 0:
            break                             # no positive triple sums to 0
        lo, hi = i + 1, n - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s < 0:
                lo += 1
            elif s > 0:
                hi -= 1
            else:
                res.append([nums[i], nums[lo], nums[hi]])
                lo += 1; hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
    return res''',
        "time": "O(N^2)", "space": "O(1)",
        "edges": ["Fewer than 3 elements", "All zeros → one triplet", "Duplicates must be skipped"],
        "followups": ["3Sum Closest", "4Sum", "3Sum Smaller (count)"],
        "related": ["3sum-closest", "4sum", "two-sum-ii"],
    },
    {
        "slug": "container-with-most-water", "title": "Container With Most Water", "pattern": "two-pointers", "tier": "A",
        "companies": "Amazon, Google, Meta", "difficulty": "Medium", "leetcode": 11,
        "cue": "Max area between two lines → ends inward, move the shorter",
        "problem": "Given heights, find two lines forming a container holding the most water.",
        "solution": '''def max_area(height: list[int]) -> int:
    lo, hi = 0, len(height) - 1
    best = 0
    while lo < hi:
        best = max(best, (hi - lo) * min(height[lo], height[hi]))
        if height[lo] < height[hi]:
            lo += 1                          # moving the shorter may help
        else:
            hi -= 1
    return best''',
        "time": "O(N)", "space": "O(1)",
        "identify": "Width shrinks each step, so we only gain by increasing the limiting (shorter) height — move that pointer.",
        "related": ["trapping-rain-water"],
    },
    {
        "slug": "remove-duplicates-sorted", "title": "Remove Duplicates from Sorted Array", "pattern": "two-pointers", "tier": "A",
        "companies": "Amazon, Microsoft, Adobe", "difficulty": "Easy", "leetcode": 26,
        "cue": "In-place compaction → slow write pointer, fast read pointer",
        "problem": "Remove duplicates in place from a sorted array; return the new length.",
        "solution": '''def remove_duplicates(nums: list[int]) -> int:
    if not nums:
        return 0
    write = 1
    for read in range(1, len(nums)):
        if nums[read] != nums[write - 1]:
            nums[write] = nums[read]
            write += 1
    return write''',
        "time": "O(N)", "space": "O(1)",
        "related": ["remove-element", "move-zeroes"],
    },
    {
        "slug": "move-zeroes", "title": "Move Zeroes", "pattern": "two-pointers", "tier": "A",
        "companies": "Meta, Amazon, Bloomberg", "difficulty": "Easy", "leetcode": 283,
        "cue": "Partition in place keeping order → write pointer for non-zeros",
        "problem": "Move all 0s to the end while keeping the relative order of non-zero elements, in place.",
        "solution": '''def move_zeroes(nums: list[int]) -> None:
    write = 0
    for read in range(len(nums)):
        if nums[read] != 0:
            nums[write], nums[read] = nums[read], nums[write]
            write += 1''',
        "time": "O(N)", "space": "O(1)",
        "related": ["remove-duplicates-sorted"],
    },
    {
        "slug": "merge-sorted-array", "title": "Merge Sorted Array", "pattern": "two-pointers", "tier": "A",
        "companies": "Meta, Microsoft, Amazon", "difficulty": "Easy", "leetcode": 88,
        "cue": "Merge in place from the back → avoid overwriting",
        "problem": "Merge `nums2` into `nums1` (which has trailing space) in sorted order, in place.",
        "solution": '''def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]; i -= 1
        else:
            nums1[k] = nums2[j]; j -= 1
        k -= 1''',
        "time": "O(M+N)", "space": "O(1)",
        "edges": ["nums2 empty", "All nums2 smaller", "Fill from the end to avoid clobbering"],
        "related": ["merge-two-sorted-lists"],
    },
    {
        "slug": "3sum-closest", "title": "3Sum Closest", "pattern": "two-pointers", "tier": "B",
        "companies": "Amazon, Bloomberg", "difficulty": "Medium", "leetcode": 16,
        "cue": "Closest triplet sum to target → sort + two pointers tracking best diff",
        "problem": "Return the sum of three integers closest to `target`.",
        "solution": '''def three_sum_closest(nums: list[int], target: int) -> int:
    nums.sort()
    best = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        lo, hi = i + 1, len(nums) - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if abs(s - target) < abs(best - target):
                best = s
            if s < target:
                lo += 1
            elif s > target:
                hi -= 1
            else:
                return s
    return best''',
        "time": "O(N^2)", "space": "O(1)",
        "related": ["3sum", "4sum"],
    },
    {
        "slug": "sort-colors", "title": "Sort Colors (Dutch Flag)", "pattern": "two-pointers", "tier": "B",
        "companies": "Microsoft, Amazon, Meta", "difficulty": "Medium", "leetcode": 75,
        "cue": "Three-way partition (0/1/2) in one pass → low/mid/high pointers",
        "problem": "Sort an array of 0s, 1s, 2s in place in one pass.",
        "solution": '''def sort_colors(nums: list[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1; mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1                          # don't advance mid (swapped-in unknown)
''',
        "time": "O(N)", "space": "O(1)",
        "edges": ["All same color", "Do not advance mid after swapping from high"],
        "related": ["move-zeroes"],
    },
    {
        "slug": "4sum", "title": "4Sum", "pattern": "two-pointers", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 18,
        "cue": "Quadruplets to target → sort + two nested anchors + two pointers",
        "problem": "Return all unique quadruplets summing to `target`.",
        "solution": '''def four_sum(nums: list[int], target: int) -> list[list[int]]:
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            lo, hi = j + 1, n - 1
            while lo < hi:
                s = nums[i] + nums[j] + nums[lo] + nums[hi]
                if s < target:
                    lo += 1
                elif s > target:
                    hi -= 1
                else:
                    res.append([nums[i], nums[j], nums[lo], nums[hi]])
                    lo += 1; hi -= 1
                    while lo < hi and nums[lo] == nums[lo - 1]:
                        lo += 1
                    while lo < hi and nums[hi] == nums[hi + 1]:
                        hi -= 1
    return res''',
        "time": "O(N^3)", "space": "O(1)",
        "related": ["3sum", "3sum-closest"],
    },
    {
        "slug": "is-subsequence", "title": "Is Subsequence", "pattern": "two-pointers", "tier": "B",
        "companies": "Google, Amazon, Pinterest", "difficulty": "Easy", "leetcode": 392,
        "cue": "Is s a subsequence of t → advance one pointer per match",
        "problem": "Return True if `s` is a subsequence of `t`.",
        "solution": '''def is_subsequence(s: str, t: str) -> bool:
    i = 0
    for ch in t:
        if i < len(s) and s[i] == ch:
            i += 1
    return i == len(s)''',
        "time": "O(N)", "space": "O(1)",
        "followups": ["Many queries s against same t → preprocess index lists + binary search"],
        "related": ["two-sum-ii"],
    },
    {
        "slug": "valid-palindrome-ii", "title": "Valid Palindrome II", "pattern": "two-pointers", "tier": "B",
        "companies": "Meta, Amazon", "difficulty": "Easy", "leetcode": 680,
        "cue": "Palindrome with one deletion allowed → branch on first mismatch",
        "problem": "Return True if `s` can become a palindrome by deleting at most one character.",
        "solution": '''def valid_palindrome(s: str) -> bool:
    def is_pal(i, j):
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1; j -= 1
        return True
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return is_pal(i + 1, j) or is_pal(i, j - 1)
        i += 1; j -= 1
    return True''',
        "time": "O(N)", "space": "O(1)",
        "related": ["valid-palindrome"],
    },
    {
        "slug": "boats-to-save-people", "title": "Boats to Save People", "pattern": "two-pointers", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 881,
        "cue": "Pair heaviest with lightest under a limit → sort + two pointers (greedy)",
        "problem": "Each boat carries at most 2 people within `limit` weight. Return the minimum number of boats.",
        "solution": '''def num_rescue_boats(people: list[int], limit: int) -> int:
    people.sort()
    lo, hi = 0, len(people) - 1
    boats = 0
    while lo <= hi:
        if people[lo] + people[hi] <= limit:
            lo += 1
        hi -= 1
        boats += 1
    return boats''',
        "time": "O(N log N)", "space": "O(1)",
        "related": ["two-sum-ii"],
    },
    {
        "slug": "trapping-rain-water-2p", "title": "Trapping Rain Water (Two Pointers)", "pattern": "two-pointers", "tier": "C",
        "companies": "Amazon, Google, Goldman Sachs", "difficulty": "Hard", "leetcode": 42,
        "cue": "Water above bars → two pointers tracking left/right max",
        "problem": "Compute total trapped rainwater given elevation heights.",
        "approaches": [("DP arrays", "O(N)", "O(N)", "prefix max L/R"), ("Two pointers", "O(N)", "O(1)", "move side with smaller max")],
        "solution": '''def trap(height: list[int]) -> int:
    if not height:
        return 0
    lo, hi = 0, len(height) - 1
    left_max, right_max = height[lo], height[hi]
    water = 0
    while lo < hi:
        if left_max < right_max:
            lo += 1
            left_max = max(left_max, height[lo])
            water += left_max - height[lo]
        else:
            hi -= 1
            right_max = max(right_max, height[hi])
            water += right_max - height[hi]
    return water''',
        "time": "O(N)", "space": "O(1)",
        "identify": "Water at a position depends on min(maxLeft, maxRight). Two pointers let the smaller side commit safely.",
        "related": ["container-with-most-water"],
    },
]

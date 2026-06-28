# -*- coding: utf-8 -*-
"""Cyclic Sort questions."""

QUESTIONS = [
    {
        "slug": "missing-number", "title": "Missing Number", "pattern": "cyclic-sort", "tier": "A",
        "companies": "Amazon, Microsoft, Bloomberg", "difficulty": "Easy", "leetcode": 268,
        "cue": "Numbers 0..n with one missing → sum formula or XOR or cyclic placement",
        "problem": "Given `n` distinct numbers in range [0, n], return the missing one.",
        "approaches": [("Sum formula", "O(N)", "O(1)", "n(n+1)/2 - sum"), ("XOR", "O(N)", "O(1)", "xor indices and values")],
        "solution": '''def missing_number(nums: list[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)''',
        "time": "O(N)", "space": "O(1)",
        "related": ["find-all-numbers-disappeared", "first-missing-positive"],
    },
    {
        "slug": "find-all-numbers-disappeared", "title": "Find All Numbers Disappeared in an Array", "pattern": "cyclic-sort", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 448,
        "cue": "Values in 1..n, find all missing → mark indices by sign",
        "problem": "Given `nums` in [1, n], return all values in [1, n] that do not appear.",
        "solution": '''def find_disappeared_numbers(nums: list[int]) -> list[int]:
    for n in nums:
        idx = abs(n) - 1
        if nums[idx] > 0:
            nums[idx] = -nums[idx]              # mark seen
    return [i + 1 for i, n in enumerate(nums) if n > 0]''',
        "time": "O(N)", "space": "O(1)",
        "identify": "Range [1..n] lets us use indices as a hash; sign-marking records presence in O(1) space.",
        "related": ["find-all-duplicates", "missing-number"],
    },
    {
        "slug": "find-all-duplicates", "title": "Find All Duplicates in an Array", "pattern": "cyclic-sort", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 442,
        "cue": "Values 1..n, each once or twice → sign-mark; second hit = duplicate",
        "problem": "Return all values appearing twice in `nums` (values in [1, n]).",
        "solution": '''def find_duplicates(nums: list[int]) -> list[int]:
    res = []
    for n in nums:
        idx = abs(n) - 1
        if nums[idx] < 0:
            res.append(abs(n))
        else:
            nums[idx] = -nums[idx]
    return res''',
        "time": "O(N)", "space": "O(1)",
        "related": ["find-all-numbers-disappeared"],
    },
    {
        "slug": "set-mismatch", "title": "Set Mismatch", "pattern": "cyclic-sort", "tier": "B",
        "companies": "Amazon, Bloomberg", "difficulty": "Easy", "leetcode": 645,
        "cue": "One number duplicated, one missing → cyclic sort then scan",
        "problem": "Find the duplicated number and the missing number in [1, n].",
        "solution": '''def find_error_nums(nums: list[int]) -> list[int]:
    i = 0
    n = len(nums)
    while i < n:
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            nums[i], nums[correct] = nums[correct], nums[i]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return [nums[i], i + 1]            # [duplicate, missing]
    return []''',
        "time": "O(N)", "space": "O(1)",
        "related": ["missing-number", "find-all-duplicates"],
    },
    {
        "slug": "first-missing-positive", "title": "First Missing Positive", "pattern": "cyclic-sort", "tier": "C",
        "companies": "Amazon, Google, Stripe", "difficulty": "Hard", "leetcode": 41,
        "cue": "Smallest absent positive in O(N)/O(1) → place each value at index value-1",
        "problem": "Return the smallest missing positive integer using O(N) time and O(1) space.",
        "approaches": [("Set", "O(N)", "O(N)", "violates space"), ("Cyclic sort", "O(N)", "O(1)", "place value v at index v-1")],
        "identify": "The answer lies in [1, n+1]. Place each valid value at its home index; the first index whose value is wrong reveals the answer.",
        "solution": '''def first_missing_positive(nums: list[int]) -> int:
    n = len(nums)
    i = 0
    while i < n:
        v = nums[i]
        if 1 <= v <= n and nums[v - 1] != v:
            nums[v - 1], nums[i] = nums[i], nums[v - 1]
        else:
            i += 1
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1''',
        "time": "O(N)", "space": "O(1)",
        "edges": ["[1,2,3] → 4", "Values out of range ignored", "Empty → 1"],
        "related": ["missing-number"],
    },
    {
        "slug": "find-the-duplicate-number", "title": "Find the Duplicate Number", "pattern": "cyclic-sort", "tier": "C",
        "companies": "Amazon, Google, Microsoft", "difficulty": "Medium", "leetcode": 287,
        "cue": "One duplicate in 1..n, no mutation → Floyd cycle on value-as-pointer",
        "problem": "Find the single duplicate in `nums` (values in [1, n]) without modifying it, O(1) space.",
        "approaches": [("Sort/set", "O(N)", "O(N)", "mutates or extra space"), ("Floyd cycle", "O(N)", "O(1)", "treat values as next pointers")],
        "solution": '''def find_duplicate(nums: list[int]) -> int:
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow''',
        "time": "O(N)", "space": "O(1)",
        "identify": "Indices→values form a functional graph; a repeated value creates a cycle whose entrance is the duplicate (Floyd).",
        "related": ["linked-list-cycle-ii"],
    },
]

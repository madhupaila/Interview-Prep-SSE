# -*- coding: utf-8 -*-
"""Arrays & Hashing questions."""

QUESTIONS = [
    {
        "slug": "two-sum", "title": "Two Sum", "pattern": "arrays-hashing", "tier": "A",
        "companies": "Google, Amazon, Meta, Microsoft, Apple", "difficulty": "Easy", "leetcode": 1,
        "cue": "Unsorted array + find a pair summing to target → hashmap complement",
        "problem": "Given an array `nums` and an integer `target`, return indices of the two numbers that add up to `target`. Exactly one solution; no element reused.",
        "approaches": [
            ("Brute force", "O(N^2)", "O(1)", "check all pairs"),
            ("Hashmap (one pass)", "O(N)", "O(N)", "store value→index, look up complement"),
        ],
        "identify": "We need a *pair* in an *unsorted* array with O(N). A hashmap turns the inner search into O(1) complement lookup.",
        "solution": '''def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}                       # value -> index
    for i, n in enumerate(nums):
        if target - n in seen:
            return [seen[target - n], i]
        seen[n] = i
    return []''',
        "time": "O(N)", "space": "O(N)",
        "edges": ["No valid pair (return [])", "Duplicate values (store latest index)", "Negative numbers work fine"],
        "followups": ["What if the array is sorted? (two pointers, O(1) space)", "Return all pairs?", "3Sum / 4Sum generalization"],
        "related": ["two-sum-ii", "3sum", "two-sum-iv-bst"],
    },
    {
        "slug": "contains-duplicate", "title": "Contains Duplicate", "pattern": "arrays-hashing", "tier": "A",
        "companies": "Amazon, Google, Adobe", "difficulty": "Easy", "leetcode": 217,
        "cue": "Any duplicate exists? → set membership",
        "problem": "Return `True` if any value appears at least twice in `nums`, else `False`.",
        "approaches": [
            ("Sort + scan", "O(N log N)", "O(1)", "adjacent equal"),
            ("Hash set", "O(N)", "O(N)", "seen before?"),
        ],
        "solution": '''def contains_duplicate(nums: list[int]) -> bool:
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False''',
        "time": "O(N)", "space": "O(N)",
        "edges": ["Empty array → False", "All unique → False"],
        "followups": ["Contains Duplicate II (within k indices)", "Contains Duplicate III (value window)"],
        "related": ["contains-duplicate-ii", "longest-consecutive-sequence"],
    },
    {
        "slug": "valid-anagram", "title": "Valid Anagram", "pattern": "arrays-hashing", "tier": "A",
        "companies": "Amazon, Bloomberg, Uber", "difficulty": "Easy", "leetcode": 242,
        "cue": "Same characters, same counts → frequency map",
        "problem": "Given `s` and `t`, return `True` if `t` is an anagram of `s`.",
        "approaches": [
            ("Sort both", "O(N log N)", "O(N)", "compare sorted"),
            ("Counter", "O(N)", "O(1)", "26 letters bounded"),
        ],
        "solution": '''from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    return Counter(s) == Counter(t)''',
        "time": "O(N)", "space": "O(1)",
        "edges": ["Different lengths → False", "Unicode (Counter handles)"],
        "followups": ["Unicode beyond a–z?", "Group anagrams"],
        "related": ["group-anagrams", "find-all-anagrams-in-a-string"],
    },
    {
        "slug": "group-anagrams", "title": "Group Anagrams", "pattern": "arrays-hashing", "tier": "A",
        "companies": "Amazon, Uber, Facebook", "difficulty": "Medium", "leetcode": 49,
        "cue": "Bucket strings by canonical key → hashmap of sorted-key → list",
        "problem": "Group strings that are anagrams of each other.",
        "approaches": [
            ("Sort key", "O(N·K log K)", "O(N·K)", "sorted string as key"),
            ("Count key", "O(N·K)", "O(N·K)", "26-length count tuple as key"),
        ],
        "solution": '''from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))      # or a 26-length count tuple for O(K)
        groups[key].append(s)
    return list(groups.values())''',
        "time": "O(N·K log K)", "space": "O(N·K)",
        "edges": ["Empty strings group together", "Single string"],
        "followups": ["Use count tuple to drop the log K", "Stream of words?"],
        "related": ["valid-anagram"],
    },
    {
        "slug": "longest-consecutive-sequence", "title": "Longest Consecutive Sequence", "pattern": "arrays-hashing", "tier": "A",
        "companies": "Google, Amazon, Meta", "difficulty": "Medium", "leetcode": 128,
        "cue": "Longest run of consecutive ints in O(N) → set + only start at sequence beginnings",
        "problem": "Given an unsorted array, return the length of the longest run of consecutive integers. Must be O(N).",
        "approaches": [
            ("Sort", "O(N log N)", "O(1)", "violates O(N) requirement"),
            ("Set + start check", "O(N)", "O(N)", "extend only from numbers with no left neighbor"),
        ],
        "identify": "O(N) rules out sorting. A set gives O(1) membership; we extend a sequence only from its smallest element so each number is visited once.",
        "solution": '''def longest_consecutive(nums: list[int]) -> int:
    s = set(nums)
    best = 0
    for n in s:
        if n - 1 not in s:               # n is a sequence start
            length = 1
            while n + length in s:
                length += 1
            best = max(best, length)
    return best''',
        "time": "O(N)", "space": "O(N)",
        "edges": ["Empty → 0", "Duplicates collapse in set", "Single element → 1"],
        "followups": ["Return the actual sequence?", "Streaming numbers (Union-Find variant)"],
        "related": ["contains-duplicate"],
    },
    {
        "slug": "valid-sudoku", "title": "Valid Sudoku", "pattern": "arrays-hashing", "tier": "B",
        "companies": "Amazon, Apple, Uber", "difficulty": "Medium", "leetcode": 36,
        "cue": "Check rows/cols/boxes for dupes → 3 sets keyed by index",
        "problem": "Determine if a 9×9 Sudoku board is valid (filled cells only; no need to be solvable).",
        "approaches": [
            ("Three sets", "O(1)", "O(1)", "81 cells fixed; track seen per row/col/box"),
        ],
        "solution": '''from collections import defaultdict

def is_valid_sudoku(board: list[list[str]]) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    boxes = defaultdict(set)
    for r in range(9):
        for c in range(9):
            v = board[r][c]
            if v == ".":
                continue
            b = (r // 3, c // 3)
            if v in rows[r] or v in cols[c] or v in boxes[b]:
                return False
            rows[r].add(v); cols[c].add(v); boxes[b].add(v)
    return True''',
        "time": "O(1)", "space": "O(1)",
        "edges": ["Empty cells '.' skipped", "9x9 fixed size"],
        "followups": ["Solve the Sudoku (backtracking)", "Generalize to N²×N²"],
        "related": ["sudoku-solver"],
    },
    {
        "slug": "encode-decode-strings", "title": "Encode and Decode Strings", "pattern": "arrays-hashing", "tier": "B",
        "companies": "Google, Meta, Amazon", "difficulty": "Medium", "leetcode": 271,
        "cue": "Serialize a list of arbitrary strings → length-prefix framing",
        "problem": "Design `encode(list[str]) -> str` and `decode(str) -> list[str]` that round-trip any strings (including delimiters).",
        "approaches": [
            ("Length-prefix", "O(N)", "O(N)", "len + '#' + s avoids delimiter collisions"),
        ],
        "solution": '''def encode(strs: list[str]) -> str:
    return "".join(f"{len(s)}#{s}" for s in strs)

def decode(s: str) -> list[str]:
    res, i = [], 0
    while i < len(s):
        j = s.index("#", i)
        length = int(s[i:j])
        res.append(s[j + 1: j + 1 + length])
        i = j + 1 + length
    return res''',
        "time": "O(N)", "space": "O(N)",
        "edges": ["Empty list", "Strings containing '#' or digits (length-prefix is safe)"],
        "followups": ["Unicode lengths (use byte length)", "Streaming decode"],
        "related": ["serialize-deserialize-binary-tree"],
    },
    {
        "slug": "majority-element", "title": "Majority Element", "pattern": "arrays-hashing", "tier": "B",
        "companies": "Amazon, Google, Adobe", "difficulty": "Easy", "leetcode": 169,
        "cue": "Element appearing > N/2 times → Boyer-Moore voting (O(1) space)",
        "problem": "Return the element appearing more than ⌊N/2⌋ times (guaranteed to exist).",
        "approaches": [
            ("Counter", "O(N)", "O(N)", "most_common"),
            ("Boyer-Moore voting", "O(N)", "O(1)", "candidate + count"),
        ],
        "solution": '''def majority_element(nums: list[int]) -> int:
    count = 0
    candidate = None
    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if n == candidate else -1
    return candidate''',
        "time": "O(N)", "space": "O(1)",
        "edges": ["Single element", "Majority guaranteed by problem"],
        "followups": ["Majority Element II (> N/3, up to 2 answers)"],
        "related": ["majority-element-ii"],
    },
    {
        "slug": "first-unique-character", "title": "First Unique Character in a String", "pattern": "arrays-hashing", "tier": "C",
        "companies": "Amazon, Bloomberg, Goldman Sachs", "difficulty": "Easy", "leetcode": 387,
        "cue": "First non-repeating → frequency map then scan order",
        "problem": "Return the index of the first non-repeating character in `s`, or -1.",
        "approaches": [("Counter + scan", "O(N)", "O(1)", "two passes")],
        "solution": '''from collections import Counter

def first_uniq_char(s: str) -> int:
    freq = Counter(s)
    for i, ch in enumerate(s):
        if freq[ch] == 1:
            return i
    return -1''',
        "time": "O(N)", "space": "O(1)",
        "edges": ["All repeating → -1", "Empty → -1"],
        "followups": ["Stream of characters (queue of candidates)"],
        "related": ["valid-anagram"],
    },
]

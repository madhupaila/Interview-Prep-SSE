# -*- coding: utf-8 -*-
"""String questions (algorithmic)."""

QUESTIONS = [
    {
        "slug": "reverse-string", "title": "Reverse String", "pattern": "strings", "tier": "A",
        "companies": "Amazon, Microsoft", "difficulty": "Easy", "leetcode": 344,
        "cue": "Reverse in place → two pointers swap",
        "problem": "Reverse a list of characters in place.",
        "solution": '''def reverse_string(s: list[str]) -> None:
    i, j = 0, len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1; j -= 1''',
        "time": "O(N)", "space": "O(1)",
        "related": ["reverse-words-in-a-string"],
    },
    {
        "slug": "valid-anagram-str", "title": "Valid Anagram", "pattern": "strings", "tier": "A",
        "companies": "Amazon, Bloomberg", "difficulty": "Easy", "leetcode": 242,
        "cue": "Same multiset of chars → Counter compare",
        "problem": "Return True if `t` is an anagram of `s`.",
        "solution": '''from collections import Counter

def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)''',
        "time": "O(N)", "space": "O(1)",
        "related": ["group-anagrams"],
    },
    {
        "slug": "longest-common-prefix", "title": "Longest Common Prefix", "pattern": "strings", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 14,
        "cue": "Common prefix of strings → shrink prefix against each word",
        "problem": "Return the longest common prefix among an array of strings.",
        "solution": '''def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix''',
        "time": "O(S)", "space": "O(1)",
        "related": ["implement-trie"],
    },
    {
        "slug": "valid-palindrome-str", "title": "Valid Palindrome", "pattern": "strings", "tier": "A",
        "companies": "Meta, Amazon", "difficulty": "Easy", "leetcode": 125,
        "cue": "Alphanumeric palindrome → two pointers skipping non-alnum",
        "problem": "Return True if the string is a palindrome considering alphanumeric chars only.",
        "solution": '''def is_palindrome(s: str) -> bool:
    filtered = [c.lower() for c in s if c.isalnum()]
    return filtered == filtered[::-1]''',
        "time": "O(N)", "space": "O(N)",
        "related": ["valid-palindrome"],
    },
    {
        "slug": "string-to-integer-atoi", "title": "String to Integer (atoi)", "pattern": "strings", "tier": "B",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 8,
        "cue": "Parse int with rules → strip, sign, digits, clamp",
        "problem": "Implement atoi: parse leading optional sign and digits, clamp to 32-bit range.",
        "solution": '''def my_atoi(s: str) -> int:
    s = s.lstrip()
    if not s:
        return 0
    sign = 1
    i = 0
    if s[0] in "+-":
        sign = -1 if s[0] == '-' else 1
        i = 1
    num = 0
    while i < len(s) and s[i].isdigit():
        num = num * 10 + int(s[i])
        i += 1
    num *= sign
    return max(-2**31, min(2**31 - 1, num))''',
        "time": "O(N)", "space": "O(1)",
        "edges": ["Leading spaces", "No digits → 0", "Overflow clamps"],
        "related": ["reverse-integer"],
    },
    {
        "slug": "reverse-words-in-a-string", "title": "Reverse Words in a String", "pattern": "strings", "tier": "B",
        "companies": "Amazon, Microsoft, Bloomberg", "difficulty": "Medium", "leetcode": 151,
        "cue": "Reverse word order, trim spaces → split + reverse + join",
        "problem": "Reverse the order of words, collapsing multiple spaces.",
        "solution": '''def reverse_words(s: str) -> str:
    return " ".join(reversed(s.split()))''',
        "time": "O(N)", "space": "O(N)",
        "related": ["reverse-string"],
    },
    {
        "slug": "group-anagrams-str", "title": "Group Anagrams", "pattern": "strings", "tier": "B",
        "companies": "Amazon, Uber, Meta", "difficulty": "Medium", "leetcode": 49,
        "cue": "Bucket by sorted signature → hashmap",
        "problem": "Group anagrams together.",
        "solution": '''from collections import defaultdict

def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for s in strs:
        key = [0] * 26
        for ch in s:
            key[ord(ch) - ord('a')] += 1
        groups[tuple(key)].append(s)
    return list(groups.values())''',
        "time": "O(N·K)", "space": "O(N·K)",
        "related": ["valid-anagram-str"],
    },
    {
        "slug": "longest-palindromic-substring-str", "title": "Longest Palindromic Substring", "pattern": "strings", "tier": "B",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 5,
        "cue": "Longest palindrome → expand around centers",
        "problem": "Return the longest palindromic substring.",
        "solution": '''def longest_palindrome(s: str) -> str:
    res = ""
    for i in range(len(s)):
        for l, r in ((i, i), (i, i + 1)):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(res):
                    res = s[l:r + 1]
                l -= 1; r += 1
    return res''',
        "time": "O(N^2)", "space": "O(1)",
        "related": ["longest-palindromic-substring", "palindromic-substrings"],
    },
    {
        "slug": "implement-strstr-kmp", "title": "Find the Index of First Occurrence (KMP)", "pattern": "strings", "tier": "C",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 28,
        "cue": "Substring search in O(N+M) → KMP failure function",
        "problem": "Return the index of the first occurrence of `needle` in `haystack`, or -1.",
        "solution": '''def str_str(haystack: str, needle: str) -> int:
    if not needle:
        return 0
    lps = [0] * len(needle)
    k = 0
    for i in range(1, len(needle)):
        while k and needle[i] != needle[k]:
            k = lps[k - 1]
        if needle[i] == needle[k]:
            k += 1
        lps[i] = k
    k = 0
    for i, ch in enumerate(haystack):
        while k and ch != needle[k]:
            k = lps[k - 1]
        if ch == needle[k]:
            k += 1
        if k == len(needle):
            return i - k + 1
    return -1''',
        "time": "O(N+M)", "space": "O(M)",
        "identify": "Avoid re-scanning by precomputing the longest proper prefix-suffix (LPS) so mismatches jump instead of restart.",
        "related": ["repeated-substring-pattern"],
    },
    {
        "slug": "palindromic-substrings", "title": "Palindromic Substrings", "pattern": "strings", "tier": "C",
        "companies": "Amazon, Meta", "difficulty": "Medium", "leetcode": 647,
        "cue": "Count palindromic substrings → expand around each center",
        "problem": "Count the number of palindromic substrings in `s`.",
        "solution": '''def count_substrings(s: str) -> int:
    count = 0
    for i in range(len(s)):
        for l, r in ((i, i), (i, i + 1)):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1; r += 1
    return count''',
        "time": "O(N^2)", "space": "O(1)",
        "related": ["longest-palindromic-substring-str"],
    },
]

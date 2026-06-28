# -*- coding: utf-8 -*-
"""Interview Math questions."""

QUESTIONS = [
    {
        "slug": "fizzbuzz", "title": "Fizz Buzz", "pattern": "math", "tier": "A",
        "companies": "Amazon, Microsoft", "difficulty": "Easy", "leetcode": 412,
        "cue": "Divisibility printing → mod checks",
        "problem": "Return the Fizz Buzz sequence from 1 to n.",
        "solution": '''def fizz_buzz(n: int) -> list[str]:
    res = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            res.append("FizzBuzz")
        elif i % 3 == 0:
            res.append("Fizz")
        elif i % 5 == 0:
            res.append("Buzz")
        else:
            res.append(str(i))
    return res''',
        "time": "O(N)", "space": "O(N)",
        "related": ["happy-number"],
    },
    {
        "slug": "pow-x-n", "title": "Pow(x, n)", "pattern": "math", "tier": "A",
        "companies": "Amazon, Meta, Google, LinkedIn", "difficulty": "Medium", "leetcode": 50,
        "cue": "Fast exponentiation → square and halve the exponent",
        "problem": "Implement `x` raised to the power `n` in O(log n).",
        "solution": '''def my_pow(x: float, n: int) -> float:
    if n < 0:
        x, n = 1 / x, -n
    result = 1.0
    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result''',
        "time": "O(log N)", "space": "O(1)",
        "related": ["sqrt-x"],
    },
    {
        "slug": "sqrt-x", "title": "Sqrt(x)", "pattern": "math", "tier": "A",
        "companies": "Amazon, Google, Bloomberg", "difficulty": "Easy", "leetcode": 69,
        "cue": "Integer sqrt → binary search on candidate",
        "problem": "Return the integer square root of `x` (floor).",
        "solution": '''def my_sqrt(x: int) -> int:
    lo, hi = 0, x
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi''',
        "time": "O(log X)", "space": "O(1)",
        "related": ["pow-x-n"],
    },
    {
        "slug": "plus-one", "title": "Plus One", "pattern": "math", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 66,
        "cue": "Increment digit array → carry from the end",
        "problem": "Increment a number represented as a digit array by one.",
        "solution": '''def plus_one(digits: list[int]) -> list[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    return [1] + digits''',
        "time": "O(N)", "space": "O(1)",
        "related": ["add-binary"],
    },
    {
        "slug": "happy-number-math", "title": "Happy Number", "pattern": "math", "tier": "B",
        "companies": "Amazon, Google, Uber", "difficulty": "Easy", "leetcode": 202,
        "cue": "Detect cycle of digit-square-sums → set or Floyd",
        "problem": "Determine if a number is happy (digit-square-sum reaches 1).",
        "solution": '''def is_happy(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1''',
        "time": "O(log N) per step", "space": "O(log N)",
        "related": ["happy-number"],
    },
    {
        "slug": "count-primes", "title": "Count Primes", "pattern": "math", "tier": "B",
        "companies": "Amazon, Google, Microsoft", "difficulty": "Medium", "leetcode": 204,
        "cue": "Count primes below n → Sieve of Eratosthenes",
        "problem": "Count the number of primes strictly less than `n`.",
        "solution": '''def count_primes(n: int) -> int:
    if n < 3:
        return 0
    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return sum(is_prime)''',
        "time": "O(N log log N)", "space": "O(N)",
        "related": ["pow-x-n"],
    },
    {
        "slug": "add-binary", "title": "Add Binary", "pattern": "math", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Easy", "leetcode": 67,
        "cue": "Add binary strings → carry from the end",
        "problem": "Add two binary strings and return the sum as a binary string.",
        "solution": '''def add_binary(a: str, b: str) -> str:
    i, j = len(a) - 1, len(b) - 1
    carry = 0
    res = []
    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(a[i]); i -= 1
        if j >= 0:
            total += int(b[j]); j -= 1
        carry, digit = divmod(total, 2)
        res.append(str(digit))
    return "".join(reversed(res))''',
        "time": "O(max(M,N))", "space": "O(max(M,N))",
        "related": ["plus-one", "add-two-numbers"],
    },
    {
        "slug": "excel-column-number", "title": "Excel Sheet Column Number", "pattern": "math", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 171,
        "cue": "Base-26 letters to number → Horner's accumulation",
        "problem": "Convert an Excel column title (e.g., 'AB') to its column number.",
        "solution": '''def title_to_number(column_title: str) -> int:
    result = 0
    for ch in column_title:
        result = result * 26 + (ord(ch) - ord('A') + 1)
    return result''',
        "time": "O(N)", "space": "O(1)",
        "related": ["excel-column-title"],
    },
    {
        "slug": "max-points-on-a-line", "title": "Max Points on a Line", "pattern": "math", "tier": "C",
        "companies": "Amazon, Google, LinkedIn", "difficulty": "Hard", "leetcode": 149,
        "cue": "Most collinear points → group by slope per anchor point",
        "problem": "Return the maximum number of points that lie on the same straight line.",
        "solution": '''from collections import defaultdict
from math import gcd

def max_points(points: list[list[int]]) -> int:
    n = len(points)
    if n <= 2:
        return n
    best = 0
    for i in range(n):
        slopes = defaultdict(int)
        for j in range(n):
            if i == j:
                continue
            dx = points[j][0] - points[i][0]
            dy = points[j][1] - points[i][1]
            g = gcd(dx, dy) or 1
            slope = (dx // g, dy // g)
            slopes[slope] += 1
        best = max(best, max(slopes.values()) + 1)
    return best''',
        "time": "O(N^2)", "space": "O(N)",
        "identify": "Fix each point as an anchor and bucket the others by reduced slope; the largest bucket + the anchor is the answer.",
        "related": ["pow-x-n"],
    },
    {
        "slug": "basic-calculator-ii", "title": "Basic Calculator II", "pattern": "math", "tier": "C",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 227,
        "cue": "Evaluate +-*/ expression → stack, apply */ immediately",
        "problem": "Evaluate a string expression with `+ - * /` and non-negative integers (integer division truncates toward zero).",
        "solution": '''def calculate(s: str) -> int:
    stack = []
    num = 0
    op = '+'
    for i, ch in enumerate(s):
        if ch.isdigit():
            num = num * 10 + int(ch)
        if ch in "+-*/" or i == len(s) - 1:
            if op == '+':
                stack.append(num)
            elif op == '-':
                stack.append(-num)
            elif op == '*':
                stack.append(stack.pop() * num)
            else:
                stack.append(int(stack.pop() / num))
            op = ch
            num = 0
    return sum(stack)''',
        "time": "O(N)", "space": "O(N)",
        "related": ["basic-calculator"],
    },
]

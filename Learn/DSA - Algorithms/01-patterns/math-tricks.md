# Pattern: Interview Math

## Recognition Cues

- GCD/LCM, primes, factorials, modular arithmetic
- "Pow(x, n)", "sqrt", "count primes", "happy number"
- Overflow-avoidance, digit manipulation
- (Heavy number theory is out of scope — these are interview-level only)

## Core Idea

A toolbox of small math algorithms that show up as sub-steps. Know them cold so they don't derail a larger problem.

---

## Toolbox

```python
import math

math.gcd(a, b)                      # built-in GCD
def lcm(a, b): return a * b // math.gcd(a, b)

# Fast power (binary exponentiation), O(log n)
def fast_pow(x: float, n: int) -> float:
    if n < 0:
        x, n = 1 / x, -n
    result = 1
    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result

# Sieve of Eratosthenes — primes up to n, O(n log log n)
def sieve(n: int) -> list[int]:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, p in enumerate(is_prime) if p]

# Integer sqrt via binary search
def my_sqrt(x: int) -> int:
    lo, hi = 0, x
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:
            lo = mid + 1
        else:
            hi = mid - 1
    return hi

MOD = 10**9 + 7                      # common modulus for "answer mod 1e9+7"
```

### Digit manipulation

```python
def reverse_int(x):
    sign = -1 if x < 0 else 1
    x = abs(x)
    rev = 0
    while x:
        rev = rev * 10 + x % 10
        x //= 10
    return sign * rev
```

---

## When to Use / When NOT

| Use when | Avoid when |
|----------|------------|
| Sub-step needs gcd/pow/primes | Pure data-structure problem |
| "answer mod 1e9+7" appears | — |

## Complexity

- Fast power **O(log n)**; sieve **O(n log log n)**; gcd **O(log min(a,b))**.

## Variants & Pitfalls

- **Pow(x,n)**, **Sqrt(x)**, **Count Primes**, **Happy Number**, **Excel Column**, **Reverse Integer**, **Add Strings/Binary**.
- Pitfall: handle negative exponents/overflow; in Python ints don't overflow but problems may still require mod.

## Linked Questions

- Tier A: Pow(x,n), Sqrt(x), Happy Number, Reverse Integer, FizzBuzz
- Tier B: Count Primes, Excel Sheet Column Number, Add Binary, Plus One
- Tier C: Max Points on a Line, Fraction to Recurring Decimal, Basic Calculator

## Related

- [Bit Manipulation](bit-manipulation.md) · [Binary Search](binary-search.md)

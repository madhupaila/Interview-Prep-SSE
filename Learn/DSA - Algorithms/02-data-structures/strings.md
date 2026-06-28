# Strings

Immutable sequences of characters. Most string problems reduce to array/hashing/two-pointer/DP patterns plus a couple of specialized algorithms.

---

## Python String Essentials

```python
s = "hello"
s[::-1]                  # reverse
s.lower(), s.upper()
s.split(","), " ".join(parts)
s.strip(), s.replace("a", "b")
s.startswith("he"), s.endswith("lo")
ord('a'), chr(97)        # 97, 'a'
"".join(sorted(s))       # sorted chars
s.isalnum(), s.isdigit(), s.isalpha()
idx = ord(ch) - ord('a') # map a..z -> 0..25
```

> Strings are **immutable** — build with a list then `"".join(...)`; repeated `+=` is O(N^2).

---

## Common Techniques

| Task | Approach |
|------|----------|
| Anagram check | `Counter(a) == Counter(b)` |
| Palindrome check | two pointers from ends |
| Char frequency | `Counter` / array[26] |
| Substring search | sliding window / KMP |
| Encode/decode | length-prefix or delimiter |

```python
def is_palindrome(s):
    s = [c.lower() for c in s if c.isalnum()]
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1; j -= 1
    return True
```

---

## KMP — substring search in O(N+M)

```python
def kmp_search(text, pat):
    if not pat:
        return 0
    lps = [0] * len(pat)             # longest proper prefix that is suffix
    k = 0
    for i in range(1, len(pat)):
        while k and pat[i] != pat[k]:
            k = lps[k - 1]
        if pat[i] == pat[k]:
            k += 1
        lps[i] = k
    k = 0
    for i, ch in enumerate(text):
        while k and ch != pat[k]:
            k = lps[k - 1]
        if ch == pat[k]:
            k += 1
        if k == len(pat):
            return i - k + 1          # match start index
    return -1
```

## Rabin-Karp — rolling hash (good for multiple/streaming search)

Hash a window and slide; recompute in O(1) per shift. Useful for "repeated substring" problems.

---

## Complexity

| Operation | Cost |
|-----------|------|
| Concatenate (`+`) | O(N) (avoid in loops) |
| Slice | O(k) |
| `in` substring | O(N·M) naive, O(N+M) with KMP |
| sort chars | O(N log N) |

---

## Pitfalls

- Building strings with `+=` in a loop is O(N^2) — use a list.
- Unicode vs ASCII: `ord`/`chr` work on code points.
- Off-by-one in window/two-pointer boundaries.

---

## Related Patterns

- [Sliding Window](../01-patterns/sliding-window.md), [Two Pointers](../01-patterns/two-pointers.md), [Dynamic Programming](../01-patterns/dynamic-programming.md), [Trie](../01-patterns/trie.md)

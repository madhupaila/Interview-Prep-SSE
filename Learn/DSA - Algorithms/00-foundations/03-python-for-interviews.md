# Python for Interviews — Idioms & Standard Library

Python is the fastest language to write in interviews **if** you know the standard library. Here is everything you actually use.

---

## collections

```python
from collections import defaultdict, Counter, deque, OrderedDict

# defaultdict — no KeyError, auto-init
graph = defaultdict(list)
graph[u].append(v)

freq = defaultdict(int)
freq[x] += 1

# Counter — frequency map with helpers
c = Counter("aabbbc")          # {'b':3,'a':2,'c':1}
c.most_common(2)               # [('b',3),('a',2)]
c1 - c2                        # multiset difference (keeps positives)

# deque — O(1) append/pop both ends (use as queue or stack)
q = deque()
q.append(x); q.popleft()       # queue (BFS)
q.appendleft(x); q.pop()       # double-ended
```

---

## heapq (min-heap)

```python
import heapq

h = []
heapq.heappush(h, 3)
heapq.heappush(h, 1)
smallest = heapq.heappop(h)    # 1

# Max-heap: negate values
heapq.heappush(h, -val)
largest = -heapq.heappop(h)

# Heapify a list in O(N)
nums = [5, 1, 3]
heapq.heapify(nums)

# K largest / smallest directly
heapq.nlargest(k, nums)
heapq.nsmallest(k, nums)

# Tuples sort by first element (then second) — great for (dist, node)
heapq.heappush(h, (dist, node))
```

---

## bisect (binary search on sorted list)

```python
import bisect

arr = [1, 3, 3, 5, 7]
bisect.bisect_left(arr, 3)     # 1 (first index where 3 could go)
bisect.bisect_right(arr, 3)    # 3 (after existing 3s)
bisect.insort(arr, 4)          # insert keeping sorted

# Count elements in [lo, hi]:
bisect.bisect_right(arr, hi) - bisect.bisect_left(arr, lo)
```

---

## Strings

```python
s = "hello world"
s.split()                      # ['hello', 'world']
"".join(['a','b','c'])         # 'abc'
s[::-1]                        # reverse
sorted(s)                      # list of chars sorted
ord('a'), chr(97)              # 97, 'a'
s.isalnum(), s.isdigit()
# char to 0..25 index:
idx = ord(ch) - ord('a')
```

> Strings are **immutable** — build with a list then `"".join(...)` to avoid O(N^2) concatenation.

---

## Useful built-ins

```python
enumerate(arr)                 # (index, value) pairs
zip(a, b)                      # pair up iterables
any(x > 0 for x in arr)
all(x > 0 for x in arr)
sum(arr), min(arr), max(arr)
sorted(arr, key=lambda x: (x[1], -x[0]))   # multi-key sort
float('inf'), float('-inf')    # sentinels
divmod(17, 5)                  # (3, 2)
```

---

## Matrix / grid idioms

```python
rows, cols = len(grid), len(grid[0])
# 4-directional neighbors
for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols:
        ...

# 2D array init (avoid aliasing bug!)
dp = [[0] * cols for _ in range(rows)]   # CORRECT
# dp = [[0]*cols]*rows                    # WRONG — shared rows
```

---

## Recursion limit

```python
import sys
sys.setrecursionlimit(10**6)   # deep DFS on large inputs
```

---

## Functions you reach for per pattern

| Pattern | Tools |
|---------|-------|
| Two pointers | plain indices |
| Sliding window | `defaultdict`, `Counter` |
| Top-K / Dijkstra | `heapq` |
| BFS | `deque` |
| Binary search | `bisect` or manual |
| Graph adjacency | `defaultdict(list)` |
| Frequency | `Counter` |
| DP memo | `@cache` / `functools.lru_cache` |
| Trie | nested `dict` or class |

```python
from functools import cache    # Python 3.9+

@cache
def dp(i, j):
    ...
```

---

## Gotchas

- `[[0]*c]*r` creates **shared** inner lists. Use a comprehension.
- Default args: never use mutable defaults (`def f(x=[])`).
- Integer division is `//`; `/` returns float.
- `dict` preserves insertion order (3.7+).
- Comparing tuples compares element-wise (handy for heaps).

---

## Related

- [Complexity / Big-O](02-complexity-big-o.md)
- [Data Structures](../02-data-structures/)

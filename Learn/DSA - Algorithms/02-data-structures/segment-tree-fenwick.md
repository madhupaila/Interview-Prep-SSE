# Segment Tree & Fenwick (BIT)

For **range queries with updates** (sum/min/max over a range while elements change). Interview-relevant for "range sum query — mutable", "count of smaller numbers after self", etc. (Pure-CP variants like lazy propagation are out of scope.)

---

## When You Need These

| Scenario | Structure |
|----------|-----------|
| Static array, range sum | Prefix Sum (no tree needed) |
| Mutable array, range sum, point update | **Fenwick / Segment Tree** |
| Range min/max with updates | **Segment Tree** |
| Count inversions / smaller-after-self | **Fenwick** on ranks |

---

## Fenwick Tree (Binary Indexed Tree) — range sum, point update

```python
class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)      # 1-indexed

    def update(self, i, delta):        # add delta at index i (0-based)
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & (-i)              # next index covering i

    def prefix_sum(self, i):           # sum of [0..i]
        i += 1
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & (-i)
        return s

    def range_sum(self, l, r):
        return self.prefix_sum(r) - (self.prefix_sum(l - 1) if l else 0)
```

| Operation | Cost |
|-----------|------|
| update | O(log N) |
| prefix/range sum | O(log N) |
| build | O(N log N) (or O(N)) |

---

## Segment Tree — range query + point update (sum example)

```python
class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        i >>= 1
        while i:
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]
            i >>= 1

    def query(self, l, r):             # sum of [l, r)
        res = 0
        l += self.n; r += self.n
        while l < r:
            if l & 1:
                res += self.tree[l]; l += 1
            if r & 1:
                r -= 1; res += self.tree[r]
            l >>= 1; r >>= 1
        return res
```

| Operation | Cost |
|-----------|------|
| update / query | O(log N) |
| build | O(N) |
| space | O(N) |

Swap `+` for `min`/`max` to support range-min/max queries.

---

## Pitfalls

- If there are **no updates**, prefer Prefix Sum (simpler, O(1) query).
- Fenwick is easier to code than a segment tree for pure sums.
- Off-by-one: Fenwick is 1-indexed internally.

---

## Related Patterns

- [Prefix Sum](../01-patterns/prefix-sum.md), [Binary Search](../01-patterns/binary-search.md)

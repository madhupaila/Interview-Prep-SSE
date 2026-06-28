# How to Approach Any Problem — The UMPIRE Framework

The single most important skill in DSA rounds is **a repeatable approach**. Don't jump to code. Run **UMPIRE** every time — it doubles as your spoken structure so the interviewer can follow your thinking.

---

## UMPIRE

| Step | Letter | What you do | Time (45-min round) |
|------|--------|-------------|---------------------|
| 1 | **U** — Understand | Restate problem, ask clarifying questions, note constraints | 2–4 min |
| 2 | **M** — Match | Match to a known **pattern** using cues | 1–2 min |
| 3 | **P** — Plan | Outline approach in plain words / pseudocode | 3–5 min |
| 4 | **I** — Implement | Write clean Python, narrate invariants | 10–15 min |
| 5 | **R** — Review | Dry-run a small example, check edge cases | 3–5 min |
| 6 | **E** — Evaluate | State time/space complexity, discuss tradeoffs/follow-ups | 2–3 min |

---

## Step 1 — Understand (ask before you code)

| Question | Why it matters |
|----------|----------------|
| Input size / range of N? | Drives target complexity (see table below) |
| Sorted? Duplicates allowed? | Unlocks two-pointers / binary search |
| Negative numbers? Empty input? | Edge cases |
| Return value vs in-place? | Space constraint |
| One answer or all answers? | Greedy/DP vs backtracking |
| Can I modify the input? | Cyclic sort, in-place tricks |

**Senior move:** restate it back: *"So I'm given an unsorted array of up to 10^5 integers, possibly negative, and I need the length of the longest subarray summing to K. Duplicates allowed, return 0 if none. Correct?"*

---

## Step 2 — Match (constraints → target complexity)

The input size tells you the **target complexity**, which narrows the pattern.

| N (input size) | Target complexity | Likely approach |
|----------------|-------------------|-----------------|
| ≤ 10–12 | O(N!) / O(2^N) | Backtracking, permutations |
| ≤ 20–25 | O(2^N) | Subsets, bitmask DP |
| ≤ 100–500 | O(N^3) | DP (interval), Floyd-Warshall |
| ≤ 1,000–5,000 | O(N^2) | DP (2D), nested loops |
| ≤ 10^5–10^6 | O(N log N) / O(N) | Sort, heap, sliding window, two pointers, hashing |
| ≤ 10^8 | O(N) / O(log N) | Single pass, binary search |

Then apply the [Cue Dictionary](../01-patterns/02-cue-dictionary.md) and [Decision Tree](../01-patterns/01-pattern-recognition-decision-tree.md).

---

## Step 3 — Plan (pseudocode out loud)

> "I'll use a hashmap of prefix-sum → earliest index. As I iterate, if `prefix - K` was seen, I update the max length. One pass, O(N)."

Get buy-in **before** coding. If the interviewer nods, implement. If not, you saved 15 minutes.

---

## Step 4 — Implement (clean Python)

- Name variables meaningfully (`left`, `right`, `window_sum`).
- Handle the empty/edge case first.
- Narrate invariants: *"`left` is the start of the current valid window."*
- Prefer standard library: `collections`, `heapq`, `bisect` (see [Python for Interviews](03-python-for-interviews.md)).

---

## Step 5 — Review (dry-run)

Pick a tiny example (3–5 elements) and trace your code line by line. This catches off-by-one and boundary bugs **before** the interviewer points them out.

Always check: empty input, single element, all duplicates, negative numbers, target not found.

---

## Step 6 — Evaluate

> "Time is O(N) — one pass. Space is O(N) for the hashmap. If the array were sorted I could do O(1) space with two pointers. A follow-up: handle streaming input where I can't store all prefixes."

---

## Worked Example: Subarray Sum Equals K

**U:** Array of ints (can be negative), find count of subarrays summing to K. N ≤ 2·10^4.

**M:** "Subarray + sum + count" → **Prefix Sum + Hashmap** (negatives rule out sliding window).

**P:** Track running prefix sum; hashmap counts how many times each prefix seen; for each index add `count[prefix - K]`.

**I:**

```python
from collections import defaultdict

def subarray_sum(nums: list[int], k: int) -> int:
    count = 0
    prefix = 0
    seen = defaultdict(int)
    seen[0] = 1  # empty prefix
    for n in nums:
        prefix += n
        count += seen[prefix - k]
        seen[prefix] += 1
    return count
```

**R:** `nums=[1,1,1], k=2` → prefixes 1,2,3; matches found at index 1 and 2 → count 2. Correct.

**E:** O(N) time, O(N) space. Sliding window fails here because negatives break monotonicity.

---

## Related

- [Complexity / Big-O](02-complexity-big-o.md)
- [Python for Interviews](03-python-for-interviews.md)
- [Interview Round Flow](04-interview-round-flow.md)
- [Pattern Recognition Decision Tree](../01-patterns/01-pattern-recognition-decision-tree.md)

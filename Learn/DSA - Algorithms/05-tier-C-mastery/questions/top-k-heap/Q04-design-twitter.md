# Design Twitter  ·  LeetCode #355

**Pattern:** Top-K Heap
**Tier:** C  ·  **Difficulty:** Medium
**Companies:** Amazon, Meta, Twitter

---

## Memory Hook (Recognition Cue)

> **Merge recent tweets of followees → heap merge of timelines**

---

## Problem

Design Twitter: post tweets, follow/unfollow, and fetch 10 most recent feed tweets.

---

## Clarifying Questions

- Input size / value ranges?
- Sorted? duplicates? negatives? empty?
- Return value vs in-place?

---

## Approaches

_See solution below._

---

## Pattern Identification

Cue maps to **Top-K Heap** — see [pattern sheet](../../../01-patterns/top-k-heap.md).

---

## Solution (Python)

```python
from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)           # user -> [(time, tweetId)]
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        users = self.following[userId] | {userId}
        for u in users:
            for t in self.tweets[u][-10:]:
                heap.append(t)
        return [tid for _, tid in heapq.nlargest(10, heap)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
```

**Complexity:** Time O(N log N) feed, Space O(N).

---

## Edge Cases & Pitfalls

- Empty input
- Single element
- All duplicates / negatives

---

## Follow-Ups

1. Can you reduce space?
2. How does this scale / handle streaming input?

---

## Related

- Pattern sheet: [Top-K Heap](../../../01-patterns/top-k-heap.md)
- Related questions: `merge-k-sorted-lists`
- [Pattern Master Index](../../../01-patterns/00-pattern-master-index.md) · [Decision Tree](../../../01-patterns/01-pattern-recognition-decision-tree.md)

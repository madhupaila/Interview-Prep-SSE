# -*- coding: utf-8 -*-
"""Merge Intervals questions."""

QUESTIONS = [
    {
        "slug": "merge-intervals", "title": "Merge Intervals", "pattern": "merge-intervals", "tier": "A",
        "companies": "Amazon, Meta, Google, Microsoft", "difficulty": "Medium", "leetcode": 56,
        "cue": "Combine overlapping ranges → sort by start, sweep",
        "problem": "Merge all overlapping intervals.",
        "solution": '''def merge(intervals: list[list[int]]) -> list[list[int]]:
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged''',
        "time": "O(N log N)", "space": "O(N)",
        "edges": ["Single interval", "Touching intervals [1,2],[2,3] merge", "Already sorted"],
        "related": ["insert-interval", "non-overlapping-intervals"],
    },
    {
        "slug": "insert-interval", "title": "Insert Interval", "pattern": "merge-intervals", "tier": "A",
        "companies": "Amazon, Google, LinkedIn", "difficulty": "Medium", "leetcode": 57,
        "cue": "Insert into sorted non-overlapping → three phases (before/overlap/after)",
        "problem": "Insert a new interval into a sorted, non-overlapping list and merge if needed.",
        "solution": '''def insert(intervals: list[list[int]], new: list[int]) -> list[list[int]]:
    res = []
    i, n = 0, len(intervals)
    while i < n and intervals[i][1] < new[0]:    # before
        res.append(intervals[i]); i += 1
    while i < n and intervals[i][0] <= new[1]:   # overlap → merge
        new[0] = min(new[0], intervals[i][0])
        new[1] = max(new[1], intervals[i][1])
        i += 1
    res.append(new)
    while i < n:                                 # after
        res.append(intervals[i]); i += 1
    return res''',
        "time": "O(N)", "space": "O(N)",
        "related": ["merge-intervals"],
    },
    {
        "slug": "meeting-rooms", "title": "Meeting Rooms", "pattern": "merge-intervals", "tier": "A",
        "companies": "Amazon, Meta, Google", "difficulty": "Easy", "leetcode": 252,
        "cue": "Can attend all meetings? → sort, check adjacent overlap",
        "problem": "Return True if a person can attend all meetings (no overlaps).",
        "solution": '''def can_attend_meetings(intervals: list[list[int]]) -> bool:
    intervals.sort(key=lambda x: x[0])
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    return True''',
        "time": "O(N log N)", "space": "O(1)",
        "related": ["meeting-rooms-ii"],
    },
    {
        "slug": "meeting-rooms-ii", "title": "Meeting Rooms II", "pattern": "merge-intervals", "tier": "B",
        "companies": "Amazon, Meta, Google, Uber", "difficulty": "Medium", "leetcode": 253,
        "cue": "Min rooms for overlapping meetings → min-heap of end times",
        "problem": "Return the minimum number of conference rooms required.",
        "approaches": [("Heap", "O(N log N)", "O(N)", "reuse room when freed"), ("Sweep line", "O(N log N)", "O(N)", "starts/ends events")],
        "identify": "Sort by start; a min-heap of end times lets us reuse a room whenever the earliest meeting has ended.",
        "solution": '''import heapq

def min_meeting_rooms(intervals: list[list[int]]) -> int:
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    ends = []
    for start, end in intervals:
        if ends and ends[0] <= start:
            heapq.heappop(ends)                  # reuse a freed room
        heapq.heappush(ends, end)
    return len(ends)''',
        "time": "O(N log N)", "space": "O(N)",
        "related": ["meeting-rooms", "employee-free-time"],
    },
    {
        "slug": "non-overlapping-intervals", "title": "Non-overlapping Intervals", "pattern": "merge-intervals", "tier": "B",
        "companies": "Amazon, Google, Bloomberg", "difficulty": "Medium", "leetcode": 435,
        "cue": "Min removals to remove overlaps → greedy by earliest end",
        "problem": "Return the minimum number of intervals to remove so the rest don't overlap.",
        "solution": '''def erase_overlap_intervals(intervals: list[list[int]]) -> int:
    intervals.sort(key=lambda x: x[1])           # earliest end first
    end = float('-inf')
    keep = 0
    for s, e in intervals:
        if s >= end:
            keep += 1
            end = e
    return len(intervals) - keep''',
        "time": "O(N log N)", "space": "O(1)",
        "related": ["merge-intervals", "minimum-arrows-balloons"],
    },
    {
        "slug": "interval-list-intersections", "title": "Interval List Intersections", "pattern": "merge-intervals", "tier": "B",
        "companies": "Amazon, Meta, Google", "difficulty": "Medium", "leetcode": 986,
        "cue": "Intersect two sorted interval lists → two pointers",
        "problem": "Return the intersection of two lists of sorted, disjoint intervals.",
        "solution": '''def interval_intersection(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    res = []
    i = j = 0
    while i < len(a) and j < len(b):
        lo = max(a[i][0], b[j][0])
        hi = min(a[i][1], b[j][1])
        if lo <= hi:
            res.append([lo, hi])
        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1
    return res''',
        "time": "O(M+N)", "space": "O(M+N)",
        "related": ["merge-intervals"],
    },
    {
        "slug": "minimum-arrows-balloons", "title": "Minimum Number of Arrows to Burst Balloons", "pattern": "merge-intervals", "tier": "B",
        "companies": "Amazon, Google", "difficulty": "Medium", "leetcode": 452,
        "cue": "Min points to stab all intervals → greedy by end",
        "problem": "Return the minimum number of arrows to burst all balloons (intervals).",
        "solution": '''def find_min_arrow_shots(points: list[list[int]]) -> int:
    if not points:
        return 0
    points.sort(key=lambda x: x[1])
    arrows = 1
    end = points[0][1]
    for s, e in points[1:]:
        if s > end:
            arrows += 1
            end = e
    return arrows''',
        "time": "O(N log N)", "space": "O(1)",
        "related": ["non-overlapping-intervals"],
    },
    {
        "slug": "employee-free-time", "title": "Employee Free Time", "pattern": "merge-intervals", "tier": "C",
        "companies": "Amazon, Google, LinkedIn", "difficulty": "Hard", "leetcode": 759,
        "cue": "Common free gaps across schedules → flatten, sort, find gaps",
        "problem": "Given each employee's sorted busy intervals, return the common free time intervals.",
        "solution": '''def employee_free_time(schedule: list[list[list[int]]]) -> list[list[int]]:
    intervals = sorted([iv for emp in schedule for iv in emp], key=lambda x: x[0])
    res = []
    end = intervals[0][1]
    for s, e in intervals[1:]:
        if s > end:
            res.append([end, s])                 # gap = free time
        end = max(end, e)
    return res''',
        "time": "O(N log N)", "space": "O(N)",
        "related": ["merge-intervals", "meeting-rooms-ii"],
    },
]

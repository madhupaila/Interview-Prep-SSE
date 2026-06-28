# -*- coding: utf-8 -*-
"""Fast & Slow Pointers questions."""

_LISTNODE = '''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''

QUESTIONS = [
    {
        "slug": "linked-list-cycle", "title": "Linked List Cycle", "pattern": "fast-slow-pointers", "tier": "A",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Easy", "leetcode": 141,
        "cue": "Detect a cycle → slow 1x, fast 2x; they meet iff cycle",
        "problem": "Return True if the linked list has a cycle.",
        "solution": _LISTNODE + '''
def has_cycle(head) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False''',
        "time": "O(N)", "space": "O(1)",
        "related": ["linked-list-cycle-ii", "middle-of-linked-list"],
    },
    {
        "slug": "middle-of-linked-list", "title": "Middle of the Linked List", "pattern": "fast-slow-pointers", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 876,
        "cue": "Find midpoint in one pass → fast moves twice as fast",
        "problem": "Return the middle node (second middle if even length).",
        "solution": _LISTNODE + '''
def middle_node(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow''',
        "time": "O(N)", "space": "O(1)",
        "related": ["linked-list-cycle", "reorder-list"],
    },
    {
        "slug": "happy-number", "title": "Happy Number", "pattern": "fast-slow-pointers", "tier": "A",
        "companies": "Amazon, Google, Uber", "difficulty": "Easy", "leetcode": 202,
        "cue": "Sequence cycles? → Floyd on digit-square-sum",
        "problem": "A number is happy if repeatedly summing squares of digits reaches 1. Return True/False.",
        "solution": '''def is_happy(n: int) -> bool:
    def nxt(x):
        return sum(int(d) ** 2 for d in str(x))
    slow = n
    fast = nxt(n)
    while fast != 1 and slow != fast:
        slow = nxt(slow)
        fast = nxt(nxt(fast))
    return fast == 1''',
        "time": "O(log N) per step", "space": "O(1)",
        "related": ["linked-list-cycle"],
    },
    {
        "slug": "linked-list-cycle-ii", "title": "Linked List Cycle II", "pattern": "fast-slow-pointers", "tier": "B",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 142,
        "cue": "Find cycle start → meet, then reset one pointer to head",
        "problem": "Return the node where the cycle begins, or None.",
        "identify": "After meeting, distance from head to start equals distance from meeting point to start — move both at 1x to meet there.",
        "solution": _LISTNODE + '''
def detect_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None
    slow = head
    while slow is not fast:
        slow = slow.next
        fast = fast.next
    return slow''',
        "time": "O(N)", "space": "O(1)",
        "related": ["linked-list-cycle", "find-the-duplicate-number"],
    },
    {
        "slug": "palindrome-linked-list", "title": "Palindrome Linked List", "pattern": "fast-slow-pointers", "tier": "B",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Easy", "leetcode": 234,
        "cue": "List palindrome in O(1) space → find middle, reverse half, compare",
        "problem": "Return True if the linked list is a palindrome, ideally O(1) space.",
        "solution": _LISTNODE + '''
def is_palindrome(head) -> bool:
    slow = fast = head
    while fast and fast.next:                    # find middle
        slow = slow.next
        fast = fast.next.next
    prev = None                                  # reverse second half
    while slow:
        slow.next, prev, slow = prev, slow, slow.next
    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left, right = left.next, right.next
    return True''',
        "time": "O(N)", "space": "O(1)",
        "related": ["middle-of-linked-list", "reverse-linked-list"],
    },
    {
        "slug": "remove-nth-from-end", "title": "Remove Nth Node From End of List", "pattern": "fast-slow-pointers", "tier": "B",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 19,
        "cue": "Nth from end in one pass → gap of n between two pointers",
        "problem": "Remove the nth node from the end and return the head.",
        "solution": _LISTNODE + '''
def remove_nth_from_end(head, n: int):
    dummy = ListNode(0, head)
    fast = slow = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next''',
        "time": "O(N)", "space": "O(1)",
        "edges": ["Remove head (dummy handles)", "n == length"],
        "related": ["middle-of-linked-list"],
    },
    {
        "slug": "reorder-list", "title": "Reorder List", "pattern": "fast-slow-pointers", "tier": "C",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 143,
        "cue": "L0→Ln→L1→Ln-1... → find middle, reverse second half, merge",
        "problem": "Reorder list to L0→Ln→L1→Ln-1→… in place.",
        "solution": _LISTNODE + '''
def reorder_list(head) -> None:
    if not head or not head.next:
        return
    slow = fast = head                           # find middle
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next                           # reverse second half
    slow.next = None
    prev = None
    while second:
        second.next, prev, second = prev, second, second.next
    first, second = head, prev                   # merge alternately
    while second:
        first.next, first = second, first.next
        second.next, second = first, second.next''',
        "time": "O(N)", "space": "O(1)",
        "related": ["middle-of-linked-list", "reverse-linked-list"],
    },
]

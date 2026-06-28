# -*- coding: utf-8 -*-
"""In-place Linked List Reversal questions."""

_LISTNODE = '''class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
'''

QUESTIONS = [
    {
        "slug": "reverse-linked-list", "title": "Reverse Linked List", "pattern": "linked-list-reversal", "tier": "A",
        "companies": "Amazon, Meta, Microsoft, Apple", "difficulty": "Easy", "leetcode": 206,
        "cue": "Reverse a list → flip pointers with prev/cur/next",
        "problem": "Reverse a singly linked list and return the new head.",
        "solution": _LISTNODE + '''
def reverse_list(head):
    prev = None
    cur = head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    return prev''',
        "time": "O(N)", "space": "O(1)",
        "related": ["reverse-linked-list-ii", "reverse-nodes-in-k-group"],
    },
    {
        "slug": "merge-two-lists-recursive", "title": "Merge Two Sorted Lists (Recursive)", "pattern": "linked-list-reversal", "tier": "A",
        "companies": "Amazon, Microsoft", "difficulty": "Easy", "leetcode": 21,
        "cue": "Recursive list build → pick smaller head, recurse",
        "problem": "Merge two sorted linked lists recursively.",
        "solution": _LISTNODE + '''
def merge_two_lists(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    if l1.val <= l2.val:
        l1.next = merge_two_lists(l1.next, l2)
        return l1
    l2.next = merge_two_lists(l1, l2.next)
    return l2''',
        "time": "O(M+N)", "space": "O(M+N) stack",
        "related": ["merge-two-sorted-lists"],
    },
    {
        "slug": "remove-linked-list-elements", "title": "Remove Linked List Elements", "pattern": "linked-list-reversal", "tier": "A",
        "companies": "Amazon, Google", "difficulty": "Easy", "leetcode": 203,
        "cue": "Delete all nodes equal to val → dummy head + rewire",
        "problem": "Remove all nodes with `Node.val == val`.",
        "solution": _LISTNODE + '''
def remove_elements(head, val: int):
    dummy = ListNode(0, head)
    cur = dummy
    while cur.next:
        if cur.next.val == val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return dummy.next''',
        "time": "O(N)", "space": "O(1)",
        "related": ["reverse-linked-list"],
    },
    {
        "slug": "reverse-linked-list-ii", "title": "Reverse Linked List II", "pattern": "linked-list-reversal", "tier": "B",
        "companies": "Amazon, Meta, Microsoft", "difficulty": "Medium", "leetcode": 92,
        "cue": "Reverse a sublist [left, right] → dummy + reverse in place",
        "problem": "Reverse the nodes from position `left` to `right` (1-indexed) and return the head.",
        "solution": _LISTNODE + '''
def reverse_between(head, left: int, right: int):
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(left - 1):
        prev = prev.next
    cur = prev.next
    for _ in range(right - left):                # repeatedly move cur.next after prev
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = prev.next
        prev.next = nxt
    return dummy.next''',
        "time": "O(N)", "space": "O(1)",
        "related": ["reverse-linked-list", "reverse-nodes-in-k-group"],
    },
    {
        "slug": "swap-nodes-in-pairs", "title": "Swap Nodes in Pairs", "pattern": "linked-list-reversal", "tier": "B",
        "companies": "Amazon, Microsoft, Bloomberg", "difficulty": "Medium", "leetcode": 24,
        "cue": "Swap adjacent nodes → dummy + rewire two at a time",
        "problem": "Swap every two adjacent nodes and return the head.",
        "solution": _LISTNODE + '''
def swap_pairs(head):
    dummy = ListNode(0, head)
    prev = dummy
    while prev.next and prev.next.next:
        first = prev.next
        second = first.next
        first.next = second.next
        second.next = first
        prev.next = second
        prev = first
    return dummy.next''',
        "time": "O(N)", "space": "O(1)",
        "related": ["reverse-nodes-in-k-group"],
    },
    {
        "slug": "rotate-list", "title": "Rotate List", "pattern": "linked-list-reversal", "tier": "B",
        "companies": "Amazon, Microsoft, LinkedIn", "difficulty": "Medium", "leetcode": 61,
        "cue": "Rotate right by k → close into ring, cut at new tail",
        "problem": "Rotate the list to the right by `k` places.",
        "solution": _LISTNODE + '''
def rotate_right(head, k: int):
    if not head or not head.next or k == 0:
        return head
    n = 1
    tail = head
    while tail.next:
        tail = tail.next
        n += 1
    k %= n
    if k == 0:
        return head
    tail.next = head                             # make ring
    steps = n - k
    new_tail = head
    for _ in range(steps - 1):
        new_tail = new_tail.next
    new_head = new_tail.next
    new_tail.next = None
    return new_head''',
        "time": "O(N)", "space": "O(1)",
        "related": ["reverse-linked-list"],
    },
    {
        "slug": "add-two-numbers", "title": "Add Two Numbers", "pattern": "linked-list-reversal", "tier": "B",
        "companies": "Amazon, Meta, Microsoft, Adobe", "difficulty": "Medium", "leetcode": 2,
        "cue": "Add digit lists with carry → build new list",
        "problem": "Add two numbers represented as reversed-digit linked lists; return the sum list.",
        "solution": _LISTNODE + '''
def add_two_numbers(l1, l2):
    dummy = tail = ListNode()
    carry = 0
    while l1 or l2 or carry:
        s = carry
        if l1:
            s += l1.val; l1 = l1.next
        if l2:
            s += l2.val; l2 = l2.next
        carry, digit = divmod(s, 10)
        tail.next = ListNode(digit)
        tail = tail.next
    return dummy.next''',
        "time": "O(max(M,N))", "space": "O(max(M,N))",
        "related": ["add-two-numbers-ii"],
    },
    {
        "slug": "reverse-nodes-in-k-group", "title": "Reverse Nodes in k-Group", "pattern": "linked-list-reversal", "tier": "C",
        "companies": "Amazon, Meta, Microsoft, Google", "difficulty": "Hard", "leetcode": 25,
        "cue": "Reverse every k nodes → count k, reverse block, recurse/link",
        "problem": "Reverse the list nodes `k` at a time; leftover tail (< k) stays as is.",
        "identify": "Confirm k nodes exist, reverse exactly k by pointer flipping, then connect the reversed block's tail to the recursively-processed remainder.",
        "solution": _LISTNODE + '''
def reverse_k_group(head, k: int):
    node = head
    count = 0
    while node and count < k:
        node = node.next
        count += 1
    if count < k:
        return head                              # fewer than k → leave as is
    prev, cur = None, head
    for _ in range(k):
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    head.next = reverse_k_group(cur, k)          # head is now tail of group
    return prev''',
        "time": "O(N)", "space": "O(N/k) recursion",
        "related": ["reverse-linked-list-ii", "swap-nodes-in-pairs"],
    },
]

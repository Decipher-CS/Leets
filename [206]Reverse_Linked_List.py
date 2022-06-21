# 206. Reverse Linked List

# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]


# Example 2:

# Input: head = [1,2]
# Output: [2,1]
# Example 3:

# Input: head = []
# Output: []

# Constraints:

# The number of nodes in the list is the range [0, 5000].
# -5000 <= Node.val <= 5000


import queue
from turtle import heading
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iteration 1
class Solution:
    def reverseList(self, head: Optional[ListNode]):
        q = []
        node = head
        
        while node:
            q.append(node)
            node = node.next

        if q:
            head = q.pop()
        
        node = head

        while q:
            node.next = q.pop()
            node = node.next
            node.next = None
        
        return head

# Iteration 2
class Solution:
    def reverseList(self, head: Optional[ListNode]):
        pre = None
        current = head
        
        while current:
            next = current.next
            current.next = pre
            pre = current
            current = next
        return pre

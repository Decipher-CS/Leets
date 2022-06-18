# 141. Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).


# Example 2:

# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.


# Example 3:

# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.


# Definition for singly-linked list.


from typing import Optional

from requests import head


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]):
        ll_map = {}
        ptr = head
        while 1:
            if ptr == None:
                return False
            if ptr in ll_map.keys():
                return True
            ll_map[ptr] = ptr.val
            ptr = ptr.next
        return False


inputs_constructor = [
    {
        'head' : [3,2,0,-4],
        'pos' : 1
    },
    {
        'head' : [1,2],
        'pos' : 0
    },
    {
        'head' : [1],
        'pos' : -1
    }
]

inputs = []

for input in inputs_constructor:
    head = ListNode(input['head'][0])
    curr_ptr = head
    for index in range(1, len(input['head'])):
        new_node = ListNode(input['head'][index])
        curr_ptr.next = new_node
        curr_ptr = curr_ptr.next
    
    cycle_index = input['pos']   
    if cycle_index != -1:
        ptr = head
        while cycle_index != 0:
            cycle_index -= 1
            ptr = ptr.next
        
        curr_ptr.next = ptr
    inputs.append(head)

for input in inputs:
    print(Solution().hasCycle(input))
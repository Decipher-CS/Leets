# 21. Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.


# Example 1:

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]


# Example 2:

# Input: list1 = [], list2 = []
# Output: []


# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        pass


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
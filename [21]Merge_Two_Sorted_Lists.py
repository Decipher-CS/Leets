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



from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
#         final_list_ptr = None
#         final_list_head = None
#         ptr1 = list1
#         ptr2 = list2
        
#         while True:
#             if not final_list_ptr:
#                 if ((ptr1) and (ptr2)):
#                     if (ptr1) and (ptr1.val <= ptr2.val):
#                         final_list_ptr = ListNode(ptr1.val)
#                         ptr1 = ptr1.next
#                     elif (ptr2) and (ptr2.val <= ptr1.val):
#                         final_list_ptr = ListNode(ptr2.val)
#                         ptr2 = ptr2.next
#                 elif ptr1 and not ptr2:
#                         final_list_ptr.next = ListNode(ptr1.val)
#                         ptr1 = ptr1.next
#                 elif ptr2 and not ptr1:
#                         final_list_ptr.next = ListNode(ptr2.val)
#                         ptr2 = ptr2.next
#                 final_list_head = final_list_ptr
#                 continue


#             if ((ptr1) and (ptr2)):
#                 if (ptr1.val <= ptr2.val):
#                     final_list_ptr.next = ListNode(ptr1.val)
#                     ptr1 = ptr1.next
#                 elif (ptr2) and (ptr2.val <= ptr1.val):
#                     final_list_ptr.next = ListNode(ptr2.val)
#                     ptr2 = ptr2.next
#                 else: break
#             elif ptr1 and not ptr2:
#                     final_list_ptr.next = ListNode(ptr1.val)
#                     ptr1 = ptr1.next
#             elif ptr2 and not ptr1:
#                     final_list_ptr.next = ListNode(ptr2.val)
#                     ptr2 = ptr2.next

#             final_list_ptr = final_list_ptr.next

#         return final_list_head

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]):
        head_node = ListNode()
        curr_node = head_node
        
        while (list1 and list2):
            if list1.val < list2.val:
                curr_node = list1
                list1 = list1.next
            elif list2.val < list1.val:
                curr_node = list2
                list2 = list2.next
            
            curr_node.next = ListNode()
            curr_node = curr_node.next
        
        list = list1 if list1 else list2
        while list:
            curr_node = list
            list = list.next
            if (list):
                curr_node.next = ListNode()
                curr_node = curr_node.next
        
        return head_node

inputs_constructor = [
    {
        'list1' : [1,2,4],
        'list2' : [1,3,4]
    },
    # {
    #     'list1' : [],
    #     'list2' : [],
    # }
]

inputs = []

# for input in inputs_constructor:
#     head = ListNode(input['head'][0])
#     curr_ptr = head
#     for index in range(1, len(input['list1'])):
#         new_node = ListNode(input['list1'][index])
#         curr_ptr.next = new_node
#         curr_ptr = curr_ptr.next
    
#     cycle_index = input['pos']   
#     if cycle_index != -1:
#         ptr = head
#         while cycle_index != 0:
#             cycle_index -= 1
#             ptr = ptr.next
        
#         curr_ptr.next = ptr
#     inputs.append(head)


for input in inputs:
    print(input)
    print(Solution().hasCycle(input))

# he = ListNode(1)
# if (he.next) and (print('h')):
#     print("hi")
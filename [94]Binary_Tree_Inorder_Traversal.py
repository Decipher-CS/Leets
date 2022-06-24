from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Solution
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]):
#         result = []
#         def inorder(node):
#             if not node:
#                 return None
#             inorder(node.left)
#             result.append(node.val)
#             inorder(node.right)
#             return 
            
        
#         inorder(root)
#         return result

# Iterative Solution. Fails at [3,1,null,null,2]
# class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]):
#         if not root:
#             return []
#         inorder = [root]
#         result = []
#         i = 0
#         ptr = inorder[i]
#         hp = {}
#         while 1:
#             if ptr.left:
#                 inorder.insert(i, ptr.left)
#             if ptr.right:
#                 inorder.insert(i+2, ptr.right)
#             hp[ptr] = ptr
#             try:
#                 ptr, *rest = [x for x in inorder if x not in hp.keys()]
#             except ValueError:
#                 break
#             i = inorder.index(ptr)
            
#         result = [node.val for node in inorder]
#         return result

# Iterative Solution. 
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]):
        stk = []
        result = []
        ptr = root
        while 1:
            while ptr:
                stk.append(ptr)
                ptr = ptr.left
            if not stk:
                break
            ptr = stk.pop()
            result.append(ptr.val)
            ptr = ptr.right
        return result



head = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(Solution().inorderTraversal(head))

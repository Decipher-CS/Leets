from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]):
        result = []
        def inorder(node):
            if not node:
                return None
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
            return 
            
        
        inorder(root)
        return result

head = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(Solution().inorderTraversal(head))
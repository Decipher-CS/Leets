from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Solution
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]):
        preorder = []
        def traversal(root):
            if not root:
                return None
            preorder.append(root.val)
            traversal(root.left)
            traversal(root.right)
            return None
        
        traversal(root)
        return preorder

# Iterative Solution    
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]):
        _ = [root]
        result = []
        while _:
            ptr = _.pop()
            if not ptr:
                continue
            result.append(ptr.val)
            _.append(ptr.right)
            _.append(ptr.left)
        return result


head = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(Solution().preorderTraversal(head))
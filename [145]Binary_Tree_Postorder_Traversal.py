# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive Solution
class Solution:
    def postorderTraversal(self, root):
        result = []

        def postorder(node):
            if not node:
                return None

            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
            return node

        postorder(root)
        return result


# Iterative Solution
class Solution:
    def postorderTraversal(self, root):
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
print(Solution().postorderTraversal(head))

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
        # stk = []
        # result = []
        # ptr = root
        # while 1:
        #     while ptr:
        #         stk.append(ptr)
        #         ptr = ptr.left
        #     if not stk:
        #         break
        #     ptr = stk.pop()
        #     result.append(ptr.val)
        #     ptr = ptr.right
        # return result
        
        stk = []
        result = []
        node = root
        
        while 1:
            while 1:
                stk.append(node)
                if not node.left:
                    break
                node = node.left
            if node.right:
                node = node.right
                stk.append(node)
            result.append(node.val)
            node = stk.pop()
            


head = TreeNode(1, None, TreeNode(2, TreeNode(3), None))
print(Solution().postorderTraversal(head))

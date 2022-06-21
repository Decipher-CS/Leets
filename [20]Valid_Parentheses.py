# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

# Example 3:

# Input: s = "(]"
# Output: false

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


class Solution:
    def isValid(self, s: str):
        # if len(s) % 2 != 0:
        #     return False
        # for index in range(0, len(s)-1, 2):
        #     if (s[index] == '('):
        #         if s[index+1] == ')':
        #             continue
        #     elif (s[index] == '['):
        #         if s[index+1] == ']':
        #             continue
        #     elif (s[index] == '{'):
        #         if s[index+1] == '}':
        #             continue
        #     return False
        # return True


inputs = [
    '()',
    '()[]{}'
]

for input in inputs:
    print(Solution().isValid(input))
    
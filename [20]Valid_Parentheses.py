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
        if len(s) % 2 != 0:
            return False
        corresponding_dict = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        stk = []
        
        for char in s:
            if char in '{[(':
                stk.append(char)

            elif char in ')]}':
                if len(stk) < 1:
                    return False
                value = corresponding_dict[ stk.pop() ]

                if value != char:
                    return False
        
        return False if len(stk) > 0 else True


inputs = [
    '((',
    # '()[]{}'
]

for input in inputs:
    print(Solution().isValid(input))
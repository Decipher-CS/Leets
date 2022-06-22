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

# Third Iteration
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

# Second Iteration
class Solution:
    def isValid(self, s: str):
        if len(s) % 2 != 0:
            return False
        
        if ( s[0] in ')]}' ) or ( s[-1] in '{[('):
            return False
        
        corresponding_dict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stk = []
        
        for ch in s:
            if stk and ( ch in corresponding_dict.keys() ):
                if corresponding_dict[ch] != stk.pop():
                    return False

            elif ch in '([{':
                stk.append(ch)
            
            else: return False
        
        return True if not stk else False

# Third and Final Iteration
class Solution:
    def isValid(self, s: str):
        if len(s) % 2 != 0:
            return False
        
        corresponding_dict = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        stk = []
        
        for ch in s:
            if ch in '([{':
                stk.append(ch)

            else:
                if not stk or corresponding_dict[ch] != stk.pop():
                    return False

                    
        return True if not stk else False


inputs = [
    # '((',
    # '()[]{}'
    # "()",
    # "()[]{}",
    # "{()()[][]{{()}}}",
    # "[]{}{()(]}",
    # "(]",
    # "((",
    '()[]'
]

for input in inputs:
    print(Solution().isValid(input))
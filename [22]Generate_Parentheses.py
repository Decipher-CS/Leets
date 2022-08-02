import collections
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        validParenthesis = []
        def parenthesis(brackets: str):
            if len(brackets) >= (n*2):
                if Solution.isParenthesisValid(brackets):
                    validParenthesis.append(brackets)
                return
            parenthesis(brackets + '(')
            parenthesis(brackets + ')')
        parenthesis("")
        return validParenthesis


    def isParenthesisValid(str):
        stk = collections.deque()
        for ch in str:
            if ch == "(":
                stk.append(ch)
            else:
                if not stk or stk.pop() != "(":
                    return False
                
        return True if not stk else False



inputs = [3,1]

for input in inputs:
    print(Solution().generateParenthesis(input))
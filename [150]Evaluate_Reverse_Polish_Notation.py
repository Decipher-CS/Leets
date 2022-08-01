import collections
from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()

        for token in tokens:
            if not token in '+-*/':
                stack.append(int(token))
                continue

            val1, val2= stack.pop(), stack.pop()
            
            if token == '+':
                result = val1 + val2
            elif token == '-':
                result = val2 - val1
            elif token == '*':
                result = val1 * val2
            else:
                result = val2 / val1

            stack.append(int(result))

        return stack.pop()

tokens = [
    ["2","1","+","3","*"], # output => 9
    ["4","13","5","/","+"], # output: 6
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"], # output => 22
    ["4","3","-"] # output => 1
]

for token in tokens:
    print(Solution().evalRPN(token))
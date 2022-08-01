from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if not token in '+-*/':
                stack.append(int(token))
                continue
            if token == '-':
                val1 = stack.pop() 
                val2 = stack.pop()
                stack.append(int(val2 - val1))
            elif token == '+':
                stack.append(int(stack.pop() + stack.pop()))
            elif token == '*':
                stack.append(int(stack.pop() * stack.pop()))
            else:
                val1 = stack.pop() 
                val2 = stack.pop()
                stack.append(int(val2 / val1))
        return stack[0]

tokens = [
    ["2","1","+","3","*"], # output => 9
    ["4","13","5","/","+"], # output: 6
    ["10","6","9","3","+","-11","*","/","*","17","+","5","+"], # output => 22
    ["4","3","-"] # output => 1
]

for token in tokens:
    print(Solution().evalRPN(token))
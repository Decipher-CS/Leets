from numpy import Infinity, array

class MinStack:

    def __init__(self):
        self.stack = [[0,Infinity]]
        self.top_ptr = -1

    def push(self, val: int) -> None:
        self.top_ptr += 1
        if self.top_ptr >= len(self.stack):
            self.stack.append([0,Infinity])

        self.stack[self.top_ptr][0] = val
        if self.top_ptr-1 == -1:
            self.stack[self.top_ptr][1] = val
        elif val < self.stack[self.top_ptr-1][1]:
            self.stack[self.top_ptr][1] = val
        else:
            self.stack[self.top_ptr][1] = self.stack[self.top_ptr-1][1]


    def pop(self) -> None:
        self.top_ptr -= 1
        return self.stack[self.top_ptr+1][0]

    def top(self) -> int:
        return self.stack[self.top_ptr][0]
        

    def getMin(self) -> int:
        return self.stack[self.top_ptr][1]
        


# MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(5)
obj.push(3)
obj.push(4)
print(obj.pop())
print(obj.pop())
print('min value is : ', obj.getMin())
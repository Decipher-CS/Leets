class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        while 1:
            mid = (right + left)//2
            sqr = mid*mid

            if (left>right):
                return mid

            if (sqr == x):
                return mid
            elif (sqr > x):
                right = mid-1 
            else:
                left = mid+1
        
        return -1


inputs = [
    [4, 2],
    [8, 2],
    [0, 0],
    [1, 1],
    [20000000000, 1],
    [99999999, 9]
    
]
for sqr, root in inputs:
    print(f'root of {sqr} should be {root} : res => ', Solution().mySqrt(sqr))
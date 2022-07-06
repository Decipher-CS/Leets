

class Solution:
    def climbStairs(self, n: int):
        global steps
        steps = 0
        def calcStairs(step: int):
            if (step == n):
                global steps
                steps += 1
                return 1
            elif (step > n):
                return 0
                
            calcStairs(step + 1)
            calcStairs(step + 2)
            
            return 
        calcStairs(0)
        return steps



print(Solution().climbStairs(4))

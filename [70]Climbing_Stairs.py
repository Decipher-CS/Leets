

class Solution:
    def climbStairs(self, n: int):
        steps = 0
        def calcStairs(step: int):
            if (step == n):
                step += 1
                return 1
            elif (step > n):
                return 0
            
            self.climbStairs(step + 1)
            self.climbStairs(step + 2)
            
            return 
        calcStairs(n)
        return steps



print(Solution().climbStairs(5))

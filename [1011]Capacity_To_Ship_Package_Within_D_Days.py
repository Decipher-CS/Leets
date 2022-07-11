from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int):
        left = 1
        right = 600
        mid = 0
        while (right >= left):
            mid = (right + left) // 2
            d = self.shipWithinDays_helper(weights, days, mid)
            if not(d):
                right -= 1
            if (d < 0):
                left = mid+1
            else:
                right = mid-1
        
        return mid

    def shipWithinDays_helper(self, weights, d, weight_capacity):
        running_sum = 0
        d -= 1
        for w in weights:
            if ((running_sum + w) <= weight_capacity):
                running_sum += w
            else:
                d -= 1
                running_sum = w
        if (d == 0):
            return 0
        elif (d < 0):
            return -1
        else:
            return 1

inputs = [
    # [[1,2,3,4,5,6,7,8,9,10], 5],
    [[3,2,2,4,1,4], 3],
]

for weights, days in inputs:
    print(Solution().shipWithinDays(weights, days))
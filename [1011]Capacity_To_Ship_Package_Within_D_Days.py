from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int):
        min_weight = max(weights)
        least_weight_capacity = min_weight
        total_weight = sum(weights)
        while (least_weight_capacity <= total_weight):
            running_sum = 0
            d = days
            for w in weights:
                if ((running_sum + w) <= least_weight_capacity):
                    running_sum += w
                else:
                    d -= 1
                    running_sum = w
            if (d > 0):
                return least_weight_capacity
            else:
                least_weight_capacity += 1

inputs = [
    [[1,2,3,4,5,6,7,8,9,10], 5],
    [[3,2,2,4,1,4], 3],
]

for weights, days in inputs:
    print(Solution().shipWithinDays(weights, days))
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
        
        return left


inputs = [
    [[4,5,6,7,0,1,2], 0]
]

for arr, target in inputs:
    print(Solution().search(arr, target))
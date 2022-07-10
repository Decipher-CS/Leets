from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        while i<n:
            if (i != nums[i]):
                return i
            i+=1
        return i
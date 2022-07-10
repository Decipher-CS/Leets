from typing import List


class Solution:
        # Gauss method
    def missingNumber(self, nums: List[int]) -> int:
        return ( ((len(nums)+1) * len(nums))  // 2 ) - sum(nums)

        # XOR method
    def missingNumber_xor(self, nums: List[int]) -> int:
        array = [i for i in range(len(nums)+1)]
        diff = (set(array) ^ set(nums))
        return diff.pop()

        # Comparing sorted list
    def missingNumber_sorted(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        i = 0
        while i<n:
            if (i != nums[i]):
                return i
            i+=1
        return i

print(Solution().missingNumber([1,2,0,4,5,6]))
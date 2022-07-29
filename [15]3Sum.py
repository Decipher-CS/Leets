class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        pivot = 0
        left = 1
        right = len(nums)-1
        result = []

        while pivot < len(nums)-2:
            while left < right:
                while left < right:
                    sum = nums[pivot] + nums[left] + nums[right]
                    if sum == 0:
                        result.append([nums[pivot] , nums[left] , nums[right]])
                    left += 1
                right -= 1
                left = pivot + 1
            pivot += 1
            left = pivot + 1
            right = len(nums)-1
        
        result = [tuple(res) for res in result]
        result = tuple(result)
        result = set(result)
        return result if result else []

nums = [
    [-1,0,1,2,-1,-4],
    [0,1,1],
    [0,0,0]
]

for num in nums:
    print(Solution().threeSum(num))
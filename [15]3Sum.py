
class Solution:
    def threeSum(self, nums):
        if not nums:
            return []
        nums = sorted(nums)
        pivot = 0
        result = []
        left = pivot + 1
        right = len(nums)-1
        print(nums)

        while pivot < len(nums)-2:
            if (pivot != 0) and (nums[pivot] == nums[pivot-1]):
                pivot +=1
                left += 1
                continue
            sum = nums[pivot] + nums[left] + nums[right]
            if sum == 0:
                result.append([ nums[pivot], nums[left] , nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left +=1
                while left < right and nums[right] == nums[left-1]:
                    right -=1
                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            elif sum > 0:
                right -= 1

            if left >= right:
                pivot += 1
                left = pivot + 1
                right = len(nums)-1
        return result

    def threeSum_slow(self, nums):
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
    # [-1,0,1,2,-1,-4],
    # [0,1,1],
    # [0,0,0],
    # [3,0,-2,-1,1,2], # ans ->  [[-2,-1,3],[-2,0,2],[-1,0,1]]
    [-1,0,1,2,-1,-4,-2,-3,3,0,4], # ans ->[[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]] 
]

for num in nums:
    print(Solution().threeSum(num))
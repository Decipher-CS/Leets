from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            if (  ((nums[mid] < nums[left]) and (target < nums[left])) or ((nums[mid] > nums[left]) and (target >= nums[left]))  ):
                if nums[mid] > target:
                    right = mid-1
                else:
                    left = mid+1
                
            elif nums[mid] < nums[left]: #Mid is in the original array
                right = mid-1
                pass
            else: #Mid is in rotated array
                left = mid+1
            
        return -1


inputs = [
    [[6,7,1,2,3,4,5], 6],
    [[4,5,6,7,0,1,2], 0],
    [[4,5,6,7,0,1,2], 3],
    [[1], 0]
]

for arr, target in inputs:
    print(Solution().search(arr, target))
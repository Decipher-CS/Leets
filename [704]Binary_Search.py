class Solution:
    def search(self, nums, target: int):
        mid = int (len(nums)/2)
        left = 0
        right = len(nums) -1
        
        while :
            value = nums[mid]
            mid = left + (right-left) 

            if (value == target):
                return 1
            
            if (value < target):  # Remove left
                right = mid
            else:                 # Remove right
                left = mid
        
        return -1


arr = [-1,0,3,5,9,12]
target = 9
print(Solution().search(arr, target))
# print((int)(7/2))
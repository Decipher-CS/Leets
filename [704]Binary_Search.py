from jmespath import search


class Solution:
    # recursive
    def search(self, nums, target: int):
        if not nums:
            return -1
        
        mid = int (len(nums) / 2)
        
        if (nums[mid] < target):
            search(nums[mid+1:], target)
        elif (nums[mid] > target):
            search(nums[:mid], target)
        
        
    def search_iterative(self, nums, target: int):
        left = 0
        right = len(nums) 
        
        while 1:
            mid = int (left +( (right-left)/2 ))
            value = nums[mid]

            if (value == target):
                return mid
            elif ((left == mid) or (right == mid)):
                return -1
            
            if (value < target):  # Remove left
                left = mid
            else:                 # Remove right
                right = mid
        
        return -1


arr = [-1,0,3,5,9,12]
target = 12
print(Solution().search(arr, target))
# print((int)(7/2))
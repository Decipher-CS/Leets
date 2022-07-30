class Solution:
    def maxArea(self, height):
        dist = 1
        area = 0
        
        for left in range(len(height)):
            for right in range(left+1, len(height)):
                dist = right - left
                temp_area = (dist * height[left]) if (height[left] <= height[right]) else (dist * height[right])
                area = temp_area if temp_area > area else area
                
        return area



nums = [
    [1,8,6,2,5,4,8,3,7],
    [0,0],
    [1,1],
]

for num in nums:
    print(Solution().maxArea(num))
class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        area = 0
        while left < right:
            smaller = height[left] if height[left] < height[right] else height[right]
            dist = right - left
            area =  dist * smaller if (dist * smaller) > area else area
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return area

    def maxArea_BruteForce(self, height):
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
    [1,2,1]
]

for num in nums:
    print(Solution().maxArea(num))
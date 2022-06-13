# 350. Intersection of Two Arrays II

# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]


# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.


# Constraints:

# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 1000


# Follow up:

# What if the given array is already sorted? How would you optimize your algorithm?
# What if nums1's size is small compared to nums2's size? Which algorithm is better?
# What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

from typing import List
import numpy



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]):
        value_map1 = {}
        value_map2 = {}
        intersection_array = []
        
        for num in nums1:
            if value_map1.get(num):
                value_map1[num] = value_map1.get(num) + 1
            else:
                value_map1[num] = 1

        for num in nums2:
            if value_map2.get(num):
                value_map2[num] = value_map2.get(num) + 1
            else:
                value_map2[num] = 1
        print(value_map1, value_map2)
        
        for key in value_map1:
            if ( value_map2.get(key) ) and ( value_map2[key] > 0 ):
                for i in range(numpy.minimum(value_map1[key], value_map2[key])):
                    intersection_array.append(key)
        
        return intersection_array

nums1 = [1,2,2,1]
nums2 = [2,2]

# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]

# nums1 = [1,2]
# nums2 = [1,1]

result = Solution().intersect(nums1, nums2)
print(result)

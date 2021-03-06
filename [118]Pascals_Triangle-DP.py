# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]


# Example 2:

# Input: numRows = 1
# Output: [[1]]

# Constraints:
# 1 <= numRows <= 30

from typing import List
"""
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_arr = [[1]]
        if numRows == 1:
            return final_arr
        def rec(arr, depth):
            new_arr = []
            for i in range(len(arr)-1):
                new_arr.append(arr[i] + arr[i+1])
            
            new_arr = [1] + new_arr + [1]
            final_arr.append(new_arr)
            if depth <= 1:
                return
            new_arr = rec(new_arr, depth-1)
            return 
        
        rec([], numRows-1)
        return  final_arr
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        final_arr = [[1], [1,1]]
        
        for row in range(2, numRows):
            new_arr = []
            for col in range(1, row):
                new_arr.append(final_arr[row-1][col-1] + final_arr[row-1][col])
            
            final_arr.append([1] + new_arr + [1])
        
        return final_arr


numRows = 5
result = Solution().generate(numRows)
print(result)

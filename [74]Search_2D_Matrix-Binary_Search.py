# 74. Search a 2D Matrix
# ￼
# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.


# Example 1:
# ￼
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true


# Example 2:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from timeit import timeit
from typing import List
import numpy

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):
        merged_matrix = []
        for mat in matrix:
            merged_matrix +=mat
        while len(merged_matrix) >= 1:     #Change this
            mid = int( len(merged_matrix) / 2 )
            value = merged_matrix[mid]
            if value == target:
                return True
            if target < value:
                merged_matrix = merged_matrix[:mid]
            elif target > value:
                merged_matrix = merged_matrix[mid+1:]
            
        return False

# if target in array return True

matrices = [
    {
        'matrix' : [[1,3,5,7],[10,11,16,20],[23,30,34,60]], 
        'target' : 3 
    },
    {
        'matrix' : [[1,3,5,7],[10,11,16,20],[23,30,34,60]],
        'target' : 13
    },
    {
        'matrix' : [[1,3]],
        'target' : 1
    }
]

for matrix in matrices:
    time = timeit(lambda: print(Solution().searchMatrix(matrix['matrix'], matrix['target'])), number=1)
    print(time)



class Solution:
    def twoSum(self, numbers , target: int):
        left = 0
        right = len(numbers) - 1
        while left < right:
            if left == right:
                continue
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left+1, right+1]
            elif sum > target:
                right -= 1
            else:
                left += 1

        return [-99999]

inputs = [
    [[2,7,11,15], 9],
    [[2,3,4], 6]
]

for array, target in inputs:
    print(Solution().twoSum(array, target))
from typing import List
from numpy import ceil


class Solution:
        # BINARY SEARCH APPROACH
    def minEatingSpeed(self, piles: List[int], h: int):
        pass
        
        # BRUTE FORCE APPROACH
    def minEatingSpeed_bruteForce(self, piles: List[int], h: int):
        piles.sort()
        speed = 1
        while (1):
            temp_h = h
            for pile in piles:
                temp_h -= ceil(pile/speed)
                temp_h = int(temp_h)
                if (temp_h < 0):
                    speed += 1
                    break
            if (temp_h >= 0):
                return speed

        return speed

inputs = [
    ([3,6,7,11], 8),
    ([30,11,23,4,20], 5),
    ([312884470], 312884469)
]

for pile, h in inputs:
    print(f'\ninput : {pile}, h : {h} solution => ', Solution().minEatingSpeed(pile, h))
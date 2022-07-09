from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int):
        bph = 1 # Bananas Per Hour

        while 1:
            temp_pile = piles[:]
            temp_h = h
            i = 0
            isEmpty = 1
            inc = -1

            while (temp_h):
                i+=inc
                if ((i == len(temp_pile)) or (i == -1)):
                    inc *= -1
                    i+=inc

                if not temp_pile[i]:
                    continue
                if ((temp_pile[i] - bph) <= 0):
                    temp_pile[i] = 0
                else:
                    temp_pile[i] -= bph
                
                temp_h -= 1

            for pile in temp_pile:
                if pile:
                    isEmpty = 0
            print(bph, temp_pile)
            if isEmpty:
                return bph
            bph += 1
        return -1

# piles = [3,6,7,11]
# h = 8
# piles = [30,11,23,4,20]
# h = 5
print(Solution().minEatingSpeed(piles, h))
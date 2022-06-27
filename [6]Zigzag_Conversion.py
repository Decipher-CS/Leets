class Solution:
    def convert(self, s: str, numRows: int):
        if numRows == 1:
            return s
        result = [[] for i in range(numRows)]
        isIncrement = True
        inc = 0
        for ch in s:
            if (inc == -1) or (inc == numRows):
                isIncrement = False if isIncrement else True
                inc = inc+2 if isIncrement else inc-2
            result[inc].append(ch)
            inc = inc+1 if isIncrement else inc-1

        ans = ""
        for res in result:
            for r in res:
                ans += r
        return ans

# Do the fastest solution from leetcode here.
# class Solution:
#     def convert(self, s: str, numRows: int):
#         str = [""] *numRows
#         isInc = True
#         inc = 1
#         i = 0
#         for ch in s:
#             str[i] += ch
#             pass

inputs = [
    ["PAYPALISHIRING", 3,"PAHNAPLSIIGYIR"],
    ["ABCDE", 4 ,"ABCED"]
]

for original_string, numRows, solution_String in inputs:
    if ( (solution_String) != (result := Solution().convert(original_string, numRows)) ):
        print("Wrong Answer  => ", result)
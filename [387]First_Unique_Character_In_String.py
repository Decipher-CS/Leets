# 387. First Unique Character in a String

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


# Example 1:

# Input: s = "leetcode"
# Output: 0


# Example 2:

# Input: s = "loveleetcode"
# Output: 2


# Example 3:

# Input: s = "aabb"
# Output: -1

# Constraints:

# 1 <= s.length <= 105
# s consists of only lowercase English letters.


class Solution:
    def firstUniqChar(self, s: str):
        repeating_char = {}
        q = []
        for index, char in enumerate(s):
            if char in repeating_char.keys():
                repeating_char[char][1] += 1
            else:
                repeating_char[char] = [index, 1]
                q.append(char)
        
        for index, char in enumerate(q):
            if repeating_char[ q[index] ][1] <= 1:
                return repeating_char[ q[index] ][0]
        return -1

strings = [
            'leetcode',
            'loveleetcode'
        ]

for s in strings:
    result = Solution().firstUniqChar(s)
    print(result)

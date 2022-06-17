# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?



class Solution:
    def isAnagram(self, s: str, t: str):
        # UNCOMMENT FOR UNICODE SUPPORT
        # 
        # if len(s) != len(t):
        #     return False
        # for char in s:
        #     if char in t:
        #         t = t.replace(char, '', 1)
        #         continue
        #     return False
        
        # Faster but only works with alphanumerics
        
        for char in 'abcdefghijklmnopqrstuvwxyz1234567890':
            if s.count(char) != t.count(char):
                return False
        
        return True

inputs = [
    {
        's' : 'anagram',
        't' : 'nagaram'
    },
    {
        's' : 'rat',
        't' : 'car'
    },
    {
        's' : 'ab',
        't' : 'a'
    },
    {
        's' : 'a',
        't' : 'ab'
    }, 
]

for input in inputs:
    print(Solution().isAnagram(input['s'], input['t']))
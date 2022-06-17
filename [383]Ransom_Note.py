# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false


# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false


# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

# Constraints:

# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str):
        for letter in ransomNote:
            isFound = magazine.find(letter)
            if isFound == -1:
                return False
            magazine = magazine.replace(letter, '', 1)
        return True

inputs = [
    {
        'ransomNote' : 'a',
        'magazine' : 'b'
    },
    {
        'ransomNote' : 'aa',
        'magazine' : 'ab'
    }
]

for input in inputs:
    print(Solution().canConstruct(input['ransomNote'], input['magazine']))


class Solution:
    def isPalindrome(self, s: str):
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        l = 0
        r = len(s)-1
        while (l < r):
            if (s[l] != s[r]):
                return False
            l+=1
            r-=1
        return True

strings = [
    "A man, a plan, a canal: Panama",
    "race a car",
    " "
    "aa",
    "0P"
]

for s in strings:
    print(Solution().isPalindrome(s))
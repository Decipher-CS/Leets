class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        print(s)
        
        return False

strings = [
    "A man, a plan, a canal: Panama",
    "race a car",
]

for s in strings:
    print(Solution().isPalindrome(s))
class Solution:
    def isPalindrome(self, n: int) -> bool:
        s=str(n)
        return s==s[::-1]

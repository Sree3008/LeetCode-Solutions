class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s=list(s)
        left=0
        right=len(s)-1
        while left<right:
            if left!=right:
                mini=min(s[left],s[right])
                s[left]=mini
                s[right]=mini
            left+=1
            right-=1
        return ''.join(s)

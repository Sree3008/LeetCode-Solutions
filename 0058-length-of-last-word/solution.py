class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l1=list(map(str,s.split()))
        return len(l1[-1])

class Solution:
    def largestEven(self, s: str) -> str:
        l=s.rfind('2')
        if l==-1:
            return ''
        return s[:l+1]

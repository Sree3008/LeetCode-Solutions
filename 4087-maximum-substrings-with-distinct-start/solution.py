class Solution:
    def maxDistinct(self, s: str) -> int:
        st1=''
        for i in s:
            if i not in st1:
                st1+=i
        return len(st1)

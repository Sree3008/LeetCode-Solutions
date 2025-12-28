class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        j=0
        st=''
        for i in range(len(s)):
            if j<len(spaces) and  i==spaces[j]:
                st+=' '
                j+=1
            st+=s[i]
        return st

class Solution:
    def countKeyChanges(self, s: str) -> int:
        x=s.lower()
        c=0
        for i in range(1,len(s)):
            if(x[i]!=x[i-1]):
                c+=1
        return c

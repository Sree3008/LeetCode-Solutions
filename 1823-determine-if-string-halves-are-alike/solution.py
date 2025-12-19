class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        v=0
        v1=0
        vo='aeiouAEIOU'
        leng=len(s)//2
        for i in range(0,leng):
            if s[i] in vo:
                v+=1
        for i in range(leng,len(s)):
            if s[i] in vo:
                v1+=1
        return v==v1

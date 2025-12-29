class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        x=num
        s,y=0,0
        while x!=0:
            m=x%10
            s=s*10+m
            x//=10
        while s!=0:
            c=s%10
            y=y*10+c
            s//=10
        return num==y

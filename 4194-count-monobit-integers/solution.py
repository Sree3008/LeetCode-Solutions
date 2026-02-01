class Solution:
    def countMonobit(self, n: int) -> int:
        c=0
        x=0
        while x<=n:
            c+=1
            if x==0:
                x=1
            else:
                x=(x<<1)|1
        return c

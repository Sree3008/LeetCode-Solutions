class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        r1=bin(x)[2:]
        r2=bin(y)[2:]
        m=max(len(r1),len(r2))
        r1=r1.zfill(m)
        r2=r2.zfill(m)
        l1=list(r1)
        l2=list(r2)
        c=0
        for i in range(len(l1)):
            if l1[i]!=l2[i]: 
                c+=1
        return c      

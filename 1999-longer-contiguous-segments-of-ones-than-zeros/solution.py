class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        k=0
        c=0
        c1=0
        m=0
        for i in s:
            if i=='1':
                c+=1
                k=max(k,c)
            else:
                c=0
        for i in s:
            if i=='0':
                c1+=1
                m=max(m,c1)
            else:
                c1=0
        print(k,m)
        return k>m
        

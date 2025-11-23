class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum=0
        st=str(n)
        s=0
        for i in st:
            if i=='0':
                continue
            else:
                s=s*10+int(i) 
                sum=sum+int(i)
        print(sum)
        print(s)
        return sum*s 
                

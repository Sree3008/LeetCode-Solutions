class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(n):
            k=1
            while n>0:
                m=n%10
                k*=m
                n//=10
            return k
        while True:
            if prod(n)%t==0:
                return n
            n+=1

        



        

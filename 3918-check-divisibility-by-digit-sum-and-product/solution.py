class Solution:
    def checkDivisibility(self, n: int) -> bool:
        if n<10:
            return False
        s=0
        p=1
        res=n
        while n!=0:
            m=n%10
            s+=m 
            p*=m 
            n=n//10
        if res%(s+p)==0:
            return True 
        return False
      

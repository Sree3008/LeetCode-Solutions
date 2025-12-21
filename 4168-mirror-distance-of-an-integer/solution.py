class Solution:
    def mirrorDistance(self, n: int) -> int:
        x=str(n)
        r=x[::-1]
        res=abs(int(r)-n)
        return res
        

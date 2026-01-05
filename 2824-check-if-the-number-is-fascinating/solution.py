class Solution:
    def isFascinating(self, n: int) -> bool:
        x=str(n)
        y=str(n*2)
        z=str(n*3)
        res=x+y+z
        return len(res)==9 and set(res)==set('123456789')

class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        x=0
        for i in range(n):
            num=start+2*i
            x^=num
        return x
            
        

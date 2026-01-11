class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        e=o=id=0
        while n>0:
            if n&1:
                if id%2==0:
                    e+=1
                else:
                    o+=1
            n>>=1
            id+=1
        return [e,o]

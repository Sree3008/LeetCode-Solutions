class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        e=0
        o=0
        for i in range(1,(n*2)+1):
            if i%2==0:
                e=e+i
            else:
                o=o+i
        return math.gcd(e,o)


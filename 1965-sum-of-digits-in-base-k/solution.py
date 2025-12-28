class Solution:
    def sumBase(self, n: int, k: int) -> int:
        z=0
        while n!=0:
            z+=n%k
            n//=k
        return z

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        c=high-low+1
        if c%2==0:
            return c//2
        return c//2+(0 if low%2==0 else 1)

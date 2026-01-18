class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        y=0
        while piles:
            x=piles.pop(-1)
            y+=piles.pop(-1)
            z=piles.pop(0)
        return y
         
        

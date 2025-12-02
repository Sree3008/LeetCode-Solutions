class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        x= len(set(candyType))
            
        y=len(candyType)//2
        return min(x,y)

class Solution:
    def maxContainers(self, n: int, w: int, maxWeight: int) -> int:
        x=n*n
        y=maxWeight//w
        maxi=min(x,y)
        return maxi
        

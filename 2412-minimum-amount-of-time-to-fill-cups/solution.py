class Solution:
    def fillCups(self, amt: List[int]) -> int:
        maxi=max(amt)
        sum1=sum(amt)
        return max(maxi,(sum1+1)//2)

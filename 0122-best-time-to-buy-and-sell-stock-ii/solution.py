class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        list1=[]
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                list1.append(prices[i]-prices[i-1])
        return sum(list1)

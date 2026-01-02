class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        sum=prices[1]+prices[0]
        if sum<=money:
            return money-sum
        return money
        

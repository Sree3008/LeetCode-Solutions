class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        c=0
        costs.sort()
        sum1=0
        for i in costs:
            if sum1+i<=coins:
                sum1+=i
                c+=1
            else:
                break 
        return c

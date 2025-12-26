class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        cost.reverse()
        x=0
        for i in range(len(cost)):
            if (i + 1) % 3 != 0:
                x+=cost[i]
        return x

        

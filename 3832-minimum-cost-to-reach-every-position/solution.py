class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        list1=[]
        mini=float('inf')
        for i in range(len(cost)):
            mini=min(cost[i],mini)
            list1.append(mini)
        return list1


        

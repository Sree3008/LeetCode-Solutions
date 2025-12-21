class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        t_c=sum(cost)
        k_c=defaultdict(int)
        for ch,c in zip(s,cost):
            k_c[ch]+=c
        return t_c-max(k_c.values())
        

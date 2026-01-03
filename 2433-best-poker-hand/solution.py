class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        x=Counter(ranks)
        maxi=max(x.values())
        if len(set(suits))==1: 
            return "Flush"
        elif maxi>=3:
            return "Three of a Kind"
        elif maxi==2:
            return "Pair"
        return "High Card"

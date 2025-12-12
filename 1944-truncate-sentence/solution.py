class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        l=list(s.split())
        s=""
        for i in range(0,k-1):
            s=s+l[i]+' '
        return s+l[k-1]
            

class Solution:
    def minimumChairs(self, st: str) -> int:
        s=0
        maxi=0
        for i in st:
            if i=='E':
                s+=1
                maxi=max(maxi,s)
            else:
                s-=1
        return maxi
        

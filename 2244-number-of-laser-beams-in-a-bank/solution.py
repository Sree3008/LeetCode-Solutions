class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev=0
        res=0
        for i in bank:
            c=i.count('1')
            if(c>0):
                res=res+prev*c
                prev=c
        
        return res


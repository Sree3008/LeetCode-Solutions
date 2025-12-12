class Solution:
    def defangIPaddr(self, s: str) -> str:
        res=''
        for i in s:
            if i=='.':
                res=res+'['+i+']'
            else:
                res=res+i
        return res
                

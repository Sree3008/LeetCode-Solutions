class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        flag=False
        x=0
        res=''
        for i in s:
            if not flag and i=='(':
                flag=True
            elif flag and i=='(':
                res=res+'('
                x=x+1
            elif flag and i==')':
                if x>0:
                    x=x-1
                    res=res+')'
                else:
                    flag=False
        return res



                

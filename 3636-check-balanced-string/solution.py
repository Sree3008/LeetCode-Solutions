class Solution:
    def isBalanced(self, nu: str) -> bool:
        num=list(nu)
        e=0
        o=0
        for i in range(0,len(num)):
            if i%2==0:
                e+=int(num[i])
            else:
                o+=int(num[i])
        return e==o

        

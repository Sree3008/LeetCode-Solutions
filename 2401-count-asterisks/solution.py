class Solution:
    def countAsterisks(self, s: str) -> int:
        c=0
        b=False
        for i in s:
            if i=='|':
                b=not b 
            elif i=='*' and not b:  
                c+=1
        return c

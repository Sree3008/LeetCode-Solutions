class Solution:
    def residuePrefixes(self, s: str) -> int:
        c=0
        for i in range(1,len(s)+1):
            list1=s[:i]
            if len(set(list1))==len(list1)%3:
                c+=1
        return c
                

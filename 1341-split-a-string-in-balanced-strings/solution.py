class Solution:
    def balancedStringSplit(self, s: str) -> int:
        list1=list(s)
        c=0
        s=0
        for i in list1:
            if i=='R':
                c+=1
            else:
                c-=1
            if c==0:
                s+=1
        return s




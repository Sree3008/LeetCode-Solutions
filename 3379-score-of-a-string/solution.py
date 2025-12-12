class Solution:
    def scoreOfString(self, s: str) -> int:
        list1=list(map(ord,s))
        list2=[]
        x=0
        for i in range(1,len(list1)):
            x=abs(list1[i-1]-list1[i])
            list2.append(x)
        return sum(list2)

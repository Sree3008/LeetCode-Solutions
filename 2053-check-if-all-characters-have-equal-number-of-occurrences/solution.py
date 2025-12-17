class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        x=Counter(s)
        list1=[]
        for i,v in x.items():
            list1.append(v)
        y=set(list1)
        return len(y)==1

class Solution:
    def capitalizeTitle(self, t: str) -> str:
        x=list(map(str,t.lower().split()))
        l=[]
        for i in x:
            if len(i)>=3:
                l.append(i.capitalize())
            else:
                l.append(i)
        print(l)
        return ' '.join(l)

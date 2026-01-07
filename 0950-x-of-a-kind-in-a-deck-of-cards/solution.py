class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        x=Counter(deck)
        list1=[]
        for i,v in x.items():
            list1.append(v)
        g=list1[0]
        for i in list1:
            g=math.gcd(g,i)
        return g>=2

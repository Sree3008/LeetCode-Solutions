class Solution:
    def maxFreqSum(self, s: str) -> int:
        y="aeiou"
        x=Counter(s)
        print(x)
        l=[]
        l2=[]
        for i,v in x.items():
            if i in y:
                l.append(v)
            else:
                l2.append(v)
        a = max(l) if l else 0
        b = max(l2) if l2 else 0
        return a+b
        

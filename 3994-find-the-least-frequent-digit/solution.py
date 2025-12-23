class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        x=str(n)
        y=Counter(x)
        z=min(y.values())
        print(z)
        list1=[]
        c=0
        for i,v in y.items():
            if v==z:
                list1.append(int(i))
        return min(list1)
        

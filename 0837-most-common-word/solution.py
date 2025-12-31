class Solution:
    def mostCommonWord(self, p: str, banned: List[str]) -> str:
        f=p.lower()
        s=''
        for i in f:
            if i.isalpha():
                s+=i
            else:
                s+=' '
        k=s.split()
        j=[]
        for i in k:
            if i not in banned:
                j.append(i)
        x=Counter(j)
        res=max(x.values())
        for i,v in x.items():
            if v==res:
                return i

        

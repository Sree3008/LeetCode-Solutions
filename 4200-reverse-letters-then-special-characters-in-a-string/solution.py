class Solution:
    def reverseByType(self, s: str) -> str:
        let=[]
        spe=[]
        for ch in s:
            if 'a'<=ch<='z':
                let.append(ch)
            else:
                spe.append(ch)
        let.reverse()
        spe.reverse()
        res=[]
        l=sp=0
        for ch in s:
            if 'a'<=ch<='z':
                res.append(let[l])
                l+=1
            else:
                res.append(spe[sp])
                sp+=1
        return "".join(res)
        

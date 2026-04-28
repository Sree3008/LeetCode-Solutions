class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        s=0
        for i in words:
            temp=list(chars)
            b=0
            for j in i:
                if j in temp:
                    temp.remove(j)
                else:
                    b=1
                    break
            if b==0:
                s+=len(i)
        return s
            

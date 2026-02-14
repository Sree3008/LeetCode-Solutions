class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res=[]
        for i in words:
            t=0
            for ch in i:
                t+=weights[ord(ch)-ord('a')]
            val=t%26
            map_char=chr(ord('z')-val)
            res.append(map_char)
        return "".join(res)

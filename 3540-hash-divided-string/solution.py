class Solution:
    def stringHash(self, s: str, k: int) -> str:
        res='abcdefghijklmnopqrstuvwxyz'
        ans=''
        for i in range(0,len(s),k):
            j=0
            fin=s[i:i+k]
            for ch in fin:
                j+=res.index(ch)
            ans+=res[j%26]
        return ans


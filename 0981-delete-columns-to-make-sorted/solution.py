class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c=0
        n=len(strs[0])
        for i in range(n):
            for j in range(1,len(strs)):
                if strs[j][i]<strs[j-1][i]:
                    c+=1
                    break
        return c

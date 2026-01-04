class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        maxi=0
        idx=0
        for i in range(len(mat)):
            c=0
            for j in mat[i]:
                if j==1:
                    c+=1
            if c>maxi:
                maxi=c
                idx=i
        return [idx,maxi]
            


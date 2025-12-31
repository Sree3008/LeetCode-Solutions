class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        maxi=0
        x=0
        for i in range(len(grid)):
            c=0
            for j in grid[i]:
                if j==1:
                    c+=1
            if maxi<c:
                maxi=c
                x=i
        return x
               

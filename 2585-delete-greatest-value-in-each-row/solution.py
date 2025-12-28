class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        s=0
        for _ in range(len(grid[0])):    
            list1=[]
            for i in grid:
                maxi=max(i) 
                list1.append(maxi)
                i.remove(maxi)
            s+=max(list1)  
        return s
                    


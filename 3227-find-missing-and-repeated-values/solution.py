class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        list1=[]
        for i in grid:
            for j in i:
                list1.append(j)
        x=Counter(list1)
        res=0
        for i,v in x.items():
            if v>1:
                res=i
        y=set(list1)
        list3=list(y)
        # mini=min(list3)
        # maxi=max(list3)
        n=len(grid)
        list3.sort()
        z=0
        for i in range(1,n*n+1):
            if i not in list3:
                z=i
                break
        return [res,z]

    
                


        

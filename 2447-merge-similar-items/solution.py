class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        res={}
        for i,v in items1:
            res[i]=res.get(i,0)+v
        for i,v in items2:
            res[i]=res.get(i,0)+v
        ans=[] 
        for i in res:
            ans.append([i,res[i]])
        ans.sort()
        return ans

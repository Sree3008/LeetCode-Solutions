class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums=sorted(set(arr))
        rank={}
        list1=[]
        for i in range(len(nums)):
            rank[nums[i]]=i+1
        for i in arr:
            list1.append(rank[i])
        return list1
        

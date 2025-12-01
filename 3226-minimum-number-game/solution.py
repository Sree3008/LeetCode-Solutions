class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        res=[]
        heapq.heapify(nums)
        while nums:
            x,y=heapq.heappop(nums),heapq.heappop(nums)
            res.append(y)
            res.append(x)
        return res

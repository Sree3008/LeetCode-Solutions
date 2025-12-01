class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        x,y=heapq.nlargest(2,nums)
        return (x-1)*(y-1)
        

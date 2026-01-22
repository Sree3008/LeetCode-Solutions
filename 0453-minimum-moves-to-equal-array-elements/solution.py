class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(set(nums))==1:
            return 0
        x=min(nums)
        c=0
        for i in nums:
            c+=i-x
        return c



class Solution:
    def finalElement(self, nums: List[int]) -> int:
        k=nums[:]
        return max(k[0],k[-1])

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        maxi=0
        if len(nums)==1:
            return 0
        for i in range(1,len(nums)):
            x=nums[i]-nums[i-1]
            maxi=max(x,maxi)
        return maxi


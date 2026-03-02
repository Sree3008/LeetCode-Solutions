class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        maxi2=nums[0]
        maxi1=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            curr=max(maxi1,maxi2+nums[i])
            maxi2=maxi1
            maxi1=curr
        return maxi1

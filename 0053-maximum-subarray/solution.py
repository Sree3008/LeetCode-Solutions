class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        k_max=nums[0]
        sum1=nums[0] 
        for i in range(1,len(nums)):
            sum1=max(nums[i],sum1+nums[i]) 
            k_max=max(sum1,k_max)
        return k_max

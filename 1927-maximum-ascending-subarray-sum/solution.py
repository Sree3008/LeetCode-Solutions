class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        m_sum=c_sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c_sum=c_sum+nums[i]
            else:
                c_sum=nums[i]
            m_sum=max(m_sum,c_sum)
        return m_sum

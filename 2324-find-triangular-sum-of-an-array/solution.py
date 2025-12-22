class Solution:
    def sum_triangle(self,nums):
        if len(nums)==1:
            return nums[0]
        list1=[]
        for i in range(1,len(nums)):
            s=(nums[i-1]+nums[i])%10
            list1.append(s)
        return self.sum_triangle(list1)
    def triangularSum(self, nums: List[int]) -> int:
        return self.sum_triangle(nums)
        

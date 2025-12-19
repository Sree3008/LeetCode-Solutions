class Solution:
    def num_process(self,nums,original):
        for i in range(0,len(nums)):
            if nums[i]==original:
                x=nums[i]*2
                if x in nums:
                    return self.num_process(nums,x)
                else:
                    return x
        return original
    def findFinalValue(self, nums: List[int], original: int) -> int:
        return self.num_process(nums,original)
                

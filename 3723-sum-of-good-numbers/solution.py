class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        c=0
        n=len(nums)
        for i in range(len(nums)):
            b=True
            if i+k<n and nums[i+k]>=nums[i]: 
                b=False
            if i-k>=0 and nums[i]<=nums[i-k]:
                b=False
            if b:
                c+=nums[i]
        return c


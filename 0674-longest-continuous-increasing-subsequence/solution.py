class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        c=1
        maxi=1
        if len(set(nums))==1:
            return 1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                c+=1
                maxi=max(maxi,c)
            else:
                c=1
        return maxi
        

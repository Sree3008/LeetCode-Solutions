class Solution:
    def numberOfAlternatingGroups(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            if nums[i]==nums[(i+2)%len(nums)] and nums[i]!=nums[(i+1)%len(nums)]:
                c+=1
        return c
         

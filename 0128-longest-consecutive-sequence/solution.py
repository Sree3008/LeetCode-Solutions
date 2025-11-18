class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        c=1
        res=1
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                c=c+1
            elif nums[i]==nums[i-1]:
                continue
            else:
                c=1
            res=max(res,c)
        return res


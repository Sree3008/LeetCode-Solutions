class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        l=(n*(n+1))/2
        s=0
        for i in nums:
            s=s+i
        return int(l-s)
        

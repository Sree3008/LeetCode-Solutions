class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        ans=0
        i=0
        if k==0:
            return n
        l=nums[n-k]
        c=0
        for i in nums:
            if i<l:
                c+=1
        return c

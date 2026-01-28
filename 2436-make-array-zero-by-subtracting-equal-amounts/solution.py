class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        while True:
            res=[j for j in nums if j!=0]
            if not res:
                break
            mini=min(res)
            c+=1
            for i in range(len(nums)):
                if nums[i]!=0:
                    nums[i]=nums[i]-mini
        return c

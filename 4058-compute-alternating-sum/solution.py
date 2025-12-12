class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        e=0
        o=0
        for i in range(0,len(nums)):
            if i%2==0:
                e+=nums[i]
            else:
                o+=nums[i]
        return e-o


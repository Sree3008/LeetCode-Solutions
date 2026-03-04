class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        l1=[]
        for i in range(len(nums)):
            y=(i+nums[i])%(len(nums))
            l1.append(nums[y])
        return l1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l1=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l1.append(i)
        if l1:
            return [l1[0],l1[-1]]
        return [-1,-1]

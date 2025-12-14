class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        # if 2*k>len(nums):
        #     return 0
        x=sum(nums[:k])
        y=sum(nums[-k:])
        return abs(y-x)
        

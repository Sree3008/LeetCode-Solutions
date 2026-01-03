class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        f=False
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                continue
            if f:
                return False
            f=True
            if i == 1 or nums[i] > nums[i-2]:
                nums.pop(i-1)
            else:
                nums.pop(i)
            break
        print(nums)
        b=True
        for i in range(1,len(nums)):
            if nums[i]<=nums[i-1]:
                b=False
                break
        return b

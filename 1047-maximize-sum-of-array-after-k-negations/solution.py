class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:  
        nums.sort()
        for i in range(k):
            nums[0]=-nums[0]
            nums.sort()
        return sum(nums)

        # print(sum(l1))

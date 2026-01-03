class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        list1=[]
        while nums:
            x=(nums[0]+nums[-1])/2
            nums.pop(0)
            nums.pop()
            list1.append(x)
        return min(list1)

class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        list1=[]
        while nums:
            x=(nums[0]+nums[-1])/2
            list1.append(x)
            nums.pop(0)
            nums.pop()
        return len(set(list1))



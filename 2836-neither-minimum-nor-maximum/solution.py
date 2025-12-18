class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        list1=[]
        for i in range(1,len(nums)-1):
            list1.append(nums[i])
        print(list1)
        if len(list1)>=1:
            return list1[0]
        return -1

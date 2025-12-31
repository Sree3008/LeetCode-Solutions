class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        list1=[]
        for i in range(0,len(nums)):
            list1.insert(index[i],nums[i])
        return list1

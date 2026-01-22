class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        list1=[]
        for i in range(len(nums)):
            for j in range(1,len(nums)+1):
                if nums[i]<nums[(i+j)%len(nums)]:
                    list1.append(nums[(i+j)%len(nums)])
                    break
            else:
                list1.append(-1)
        return list1


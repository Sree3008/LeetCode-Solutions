class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        list1=[]
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
            list1=[]
            list2=[]
            for i in nums:
                if i==0:
                    list1.append(i)
                else:
                    list2.append(i)
        list2.extend(list1)
        return list2

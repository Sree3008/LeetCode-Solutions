class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        list1=[]
        for i in nums:
            if i%2==0:
                list1.append(0)
            else:
                list1.append(1)
        list1.sort() 
        return list1

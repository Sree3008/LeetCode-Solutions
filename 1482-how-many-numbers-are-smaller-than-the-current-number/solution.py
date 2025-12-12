class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        list1=[]
        for i in nums:
            c=0
            for j in nums:
                if i>j:
                    c+=1
            list1.append(c)
        return list1

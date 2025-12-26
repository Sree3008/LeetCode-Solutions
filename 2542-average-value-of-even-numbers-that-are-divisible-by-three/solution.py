class Solution:
    def averageValue(self, nums: List[int]) -> int:
        list1=[]
        for i in nums:
            if i%2==0 and i%3==0:
                list1.append(i)
        if len(list1) == 0:
            return 0
        y=sum(list1)//len(list1)
        return y

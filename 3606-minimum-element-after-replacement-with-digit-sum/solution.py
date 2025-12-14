class Solution:
    def minElement(self, nums: List[int]) -> int:
        list1=[]
       
        for i in nums:
            x=0
            for j in str(i):
                x+=int(j)
            list1.append(x)
        return min(list1)



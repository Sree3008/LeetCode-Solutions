class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        list1=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                list1.append(len(set(nums[i:j]))) 
        print(list1)
        s=0
        for i in list1:
            s+=i*i
        return s

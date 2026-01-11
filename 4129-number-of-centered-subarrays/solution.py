class Solution:
    def centeredSubarrays(self, nums: List[int]) -> int:
        list1=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                list1.append(nums[i:j])
        c=0
        for i in list1:
            s=sum(i)  
            if s in i:
                c+=1 
        return c
                

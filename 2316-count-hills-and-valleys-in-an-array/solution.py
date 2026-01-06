class Solution:
    def countHillValley(self, num: List[int]) -> int:
        c=0
        nums=[num[0]]
        for i in range(1,len(num)):
            if num[i]!=num[i-1]:
                nums.append(num[i])
        for i in range(1,len(nums)-1):
            if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                c+=1
            elif nums[i-1]>nums[i] and nums[i]<nums[i+1]: 
                c+=1 
        return c

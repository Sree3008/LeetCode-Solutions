class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        list1=sorted(nums)
        print(nums)
        c=0
        for i in range(len(nums)):
            if nums==list1:
                return c
            x=nums.pop()
            nums.insert(0,x)
            c+=1
            
        return -1

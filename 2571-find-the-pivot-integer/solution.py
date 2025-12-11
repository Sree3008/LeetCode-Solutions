class Solution:
    def pivotInteger(self, n: int) -> int:
        # nums=[1,2,3,4,5,6,7,8]
        nums=[]
        for i in range(1,n+1):
            nums.append(i)
        left=0
        total=sum(nums)
        for i in range(len(nums)):
            right=total-left-nums[i]
            if left==right:
                return nums[i]
            left=left+nums[i]
        return -1

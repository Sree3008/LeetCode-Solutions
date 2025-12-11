class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        left=0
        total=sum(nums)
        cur=0
        c=0
        for i in range(len(nums)-1):
            left=left+nums[i]
            right=total-left
            cur=left-right
            if cur%2==0:
                c+=1
           
        return c


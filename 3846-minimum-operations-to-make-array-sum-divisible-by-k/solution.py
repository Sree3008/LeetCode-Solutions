class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        x=sum(nums)
        c=0
        if x%k==0:
            return 0
        while x%k!=0:
            c+=1
            x-=1
        return c




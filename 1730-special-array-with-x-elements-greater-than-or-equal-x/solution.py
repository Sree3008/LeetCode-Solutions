class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n=len(nums)
        for x in range(n+1):
            c=0
            for i in nums:
                if i>=x:
                    c+=1
            if c==x:
                return x
        return -1 

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if 0<=i<j<k<n and  nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                        c+=1
        return c

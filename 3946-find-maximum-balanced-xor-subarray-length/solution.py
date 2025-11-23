class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        nv=nums[:]
        n=len(nums)
        px=0
        bal=0
        seen={(0,0):-1}
        best=0
        for i,x in enumerate(nums):
            px^=x
            if x%2==0:
                bal+=1
            else:
                bal-=1
            key=(px,bal)
            if key in seen:
                best=max(best,i-seen[key])
            else:
                seen[key]=i
        return best

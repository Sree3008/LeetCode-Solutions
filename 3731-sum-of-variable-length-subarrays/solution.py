class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        prefix=[0]
        for i in nums:
            prefix.append(prefix[-1]+i)
        print(prefix)
        s=0
        for i in range(len(nums)):
            st=max(0,i-nums[i])
            s+=prefix[i+1]-prefix[st]
        return s
        

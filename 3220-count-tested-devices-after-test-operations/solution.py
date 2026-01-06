class Solution:
    def countTestedDevices(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            if i>ans:
                ans+=1
        return ans

        

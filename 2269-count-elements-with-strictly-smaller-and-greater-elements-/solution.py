class Solution:
    def countElements(self, nums: List[int]) -> int:
        mini=min(nums)
        maxi=max(nums)
        c=0
        for i in nums:
            if mini<i<maxi:
                c+=1
        return c
        

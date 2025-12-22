class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        x=Counter(nums)
        maxi=max(x.values())
        c=0
        for i,v in x.items():
            if v==maxi:
                c+=v
        
        return c

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        x=Counter(nums)
        y=max(x.values())
        for i,v in x.items():
            if y==v:
                return i
        return -1 
        

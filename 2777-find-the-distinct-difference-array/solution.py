class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        res=[]
        for i in range(len(nums)):
            l=len(set(nums[:i+1]))
            r=len(set(nums[i+1:]))
            res.append(l-r)
        return res


            
        

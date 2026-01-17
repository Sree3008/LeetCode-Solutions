class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        w_v=set()
        for a,b in zip(nums,target):
            if a!=b:
                w_v.add(a)
        return len(w_v)
        

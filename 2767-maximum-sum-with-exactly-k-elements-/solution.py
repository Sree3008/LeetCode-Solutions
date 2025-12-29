class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxi=max(nums)
        s=0
        for i in range(k):
            s+=maxi
            maxi+=1
        return s

                


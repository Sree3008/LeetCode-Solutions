class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        cat=0
        left=0
        right=len(nums)-1
        while left<right:
            s=str(nums[left])+str(nums[right]) 
            cat+=int(s)
            left+=1
            right-=1
        if left==right:
            cat+=nums[left]
        return cat 



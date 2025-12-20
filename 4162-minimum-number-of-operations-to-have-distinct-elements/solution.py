class Solution:
    def minOperations(self, nums: List[int]) -> int:
        seen =set()
        n=len(nums)
        i=n-1
        while i>=0:
            if nums[i] in seen:
                break
            seen.add(nums[i])
            i-=1
        remove=i+1
        return (remove+2)//3
        

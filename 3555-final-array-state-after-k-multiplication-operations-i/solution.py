class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k>0:
            x=min(nums)
            print(x)
            for i in range(len(nums)):
                if x==nums[i]:
                    nums[i]=x*multiplier
                    break
            print(nums)
            k-=1
        return nums
        
                

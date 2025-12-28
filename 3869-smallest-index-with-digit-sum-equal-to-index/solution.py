class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        mini=float('inf')
        for i in range(len(nums)): 
            s=0
            while nums[i]!=0:
                n=nums[i]%10
                s+=n
                nums[i]//=10
            if s==i:
                mini=min(s,mini)
        if mini!=float(inf):
            return mini
        return -1
        

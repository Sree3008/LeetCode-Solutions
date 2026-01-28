class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums)>1:
            res=[]
            for i in range(len(nums)//2):
                if i%2==0:
                    res.append(min(nums[2*i], nums[2*i + 1]))
                else:
                    res.append(max(nums[2*i], nums[2*i + 1]))
            nums=res
        return nums[0]
        
        


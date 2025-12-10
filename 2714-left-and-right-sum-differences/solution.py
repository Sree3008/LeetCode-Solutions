class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        pre=[0]
        suf=[0]
        for i in range(1,len(nums)):
            pre.append(pre[-1]+nums[i-1])
        for i in range(len(nums)-1,0,-1):
            suf.insert(0,suf[0]+nums[i])
        res=[]
        for i in range(len(nums)):
            res.append(abs(pre[i]-suf[i]))
        return res


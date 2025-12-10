class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]
        suf = [1]
        # nums = [1,2,3,4]
        # pre = [1,1,2,6]
        # suf = [24,12,4,1]
        for i in range(1,n):
            pre.append(pre[-1]*nums[i-1])
        for i in range(n-1,0,-1):
            suf.insert(0,suf[0]*nums[i])
        res = []
        for i in range(n):
            res.append(pre[i]*suf[i])
        return res

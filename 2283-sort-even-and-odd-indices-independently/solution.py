class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        e=[]
        o=[]
        for i in range(len(nums)):
            if i%2==0:
                e.append(nums[i])
            else:
                o.append(nums[i])
        e.sort()
        o.sort(reverse=True)
        res=[]
        for i in range(len(nums)):
            if i%2==0:
                res.append(e[i//2])
            else:
                res.append(o[i//2])
        return res 


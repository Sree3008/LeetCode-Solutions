class Solution:
    def minimumK(self, nums: List[int]) -> int:
        ven=nums
        def nonPos(k):
            return sum((x+k-1)//k for x in ven)
        l=1
        r=max(max(ven),len(ven))
        while l<r:
            mid=(l+r)//2
            if nonPos(mid)<=mid*mid:
                r=mid
            else:
                l=mid+1
        return l
        

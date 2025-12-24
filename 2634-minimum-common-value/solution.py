class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        x=set(nums1)
        y=set(nums2)
        z=x.intersection(y)
        if not z:
            return -1
        a=list(z)
        a.sort()
        return a[0]

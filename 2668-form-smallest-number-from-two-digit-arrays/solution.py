class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        list1=[]
        n1=set(nums1)
        n2=set(nums2)
        x=n1 & n2
        if x:
            return min(x)
        min1 = min(nums1)
        min2 = min(nums2)
        return int(str(min(min1, min2)) + str(max(min1, min2)))

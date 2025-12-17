class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        l1=[]
        x=Counter(nums1)
        y=Counter(nums2)
        for i in nums1:
            if i not in nums2 and i not in l1:
                l1.append(i)
        l2=[]
        for i in nums2:
            if i not in nums1 and i not in l2:
                l2.append(i)
        l3=[]
        l3.append(l1)
        l3.append(l2)
        return l3


class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1=0
        n2=0
        for i in nums1:
            if i in nums2:
                n1+=1
        for i in nums2:
            if i in nums1:
                n2+=1
        l=[]
        l.append(n1)
        l.append(n2)
        return l
        
